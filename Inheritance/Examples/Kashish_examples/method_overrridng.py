#polymorphism in python
class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):
        print("Developer is writing code")


class Analyst(Employee):
    def work(self):
        print("Analyst is analyzing data")


team = [Developer(), Analyst(), Employee()]

for person in team:
    person.work()