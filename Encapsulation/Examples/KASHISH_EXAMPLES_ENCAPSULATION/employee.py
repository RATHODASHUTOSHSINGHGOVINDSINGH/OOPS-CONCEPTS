class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def update_salary(self, amount):
        if amount > 0:
            self.__salary = amount
            print("Updated salary:", self.__salary)
        else:
            print("Invalid salary")

emp = Employee(30000)
emp.update_salary(70000)
emp = Employee(30000)
emp.update_salary(35000)