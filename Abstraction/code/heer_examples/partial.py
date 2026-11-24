from abc import ABC,abstractmethod

class vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# class car is stil abstract child class as it has only some methods implemented from vehicle parent class
class car(vehicle):

   
    
    def start(self):
        print("starts the car")


class electriccar(car):

    def stop(self):
        print("stops the car")


    

c=electriccar()
c.stop()
print()
c.start()
    