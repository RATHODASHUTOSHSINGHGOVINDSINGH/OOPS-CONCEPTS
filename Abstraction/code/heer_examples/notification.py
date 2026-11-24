from abc import ABC,abstractmethod
class Notification(ABC):
    def __init__(self,receiver):
        self.receiver=receiver

    @abstractmethod
    def send(self,message):
        pass

class EmailNotification(Notification):
    def send(self,message):
        print()
        print("sending email to: ",self.receiver)
        print("message: ",message)
        print()

class SMSNotification(Notification):
    def send(self,message):
        print()
        print("sending sms to: ",self.receiver)
        print("message: ",message)
        print()


notify=[EmailNotification("heer@123.gmail.com"),SMSNotification("1234567890")]

for notification in notify:
    notification.send("your order has been placed successfully")