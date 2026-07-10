def employee_ids():

    yield 101
    yield 102
    yield 103


emp = employee_ids()

print(next(emp))
print(next(emp))
print(next(emp))