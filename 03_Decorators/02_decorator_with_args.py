def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before execution")

        result = func(*args, **kwargs)

        print("After execution")

        return result

    return wrapper


@decorator
def add(a, b):
    return a + b


print("Result:", add(5, 3))