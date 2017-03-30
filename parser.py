from piecewise import *
from transform import *
from display import *
from matrix import *
from draw import *

from time import sleep
from math import pi


def parse_file(fname, points, transform, screen, color):
    f = open(fname, 'r')
    lines = f.readlines()
    i = 0
    while i < len(lines):
        cmd = lines[i].strip()
        #print(cmd + " - " + str(i))
#        try:
        if cmd == "line":
            args = lines[i+1].strip().split()
            for k in range(len(args)):
                args[k] = float(args[k])
            points = add_edge(points, args[0], args[1], args[2], args[3], args[4], args[5])
            i += 2
        elif cmd == "ident":
            transform = identity_mtrx()
            i += 1
        elif cmd == "scale":
            args = lines[i+1].strip().split()
            for k in range(len(args)):
                args[k] = float(args[k])
            transform = scale(transform, args[0], args[1], args[2])
            i += 2
        elif cmd == "move":
            args = lines[i+1].strip().split()
            for k in range(len(args)):
                args[k] = float(args[k])
            transform = translate(transform, args[0], args[1], args[2])
            i += 2
        elif cmd == "rotate":
            args = lines[i+1].strip().split()
            theta = (float(args[1])/180) * pi
            if args[0] == "x":
                transform = rotateX(transform, theta)
            elif args[0] == "y":
                transform = rotateY(transform, theta)
            elif args[0] == "z":
                transform = rotateZ(transform, theta)
            else:
                raise Exception("not an axis, try again")
            i += 2
        elif cmd == "circle":
            args = lines[i+1].strip().split()
            for k in range(len(args)):
                args[k] = float(args[k])
            points = add_circle(points, args[0], args[1], args[2], args[3])
            i += 2
        elif cmd == "hermite":
            args = lines[i+1].strip().split()
            for k in range(len(args)):
                args[k] = float(args[k])
            points = add_curve(points, "h", args)
            i += 2
        elif cmd == "bezier":
            args = lines[i+1].strip().split()
            for k in range(len(args)):
                args[k] = float(args[k])
            points = add_curve(points, "b", args)
            i += 2
        elif cmd == "box":
            args = lines[i+1].strip().split()
            for k in range(len(args)):
                args[k] = float(args[k])
            points = add_box(points, args[0], args[1], args[2], args[3], args[4], args[5])
            i += 2
        elif cmd == "sphere":
            args = lines[i+1].strip().split()
            for k in range(len(args)):
                args[k] = float(args[k])
            points = add_sphere(points, args[0], args[1], args[2], args[3])
            i += 2
        elif cmd == "torus":
            args = lines[i+1].strip().split()
            for k in range(len(args)):
                args[k] = float(args[k])
            points = add_torus(points, args[0], args[1], args[2], args[3], args[4])
            i += 2
        elif cmd == "clear":
            points = []
            transform = identity_mtrx()
            i += 1
        elif cmd == "apply":
            display_mtrx(transform)
            points = mtrx_mult(points, transform)
            i += 1
        elif cmd == "display":
            sleep(1)
            draw_lines(screen, points, color)
            display(screen)
            i += 1
        elif cmd == "save":
            #display_mtrx(points)
            #for k in points:
            #    k[0] += 200
            #    k[1] += 200
            arg = lines[i+1].strip()
            #draw_lines(screen, points, color)
            save_extension(screen, arg)
            i += 2
        elif cmd == "quit":
            return
        elif cmd[0] == "#":
            i += 1
        else:
            print("INVALID COMMAND:" + cmd)
            i += 1
#            raise Exception("invalid command" + cmd)
#        except:
#            print "invalid file to parse. please edit and try again"
