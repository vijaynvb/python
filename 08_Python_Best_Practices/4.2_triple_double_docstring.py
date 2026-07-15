def my_func_preferred():
    """This is a docstring using triple double quotes."""
    return None


print("Using __doc__:")
print(my_func_preferred.__doc__)

print("\nUsing help():")
help(my_func_preferred)