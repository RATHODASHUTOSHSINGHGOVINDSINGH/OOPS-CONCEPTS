class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.__price = price
        self.__stock = stock

    @property#getting any value
    def price(self):
        return self.__price

    @price.setter # set any value
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Invalid price!")

    def sell_product(self, quantity):
        if 0 < quantity <= self.__stock:
            self.__stock -= quantity
            print("Product sold successfully!")
        else:
            print("Insufficient stock!")

    def display(self):
        print("Product:", self.name)
        print("Price:", self.__price)
        print("Available Stock:", self.__stock)


# Creating object
p = Product("Keyboard", 1000, 10)

# Updating price
p.price = -80

# Selling product
p.sell_product(2)

# Displaying details
p.display()