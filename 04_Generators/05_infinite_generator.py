def infinite_numbers():

    num = 1

    while True:
        yield num
        num += 1


numbers = infinite_numbers()

for _ in range(5):
    print(next(numbers))