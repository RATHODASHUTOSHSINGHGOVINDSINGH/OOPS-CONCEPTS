#Simple Polymorphism Example
class Dog:
    def sound(self):
        print("Dog Barks")
class Cat:
    def sound(self):
        print("Cat meows")
class Cow:
    def sound(self):
        print("Cow moos")

d = Dog()
c = Cat()
cow = Cow()

d.sound()
c.sound()
cow.sound()
