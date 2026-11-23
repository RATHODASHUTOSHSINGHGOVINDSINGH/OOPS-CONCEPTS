class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("Vehicle is starting...")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start(self):
        print(self.brand, self.model, "is starting...")


car = Car("Toyota", "Fortuner")

car.start()