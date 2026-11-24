class Employee:
    def __init__(self,name,employee_id,department):
        self.__name = name
        self.__employee_id = employee_id
        self.__department = department

    def display_details(self):
        print("Employee Name:", self.__name)
        print("Employee ID:", self.__employee_id)
        print("Department:", self.__department) 


class Developer(Employee):
    def write_code(self):
        print(f"{self._Employee__name} is writing code.")

class DataAnalyst(Employee):
    def analyze_data(self):
        print(f"{self._Employee__name} is analyzing data.")

class HRManager(Employee):
    def manage_hr(self):
        print(f"{self._Employee__name} is managing HR tasks.")

analyst = DataAnalyst("Kashish", 101, "Analytics")

analyst.display_details()
analyst.analyze_data()

e = Employee("John", 102, "HR")
e.display_details()



