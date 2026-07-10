import time

def timer(func):

    def wrapper():

        start_time = time.time()

        func()

        end_time = time.time()

        print("Execution Time:",
              round(end_time - start_time, 2),
              "seconds")

    return wrapper

@timer
def process_data():

    time.sleep(2)

    print("Processing completed")

process_data()

