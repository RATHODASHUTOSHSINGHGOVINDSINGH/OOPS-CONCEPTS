
class Employee:
    def __init__(self, name, salary, password):
        self.name = name                 # Public
        self._salary = salary            # Protected
        self.__password = password       # Private

    def show_password(self):
        # Private attribute accessed inside parent class
        print("Password:", self.__password)


class Developer(Employee):
    def show_details(self):
        # Accessing public attribute
        print("Name:", self.name)

        # Accessing protected attribute
        print("Salary:", self._salary)

        # Private attribute cannot be accessed directly
        # print(self.__password)  # AttributeError


 
dev = Developer("Rahul", 50000, "abc123")

dev.show_details()

# Accessing private attribute through parent class method
dev.show_password()
