class Product:
    def __init__(self, stock):
        self.__stock = stock

    def sell(self, quantity):
        if quantity <= 0 or quantity > self.__stock:
            raise ValueError("Invalid quantity")
        self.__stock -= quantity