#Run-time polymorphism
#Example 3
class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):
        print("Car starts with a push button")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start or kick start")

class Electric(Vehicle):
    def start(Self):
        print("Electric vehicle starts with a power system")

v = Vehicle()
c = Car()
b = Bike()
e = Electric()

v.start()
c.start()
b.start()
e.start()
