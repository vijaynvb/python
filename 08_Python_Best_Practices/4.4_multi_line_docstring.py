def add(a, b):
    """
    Add two numbers.

    Parameters:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: Sum of a and b.
    """
    return a + b


print("Result:", add(3, 7))

print("\nUsing __doc__:")
print(add.__doc__)

print("\nUsing help():")
help(add)