class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_employee(self):
        print("Employee Details")
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)


 
class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    def display_manager(self):
        self.display_employee()
        print("Department:", self.department)


 
manager = Manager("Avinash", "EMP101", "IT")

manager.display_manager()