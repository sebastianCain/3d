from display import *

def draw_line(screen, x0, y0, x1, y1, color):
    x = 0.0
    y = 0.0

    #account for left side of drawing by swapping
    if x0 <= x1:
        x = x0
        y = y0
    else:
        x = x1
        x1 = x0
        y = y1
        y1 = y0



    A = y1 - y
    B = -(x1 - x)
    
    if x == x1:
        if y < y1:
            while y <= y1:
                plot(screen, color, x, y)
                y += 1
        else:
            while y >= y1:
                plot(screen, color, x, y)
                y -= 1
        return
        #some shit
    
    slope = float(y1 - y)/float(x1 - x)
    
    if slope > 1.0: #oct 2
        d = (2 * B) + A
        A *= 2; B *= 2
        while y <= y1:
            plot(screen, color, x, y)
            if d < 0:
                x += 1
                d += A
            y += 1
            d += B
    elif slope >= 0.0:
        d = (2 * A) + B
        A *= 2; B *= 2
        while x <= x1: #oct 1
            plot(screen, color, x, y)
            if d > 0:
                y += 1
                d += B
            x += 1
            d += A
    elif slope >= -1.0: #oct 8
        d = (2 * A) - B
        A *= 2; B *= 2
        while x <= x1:
            plot(screen, color, x, y)
            if d < 0:
                y -= 1
                d -= B
            x += 1
            d += A
    elif slope < 1.0: #oct 7
        d = A - (2 * B)
        A *= 2; B *= 2
        while y >= y1:
            plot(screen, color, x, y)
            if d > 0:
                x += 1
                d += A
            y -= 1
            d -= B

def draw_parametric(matrix, x, y, z, data, fx, fy, step = 0.01):
    t = 0.0
    #tx0, ty0, tx1, ty1 = 0.0
    stop = 1.001

    tx0 = fx(x, 0, data)
    ty0 = fy(y, 0, data)

    while t <= stop:
        tx1 = fx(x, t, data)
        ty1 = fy(y, t, data)
        
        matrix = add_edge(matrix, tx0, ty0, 0, tx1, ty1, 0)
        
        tx0 = tx1
        ty0 = ty1
        t += step
    return matrix

def draw_lines(screen, matrix, color):
    i = 0
    #print "m len: " + str(len(matrix))
    while i < len(matrix):
        if color == None:
            r = int(random.random()*255)
            g = int(random.random()*255)
            b = int(random.random()*255)
            color = [r, g, b]
#        try:
        draw_line(screen, int(matrix[i][0]), int(matrix[i][1]), int(matrix[i+1][0]), int(matrix[i+1][1]), color)
#        except:
#            print "odd number of points, u fail!! pls make even number of points so things can work"
        i += 2
