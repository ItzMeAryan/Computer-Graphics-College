wap to translate an object with translation parameters in x & y directions.
---> create an object (ask from user whether rectangle, circle, ellipse)
---> ask translate parameters from user
---> show original object & translated object as output.
---> implement same in OpenGL


import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Ellipse

# Function to get user inputs for the shape and translation
def get_shape_details():
    shape = input("Enter the shape (rectangle, circle, ellipse): ").strip().lower()
    
    if shape == 'rectangle':
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        return shape, width, height
    elif shape == 'circle':
        radius = float(input("Enter the radius of the circle: "))
        return shape, radius, 0  # Circle only needs radius, height is irrelevant
    elif shape == 'ellipse':
        width = float(input("Enter the width of the ellipse: "))
        height = float(input("Enter the height of the ellipse: "))
        return shape, width, height
    else:
        print("Invalid shape selected. Please choose rectangle, circle, or ellipse.")
        return get_shape_details()

# Function to plot the original and translated objects
def plot_shapes(shape, dimensions, tx, ty):
    fig, ax = plt.subplots()

    # Create the original shape
    if shape == 'rectangle':
        rect = Rectangle((0, 0), dimensions[0], dimensions[1], edgecolor='blue', facecolor='none', lw=2)
        translated_rect = Rectangle((tx, ty), dimensions[0], dimensions[1], edgecolor='red', facecolor='none', lw=2)
        ax.add_patch(rect)
        ax.add_patch(translated_rect)

    elif shape == 'circle':
        circle = Circle((0, 0), dimensions[0], edgecolor='blue', facecolor='none', lw=2)
        translated_circle = Circle((tx, ty), dimensions[0], edgecolor='red', facecolor='none', lw=2)
        ax.add_patch(circle)
        ax.add_patch(translated_circle)

    elif shape == 'ellipse':
        ellipse = Ellipse((0, 0), dimensions[0], dimensions[1], edgecolor='blue', facecolor='none', lw=2)
        translated_ellipse = Ellipse((tx, ty), dimensions[0], dimensions[1], edgecolor='red', facecolor='none', lw=2)
        ax.add_patch(ellipse)
        ax.add_patch(translated_ellipse)

    # Set axis limits to view both shapes properly
    ax.set_xlim(-10, 10 + max(dimensions[0], tx))
    ax.set_ylim(-10, 10 + max(dimensions[1], ty))

    # Set equal scaling
    ax.set_aspect('equal')

    # Show grid and legend
    plt.grid(True)
    plt.title(f"Original {shape} in blue and Translated {shape} in red")
    plt.show()

# Main function to run the program
def main():
    # Get the shape and dimensions from the user
    shape, width, height = get_shape_details()

    # Ask for translation parameters
    tx = float(input("Enter the translation in the x direction: "))
    ty = float(input("Enter the translation in the y direction: "))

    # Plot the original and translated objects
    plot_shapes(shape, (width, height), tx, ty)

# Run the program
main()
