#Single Inheritance
#Example 1
class Animal:
    def sound(self): #method inside parent class
        print("Every animal makes a sound")

class Dog(Animal):
    #child inherits the properties from its parents
    def bark(self): #Child class method
        print("Dog barks")

#Object creation for Dog(Child) Class
dog = Dog() #object for child class
dog.sound() #call for parent method
dog.bark() #call for child method


#Example 2
class Dog:
    def sound(self):
        print("Woof!!")

class Puppy(Dog):
    def sound(self):
        print("Aif Aif!!")
        super().sound()
        #super() refers to parent(Base class)
        #It calls the method in parent class
    def play(self):
        print("I like playing")

#Object creation for Puppy(Child) class
p1 = Puppy()
p1.sound()
p1.play()


#Example 3
class Dad:
    def __init__(self,Name):
        self.Name = Name

class Son(Dad):
    def __init__(self,Name,sname,Age):
        self.sname = sname
        self.Age = Age
        super().__init__(Name)
        #Dad.__init__(self,Name) #passes name to the parent

    def display(self):
        print("I love my Dad")
        print("My Dad name is ",self.Name)
        print("My name is ",self.sname)
        print("I am ",self.Age," years old")
#Object for Son(child) class
S = Son("Sri Ram","Luv Kush",24)
S.display()
