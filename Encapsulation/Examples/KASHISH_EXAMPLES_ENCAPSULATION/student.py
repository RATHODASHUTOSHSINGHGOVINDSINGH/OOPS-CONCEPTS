class Student:
    def __init__(self,marks):
        self.__marks = marks

    def update_marks(self,marks):
        if 0<= marks <= 100:
            self.__marks = marks

    def show_marks(self):
        print("Marks:",self.__marks)

s = Student(89)
s.update_marks(90)
s.show_marks()


        