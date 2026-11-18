
class Student:
    def __init__(self, name, marks, student_id):
        self.name = name
        self.__marks = marks
        self.__student_id = student_id

    # 1. Getter
    @property
    def marks(self):
        return self.__marks

    # 2. Setter
    @marks.setter
    def marks(self, value):
        if 0 <= value <= 500:
            self.__marks = value
        else:
            print("Invalid marks! Enter between 0 and 500.")

    # 3. Deleter
    @marks.deleter
    def marks(self):
        print("Marks deleted!")
        del self.__marks

    # 4. Read-only property
    @property
    def student_id(self):
        return self.__student_id

    # 5. Computed property
    @property
    def percentage(self):
        return (self.__marks / 500) * 100


 
student = Student("Ashutosh", 400, 101)

# Getter
print("Marks:", student.marks)

# Setter
student.marks = 450
print("Updated Marks:", student.marks)

# Read-only property
print("Student ID:", student.student_id)

# Computed property
print("Percentage:", student.percentage)

# Invalid marks
student.marks = 600

# Deleter (execute at the end)
del student.marks
