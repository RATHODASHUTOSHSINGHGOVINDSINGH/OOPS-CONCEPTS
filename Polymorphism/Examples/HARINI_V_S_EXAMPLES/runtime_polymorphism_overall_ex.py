#Runtime polymorphism
#overall example with parameters
#Inheritance+method overriding and dynamic polymorphism'

class Payment:

    def __init__(self,amount):
        self.amount = amount
    def pay(self):
        print("Payment processing...")

class UPI(Payment):
    def __init__(self,amount,upi_id):
        super().__init__(amount)
        self.upi_id = upi_id
    def pay(self):
        print("UPI payment successfull")
        print("UPI ID:", self.upi_id)
        print("Amount:", self.amount)
    def details(self):
        print("Payment mode: UPI")

class CreditCard(Payment):
    def __init__(self,amount,card_num):
        super().__init__(amount)
        self.card_num = card_num
    def pay(self):
        print("Credit card payment successfull")
        print("Card number:", self.card_num)
        print("Amount:", self.amount)
    def check(self):
        print("Credit card verification completed")

class Cash(Payment):
    def __init__(self,amount, customer_name):
        super().__init__(amount)
        self.customer_name = customer_name
    def pay(self):
        print("Cash on delivery successfull")
        print("Customer:",self.customer_name)
        print("Amount:",self.amount)
    def receipt(self):
        print("Cash receipt generated")

#creating objects
payments = [UPI(1500,"harini@upi"),
            CreditCard(2500,"XXXX-XXXX-1234"),
            Cash(1200,"Harini")]
#dynamic polymorphism
#takes place by printing all the implementation of the method pay()
for p in payments:
    p.pay()
    print("----------------------")