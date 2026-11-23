class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)


class Developer(Employee):
    def show_role(self):
        print("Role: Software Developer")


emp = Developer("Rahul", 50000)

emp.display_details()
emp.show_role()