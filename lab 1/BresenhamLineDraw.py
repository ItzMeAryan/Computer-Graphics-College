import matplotlib.pyplot as plt

def plot_line_gentle_slope(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    if dx >= dy:
        length = dx
    else:
        length = dy
    
    d = 2 * dy - dx
    
    incr1 = 2 * dy - 2 * dx
    incr2 = 2 * dy
    
    if x2 > x1:
        xincr = 1
    else:
        xincr = -1
    
    if y2 > y1:
        yincr = 1
    else:
        yincr = -1
    
    x = x1
    y = y1
    
    x_points = [x]
    y_points = [y]
    
    for i in range(length):
        if d >= 0:
            x += xincr
            y += yincr
            d += incr1
        else:
            x += xincr
            d += incr2
        
        x_points.append(x)
        y_points.append(y)
    
    plt.plot(x_points, y_points, marker='o')
    plt.title(f"Line Segment from ({x1}, {y1}) to ({x2}, {y2})")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

x1, y1 = 2, 3
x2, y2 = 12, 8

plot_line_gentle_slope(x1, y1, x2, y2)
