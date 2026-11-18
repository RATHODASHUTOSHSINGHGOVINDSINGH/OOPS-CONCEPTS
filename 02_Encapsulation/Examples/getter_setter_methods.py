
class Student:
    def __init__(self, marks):
        self.__marks = marks

    # Getter method
    def get_marks(self):
        return self.__marks

    # Setter method
    def set_marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
            print("Marks updated successfully!")
        else:
            print("Invalid marks! Enter between 0 and 100.")


student = Student(75)

# Getting marks
print("Current Marks:", student.get_marks())

# Updating marks
student.set_marks(90)
print("Updated Marks:", student.get_marks())

# Invalid update
student.set_marks(120)
