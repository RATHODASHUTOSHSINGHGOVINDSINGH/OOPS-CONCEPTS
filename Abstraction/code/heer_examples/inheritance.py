from abc import ABC,abstractmethod

class vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class car(vehicle):

    @abstractmethod
    def charge(self):
        pass
    def start(self):
        print("starts the car")


class electriccar(car):

    def charge(self):
        print("electric car")


    def start(self):
        print("starts electric car")


c=electriccar()
c.charge()
print()
c.start()
    