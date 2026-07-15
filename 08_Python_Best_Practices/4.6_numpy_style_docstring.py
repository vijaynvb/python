def divide(a, b):
    """
    Divide two numbers.

    Parameters
    ----------
    a : float
        Dividend.
    b : float
        Divisor.

    Returns
    -------
    float
        Quotient of division.
    """

    if b == 0:
        raise ValueError("Division by zero is not allowed.")

    return a / b


print("Result:", divide(6, 2))

print("\nUsing __doc__:")
print(divide.__doc__)

print("\nUsing help():")
help(divide)