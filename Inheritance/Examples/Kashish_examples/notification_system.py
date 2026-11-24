class Notification:
    def send(self, message):
        raise NotImplementedError("Subclasses must implement send()")


class EmailNotification(Notification):
    def send(self, message):
        print("Email Notification:", message)


class SMSNotification(Notification):
    def send(self, message):
        print("SMS Notification:", message)


class WhatsAppNotification(Notification):
    def send(self, message):
        print("WhatsApp Notification:", message)


notifications = [
    EmailNotification(),
    SMSNotification(),
    WhatsAppNotification()
]

for notification in notifications:
    notification.send("Your order has been confirmed!")