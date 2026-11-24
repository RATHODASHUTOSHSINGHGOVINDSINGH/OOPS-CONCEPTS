#Inheritance: A Vehicle is a base class, and Car is a derived class
class Engine:
    def start(self):
        print("Engine started")

#Composition: A Car has an Engine
class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print("Car is ready to drive")


my_car = Car()
my_car.start_car()