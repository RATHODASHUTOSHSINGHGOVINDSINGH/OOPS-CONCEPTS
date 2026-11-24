class Employee:
    def company(self):
        print("Working at ABC Company")


class Developer(Employee):
    def code(self):
        print("Developer writes code")


class Analyst(Employee):
    def analyze(self):
        print("Analyst analyzes data")


dev = Developer()
analyst = Analyst()

dev.company()
dev.code()

analyst.company()
analyst.analyze()