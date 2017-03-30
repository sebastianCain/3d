from math import sin, cos, pi
from matrix import *
from draw import *

def circx(x, t, r):
    return r * cos(2 * pi * t) + x

def circy(y, t, r):
    return r * sin(2 * pi * t) + y

def add_circle(matrix, x, y, z, r):
    return draw_parametric(matrix, x, y, z, r, circx, circy, 0.01)

def cubicx(x, t, c):
    #xc is x coefficients
    xc = c[0]
    return (xc[0] * (t ** 3)) + (xc[1] * (t ** 2)) + (xc[2] * t) + xc[3] 

def cubicy(y, t, c):
    #yc is y coefficients
    yc = c[1]
    return (yc[0] * (t ** 3)) + (yc[1] * (t ** 2)) + (yc[2] * t) + yc[3]

def add_curve(matrix, type, vals):

    xdata = vals[::2]
    ydata = vals[1::2]
    
    xc = get_coefficients(type, xdata)
    yc = get_coefficients(type, ydata)

    coeffs = [xc, yc]

    return draw_parametric(matrix, vals[0], vals[1], 0, coeffs, cubicx, cubicy, 0.01) 

def generate_sphere(cx, cy, cz, r):
    points = []

    rot = 0.01
    while rot < 1.001:        
        circ = 0.01
        while circ < 1.001:
            point = []
            point.append(r * cos(2 * pi * circ) + cx)
            point.append(r * sin(2 * pi * circ) * cos(2 * pi * rot) + cy)
            point.append(r * sin(2 * pi * circ) * cos(2 * pi * rot) + cz)
            point.append(1)

            points.append(point)

            circ += 0.01
            print("circ: " + str(circ))
        rot += 0.01
        print("ROT: " + str(rot))

    return points

def add_sphere(matrix, x, y, z, r):
    points = generate_sphere(x, y, z, r)
    for p in points:
        matrix = add_edge(matrix, p[0], p[1], p[2], p[0] + 1, p[1], p[2])
    return matrix

def generate_torus(cx, cy, cz, r, R):
    points = []

    rot = 0.01
    while rot < 1.001:
        circ = 0.01
        while circ < 1.001:
            point = []
            point.append(cos(2 * pi * rot) * (r * cos(2 * pi * circ) + R) + cx)
            point.append(r * sin(2 * pi * circ) + cy)
            point.append(-(sin(2 * pi * rot)) * (r * cos(2 * pi * circ) + R) + cz)
            point.append(1)

            points.append(point)

            circ += 0.01
        rot += 0.01

    return points

def add_torus(matrix, x, y, z, r, R):
    points = generate_torus(x, y, z, r, R)
    for p in points:
        matrix = add_edge(matrix, p[0], p[1], p[2], p[0] + 1, p[1], p[2])
    return matrix

def generate_box(cx, cy, cz, w, h, d):
    points = []
    points.append([cx, cy, cz, 1])
    points.append([cx+w, cy, cz, 1])
    points.append([cx, cy-h, cz, 1])
    points.append([cx, cy, cz-d, 1])
    points.append([cx+w, cy-h, cz, 1])
    points.append([cx, cy-h, cz-d, 1])
    points.append([cx+w, cy, cz-d, 1])
    points.append([cx+w, cy-h, cz-d, 1])

    return points

def add_box(matrix, x, y, z, w, h, d):
    points = generate_box(x, y, z, w, h, d)
    for p in points:
        matrix = add_edge(matrix, p[0], p[1], p[2], p[0] + 1, p[1], p[2])
    return matrix
