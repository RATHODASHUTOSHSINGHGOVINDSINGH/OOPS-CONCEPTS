from abc import ABC,abstractmethod
class employee(ABC):
    def __init__(self,name,role):
        self.name=name
        self.role=role

    @abstractmethod
    def display_details(self):
        pass

    def display_company(self):
        return "XYZ"

class manager(employee):
    def display_details(self):
        print("employee name: ",self.name)
        print("employee role: ",self.role)
        print("company: ",self.display_company())


class developer(employee):
    def display_details(self):
        print("employee name: ",self.name)
        print("employee role: ",self.role)
        print("company: ",self.display_company())


e1=manager("rahul","manager")
e2=developer("ritika","developer")

e1.display_details()
print()

e2.display_details()
