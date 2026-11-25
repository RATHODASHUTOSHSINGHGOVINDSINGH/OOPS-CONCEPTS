#Run-time polymorphism
#Example 2 (Payment)
class Payment:
    def pay(self):
        print("Processing payment")

class UPI(Payment):
    def pay(self):
        print("Payment through UPI")
class creditCard(Payment):
    def pay(self):
        print("Payment through Credit card")
class Cash(Payment):
    def pay(Self):
        print("Cash on delivery")

payments = [Payment(), UPI(), creditCard(), Cash()]
for p in payments:
    p.pay()