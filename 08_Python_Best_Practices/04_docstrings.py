def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
        length (float): Length of the rectangle
        width (float): Width of the rectangle

    Returns:
        float: Area of the rectangle
    """

    return length * width


area = calculate_area(10, 5)

print("Area:", area)

print("\nFunction Documentation:")
print(calculate_area.__doc__)