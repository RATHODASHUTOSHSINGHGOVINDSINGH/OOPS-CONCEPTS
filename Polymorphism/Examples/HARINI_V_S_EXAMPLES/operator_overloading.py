#operator overloading example
class Product:
    def __init__(self,price):
        self.price = price
    def __add__(self, other): # self->object 1 and other -> object 2
        return self.price + other.price
p1 = Product(500)
p2 = Product(300)
print(p1+p2) # print(p1.__add__(p2))
