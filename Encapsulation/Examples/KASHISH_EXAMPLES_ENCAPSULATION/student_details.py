class student:
    def __init__(self):
        self.__name = "kashish"
        self.__rollno = 101
        self.__marks = 90

    @property
    def name(self):
        return self.__name

    @property
    def rollno(self):
        return self.__rollno

    @property
    def marks(self):
        return self.__marks

    @name.setter
    def name(self, name):
        self.__name = name

    @rollno.setter
    def rollno(self, rollno):
        self.__rollno = rollno

    @marks.setter
    def marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
             print("Invalid marks", marks, "is not in range 0-100")

s = student()
print("value before setting")
print(s.name)
print(s.rollno)
print(s.marks)

#set value
s.name = "abc"
s.rollno = 102
s.marks = -95
print("value after setting")
print(s.name)  
print(s.rollno)
print(s.marks)
