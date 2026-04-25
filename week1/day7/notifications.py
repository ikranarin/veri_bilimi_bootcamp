class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        return "Email gönderildi"

class SMSNotification(Notification):
    def send(self):
        return "SMS gönderildi"