
class Employee:
   def __init__(self, name, salary, pin):
        self.name = name
        self._salary = salary
        self.__pin = pin


emp = Employee("Aarav", 75000, 4321)

# Accessing public attribute
print(emp.name)

# Accessing protected attribute
print(emp._salary)

# Inspecting object's internal dictionary
print(emp.__dict__)

# Direct access to private attribute
# print(emp.__pin)  # AttributeError

# Accessing private attribute using name mangling
print(emp._Employee__pin)
