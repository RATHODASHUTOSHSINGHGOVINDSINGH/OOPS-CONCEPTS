from abc import ABC,abstractmethod
class employee(ABC):
    @abstractmethod
    def work(Self):
        pass


emp=employee()

# it gives type error while creating object of abstract class as python doesn't allow instantiate it 
