import numpy as np
import matplotlib.pyplot as plt

def draw_circle(center, radius, ax, color='blue'):
    x0, y0 = center
    # Create a grid of points
    theta = np.linspace(0, 2 * np.pi, 100)
    x = x0 + radius * np.cos(theta)
    y = y0 + radius * np.sin(theta)
    ax.plot(x, y, color=color)

def main():
    try:
        # Take input from user
        radius = float(input("Enter the radius of the circle: "))
        
        x_center = float(input("Enter the x-coordinate of the center of the first circle: "))
        y_center = float(input("Enter the y-coordinate of the center of the first circle: "))
        
        xi = float(input("Enter the x-coordinate of the second circle's center: "))
        yi = float(input("Enter the y-coordinate of the second circle's center: "))
        
        # Create a figure and axis
        fig, ax = plt.subplots()

        # Draw the circles
        draw_circle((0, 0), radius, ax, color='blue')        # Circle centered at origin
        draw_circle((xi, yi), radius, ax, color='red')        # Circle centered at (xi, yi)

        # Set the aspect ratio of the plot to be equal
        ax.set_aspect('equal', 'box')

        # Set limits to make sure circles are fully visible
        ax.set_xlim([-radius-1, radius+1])
        ax.set_ylim([-radius-1, radius+1])

        # Add grid and labels
        ax.grid(True)
        ax.set_title('Brehenham\'s Circle Drawing Algorithm')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')

        # Show plot
        plt.show()
        
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter numeric values for radius and coordinates.")

if __name__ == "__main__":
    main()
