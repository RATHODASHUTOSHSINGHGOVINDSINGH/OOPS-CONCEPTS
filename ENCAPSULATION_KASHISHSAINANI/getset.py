class Product:
    def __init__(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Invalid price")
        self.__price = value

p = Product(79)
p.set_price(89)
print(p.get_price())