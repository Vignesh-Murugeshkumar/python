
class Employee:

    def __init__(self, name, employee_id, salary):
        self.name=name
        self.employee_id=employee_id
        self.salary=salary

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary}")

class Developer(Employee):

    def __init__(self, name, employee_id, salary, language):
        super().__init__(name, employee_id, salary)
        self.language=language

    def display_role(self):
        print(f"Role: Developer")
        print(f"Programming Language: {self.language}")


class Manager(Employee):

    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size=team_size

    def display_role(self):
        print(f"Role: Manager")
        print(f"Team Size: {self.team_size}")


# Test
dev = Developer("Vignesh", 101, 50000, "Python")
mgr = Manager("Arun", 102, 70000, 5)

dev.display_details()
dev.display_role()

mgr.display_details()
mgr.display_role()
