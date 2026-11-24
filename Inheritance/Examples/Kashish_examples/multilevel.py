class Grandparent:
    def family_name(self):
        print("Family name: Shah")


class Parent(Grandparent):
    def parent_info(self):
        print("This is the parent class")


class Child(Parent):
    def child_info(self):
        print("This is the child class")


obj = Child()
obj.family_name()
obj.parent_info()
obj.child_info()