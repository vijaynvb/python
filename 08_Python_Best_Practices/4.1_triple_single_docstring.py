def my_func():
    '''This is a docstring using triple single quotes.'''
    return None


print("Using __doc__:")
print(my_func.__doc__)

print("\nUsing help():")
help(my_func)