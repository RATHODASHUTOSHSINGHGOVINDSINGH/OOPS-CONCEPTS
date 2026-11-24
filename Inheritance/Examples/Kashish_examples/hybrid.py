class Person:
    def show(self):
        print("Person details")


class Employee(Person):
    def work(self):
        print("Employee works")


class Student(Person):
    def study(self):
        print("Student studies")


class Intern(Employee, Student):
    pass


obj = Intern()
obj.show()
obj.work()
obj.study()