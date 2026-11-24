
class Report:
    def __init__(self, name):
        self.name = name

    def generate(self):
        print("Generating general report")


class SalesReport(Report):
    def generate(self):
        print(f"Generating Sales Report: {self.name}")


class HRReport(Report):
    def generate(self):
        print(f"Generating HR Report: {self.name}")


class FinanceReport(Report):
    def generate(self):
        print(f"Generating Finance Report: {self.name}")


reports = [
    SalesReport("Quarter 4"),
    HRReport("Employee Performance"),
    FinanceReport("Annual Budget")
]

for report in reports:
    report.generate()