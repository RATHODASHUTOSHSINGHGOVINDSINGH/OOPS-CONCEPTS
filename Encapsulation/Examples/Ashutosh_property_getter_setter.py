
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    # Getter
    @property
    def balance(self):
        return self.__balance

    # Setter
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Invalid amount")

        self.__balance = amount


acc = BankAccount("Ashutosh", 5000)

# Calling getter
print("Current Balance:", acc.balance)

# Calling setter
acc.balance = 8500
print("Updated Balance:", acc.balance)

# Invalid update
acc.balance = -200
