from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self,name,emp_id):
        self.name=name
        self.emp_id=emp_id

    def display_details(self):
        print("employee name: ", self.name)
        print("employee id: ",self.emp_id)

    @abstractmethod
    def calculate_salary(self):
        pass

class Fulltime(Employee):
    def calculate_salary(self):
        return 40000


class Parttime(Employee):
    def calculate_salary(self):
        return 15000


emp1=Fulltime("vishwa",101)
emp2=Parttime("diva",102)

emp1.display_details()
print("employee salary: ",emp1.calculate_salary())

print()

emp2.display_details()
print("employee salary: ",emp2.calculate_salary())