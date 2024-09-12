# implement DDA line drawing algorithm.
import matplotlib.pyplot as plt
def plot_line(x1, y1, x2, y2):
    if abs(x2 - x1) >= abs(y2 - y1):
        length = abs(x2 - x1)
    else:
        length = abs(y2 - y1)
    xincr = (x2 - x1) / length
    yincr = (y2 - y1) / length    
    x = x1 + 0.5
    y = y1 + 0.5
    i = 1    
    x_coords = []
    y_coords = []    
    while i <= length:
        x_coords.append(int(x))
        y_coords.append(int(y))
        x = x + xincr
        y = y + yincr
        i = i + 1
    x_coords.append(x2)
    y_coords.append(y2)    
    # plt.plot(x_coords, y_coords, marker='o', linestyle='None')
    plt.plot(x_coords, y_coords, marker='o')
    plt.title(f'Line from ({x1}, {y1}) to ({x2}, {y2})')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()
x1, y1 = 2, 3
x2, y2 = 12, 8
plot_line(x1, y1, x2, y2)
