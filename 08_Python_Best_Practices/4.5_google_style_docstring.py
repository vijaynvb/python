def multiply(a, b):
    """
    Multiply two numbers.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: Product of a and b.
    """
    return a * b


print("Result:", multiply(3, 5))

print("\nUsing __doc__:")
print(multiply.__doc__)

print("\nUsing help():")
help(multiply)