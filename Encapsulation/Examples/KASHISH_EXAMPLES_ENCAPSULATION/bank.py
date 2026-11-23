class BankAccount:
    def __init__(self):
        self.__account_holder = "kashish"
        self.__balance = 60000

    @property
    def account_holder(self):
        return self.__account_holder

    @property
    def balance(self):
        return self.__balance

    @account_holder.setter
    def account_holder(self,name):
        self.__account_holder = name

    @balance.setter
    def balance(self,balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Invalid balance", balance, "is not valid")
            raise ValueError("Invalid balance")

b = BankAccount()
print("value before setting")
print("Account Holder:", b.account_holder)
print("Balance:", b.balance)

b.account_holder = "pravi"
b.balance = -70000

print("value after setting")
print("Account Holder:", b.account_holder)
print("Balance:", b.balance)
