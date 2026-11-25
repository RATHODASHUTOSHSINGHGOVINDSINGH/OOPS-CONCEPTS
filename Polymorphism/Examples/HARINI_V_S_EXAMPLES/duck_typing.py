#Duck typing example
#Example 1
class Animal:
    def sound(self):
        return "hello"
class Dog(Animal):
    def sound(self):
        return "welcome"
def action(Bark):
    print(Bark.sound())
animal = Animal()
dog = Dog()
action(animal)
action(dog)

#Example 2
class Mobile:
    def play(self):
        print("Mobile is playing music")
class Laptop:
    def play(self):
        print("Laptop is playing music")
class Television:
    def play(self):
        print("Television is playing music")

def music(device): #common function
    device.play()

m = Mobile()
l = Laptop()
t = Television()
music(m)
music(l)
music(t)