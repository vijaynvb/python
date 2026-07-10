students = {
    101: "Avinash",
    102: "Rahul",
    103: "Priya"
}

print("Student Records")
print("Student ID 101:", students[101])

students[104] = "Kiran"

print("\nAll Students:")
for student_id, name in students.items():
    print(student_id, "-", name)