contacts = {
    "Avinash": "9876543210",
    "Rahul": "9876543211",
    "Priya": "9876543212"
}

print("Avinash:", contacts["Avinash"])

contacts["Kiran"] = "9876543213"

print("\nAll Contacts:")

for name, number in contacts.items():
    print(name, "-", number)
    