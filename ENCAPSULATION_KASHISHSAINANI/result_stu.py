
class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    @property
    def name(self):
        return self.__name

    @property
    def marks(self):
        return self.__marks

    @name.setter
    def name(self, name):
        self.__name = name

    @marks.setter
    def marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            raise ValueError(f"Invalid marks: {marks}")

    def show(self):
        if self.__marks >= 35:
            print(f"PASS: {self.__marks}")
        else:
            print(f"FAIL: {self.__marks}")


s = Student("kashish", 33)

print(f"Value before setting: {s.name}, {s.marks}")

s.name = "Kashish"
s.marks = 29

print(f"Value after setting: {s.name}, {s.marks}")

s.show()
