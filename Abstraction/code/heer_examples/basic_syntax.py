from abc import ABC,abstractmethod
class random(ABC):

    @abstractmethod
    def compose(self):
        pass

    def supply(self):
            print("normal method")

class methods(random):

    def compose(self):
        print("abstract method")


m=methods()
m.compose()
m.supply()