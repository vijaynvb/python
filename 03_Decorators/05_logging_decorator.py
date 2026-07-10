def logger(func):

    def wrapper():

        print(f"[LOG] Function '{func.__name__}' started")

        func()

        print(f"[LOG] Function '{func.__name__}' completed")

    return wrapper


@logger
def process_order():

    print("Processing customer order...")


process_order()