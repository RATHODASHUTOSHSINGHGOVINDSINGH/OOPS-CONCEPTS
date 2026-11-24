class Employee:
    def work(self):
        print("Employee is working.")

class Developer(Employee):
    pass

dev = Developer()
dev.work()  # Output: Employee is working.
