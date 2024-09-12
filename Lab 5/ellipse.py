import matplotlib.pyplot as plt

def draw_ellipse(xc, yc, rx, ry):
    x = 0
    y = ry
    rx2 = rx * rx
    ry2 = ry * ry
    tworx2 = 2 * rx2
    twory2 = 2 * ry2
    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)
    
    boundary_x_coords = []
    boundary_y_coords = []

    def plot_ellipse_points(xc, yc, x, y):
        boundary_x_coords.extend([xc + x, xc - x, xc + x, xc - x])
        boundary_y_coords.extend([yc + y, yc + y, yc - y, yc - y])

    plot_ellipse_points(xc, yc, x, y)
    
    while (twory2 * x) < (tworx2 * y):
        x += 1
        if p1 < 0:
            p1 += twory2 * x + ry2
        else:
            y -= 1
            p1 += twory2 * x + ry2 - tworx2 * y
        plot_ellipse_points(xc, yc, x, y)

    p2 = ry2 * (x + 0.5) * (x + 0.5) + rx2 * (y - 1) * (y - 1) - rx2 * ry2
    while y > 0:
        y -= 1
        if p2 > 0:
            p2 += rx2 - tworx2 * y
        else:
            x += 1
            p2 += twory2 * x + rx2 - tworx2 * y
        plot_ellipse_points(xc, yc, x, y)

    # Plot only the boundary points
    plt.scatter(boundary_x_coords, boundary_y_coords, c='b', s=10)  # 'b' for blue color, s=10 for point size
    plt.gca().set_aspect('equal', adjustable='box')

draw_ellipse(0, 0, 70, 40)
plt.title("Midpoint Ellipse Algorithm with Boundary Points Only")
plt.show()
