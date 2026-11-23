#Hybrid Inheritance
#Example 1
'''class Parents:
    def happy(self):
        print("Parents are happy")
class Dad(Parents):
    def proud(self):
        print("Proud dad")
class Aunt(Parents):
    def sweet(self):
        print("sweet aunt")
class Mom(Dad,Parents):
    def loving(self):
        print("My mom is a loving person")

m1 = Mom()
m1.loving()
m1.happy()
m1.proud()

#object for Aunt class
a1 = Aunt()
a1.sweet()

#Example 2
class Grandpa:
    def elder(self):
        print("Grandpa is the oldest member of the family")
class Grandma:
    def caring(self):
        print("Grandma is a caring person")
class Dad(Grandpa):
    def gentleman(self):
        print("My dad is a wise man")
class Son(Dad,Grandma):
    def childish(self):
        print("I like playing football")

    #overridden method of Grandma's class
    def caring(self):
        print("Son is also a caring person")
        
# Object for Son(child) class
m1 = Son()
m1.elder()
m1.caring()
m1.gentleman()
m1.childish()
print(Son.__mro__)
'''
#Example 3
class Vehicle:
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        print(f"{self.brand} started")
    def stop(self):
        print(f"{self.brand} stopped")

class PetrolVehicle(Vehicle):
    def __init__(self,brand,fuel=0):
        super().__init__(brand)
        self.fuel = fuel
    def refuel(self,litres):
        self.fuel += litres #fuel=30 and self.refuel(10) = fuel =40
    def run_on_fuel(self):
        print("Running on fuel")

class ElectricVehicle(Vehicle):
    def __init__(self,brand,battery=0):
        super().__init__(brand)
        self.battery = battery #self.battery = 80 then self.recharge(10) = battery = 90
    def recharge(self,percent):
        self.battery += percent
    def run_on_battery(self):
        print("Running on battery")

class HybridCar(PetrolVehicle,ElectricVehicle):
    def __init__(self,brand,fuel=0,battery=0):
        PetrolVehicle.__init__(self,brand,fuel)
        self.battery=battery
    def switch_drive_mode(self,mode):
        self.mode = mode
        if mode == "petrol":
            self.run_on_fuel()
        else:
            self.run_on_battery()

car = HybridCar("BMW",20,80)
car.start()
car.switch_drive_mode("battery")
print(HybridCar.__mro__)