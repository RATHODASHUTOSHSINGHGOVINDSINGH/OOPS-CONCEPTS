class Employee:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print("Employee Name:", self.name)


class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def show_details(self):
        super().show_details()
        print("Programming Language:", self.language)


dev = Developer("Kashish", "Python")
dev.show_details()