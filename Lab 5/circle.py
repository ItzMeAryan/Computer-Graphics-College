# WAP to draw a circle and ellipse using mid point algorithm.

import matplotlib.pyplot as plt

def draw_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r
    
    boundary_x_coords = []
    boundary_y_coords = []

    def plot_circle_points(xc, yc, x, y):
        boundary_x_coords.extend([xc + x, xc - x, xc + x, xc - x, xc + y, xc - y, xc + y, xc - y])
        boundary_y_coords.extend([yc + y, yc + y, yc - y, yc - y, yc + x, yc + x, yc - x, yc - x])

    plot_circle_points(xc, yc, x, y)
    
    while x < y:
        x += 1
        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * (x - y) + 1
        plot_circle_points(xc, yc, x, y)

    # Plot only the boundary points
    plt.scatter(boundary_x_coords, boundary_y_coords, c='b', s=10)  # 'b' for blue color, s=10 for point size
    plt.gca().set_aspect('equal', adjustable='box')

draw_circle(0, 0, 50)
plt.title("Midpoint Circle Algorithm with Boundary Points Only")
plt.show()
