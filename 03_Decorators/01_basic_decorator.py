def decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper


@decorator # customfunc = decorator(greet)
           # customfunc() 
def greet():
    print("Hello, World!")


greet()