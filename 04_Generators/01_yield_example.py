def employee_ids():
    yield 101
    yield 102
    yield 103


#print(employee_ids() )

for emp_id in employee_ids():
    print("Employee ID:", emp_id)