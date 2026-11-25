#Run-time polymorphism
#Example 1 (Animal)
class Animal:
    def sound(self):
        print("Animals makes sound")

class Dog(Animal):
    def sound(self):
        print("Dogs bark!")
class Cat(Animal):
    def sound(self):
        print("Cat meows!!")

#object creation for all the classes on a whole
animals=[Dog(),Cat(),Animal()] #the execution follows this order
for animal in animals:
    animal.sound()