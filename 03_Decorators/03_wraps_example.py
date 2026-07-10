from functools import wraps

def decorator(func):

    @wraps(func)
    def wrapper():
        print("Before execution")

        func()

        print("After execution")

    return wrapper

@decorator
def greet():
    """Greeting Function"""
    print("Hello, World!")

greet()
print("\nFunction Name:", greet.__name__)