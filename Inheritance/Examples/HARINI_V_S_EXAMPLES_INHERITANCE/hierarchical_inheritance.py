#Hierarchical Inheritance
#Example 1
class Grandpa:
    def respect(self):
        print("He is elder of the family")
class Dad(Grandpa):
    def proud(self):
        print("I am a proud son")
    def respect(self):
        print("He is my dad")
class Aunt(Grandpa):
    def sweet(self):
        print("My aunt is sweet")
    def respect(self):
        print("I am his sweet daughter")
class Uncle(Grandpa):
    def calm(self):
        print("My uncle is a very calm person")
    def respect(self):
        print("I am his cool son")

#creating objects
d1 = Dad() #object for class Dad
a1 = Aunt() #object for class Aunt
u1 = Uncle() #object for class Dad
g = Grandpa() #object for class Dad

# Grandpa class method
g.respect()

#Dad class methods
d1.proud()
d1.respect()

#Aunt class methods
a1.sweet()
a1.respect()

# Uncle class methods
u1.calm()
u1.respect()

#Example 2
class Vehicle:
    def __init__(self,brand):
        self.brand = brand
    def model(self):
        return f"{self.brand} is a great brand"
class Bike(Vehicle):
    def model(self):
        return f"{self.brand} The ultimate driving machine"
class Car(Vehicle):
    def model(self):
        return f"{self.brand} There is no substitute"
print(Vehicle("TATA Motors").model())
print(Bike("BMW").model())
print(Car("Porche").model())