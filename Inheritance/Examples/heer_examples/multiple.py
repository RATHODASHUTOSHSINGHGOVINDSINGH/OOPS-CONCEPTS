class Programming:
    def skills(self):
        print("Programming: Python, Java")


class Database:
    def skills(self):
        print("Database: SQL, MongoDB")


class Developer(Programming, Database):
    def skills(self):
        print("Developer Skills:")
        super().skills()


dev = Developer()
dev.skills()

print(Developer.mro())