class Inventory:
    def __init__(self, stock):
        self.__stock = stock

    def sell(self, qty):
        if 0 < qty <= self.__stock:
            self.__stock -= qty
            print("Remaining stock:", self.__stock)
        else:
            print("Out of stock")

item = Inventory(50)
item.sell(5)