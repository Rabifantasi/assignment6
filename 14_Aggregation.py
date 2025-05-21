# Create a class Department and a class Employee. 
# Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee

    def get_details(self):
        return f"{self.employee.name} works in {self.department_name} department"

emp = Employee("Rabia")
dept = Department("HR", emp)

print(dept.get_details())
