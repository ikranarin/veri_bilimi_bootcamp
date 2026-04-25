# notifications.py
from datetime import datetime

class Notification:
    def __init__(self, message):
        self.message = message
        self.created_at = datetime.now()

    def send(self):
        # Base method: Alt sınıflar bunu ezecek (override)
        pass

    def __str__(self):
        return f"[{self.created_at}] Bildirim: {self.message}"

    def __len__(self):
        # Özel metod: Bildirim mesajının uzunluğunu döndürür
        return len(self.message)

class EmailNotification(Notification):
    def send(self):
        print(f"Email gönderildi: {self.message}")

class SMSNotification(Notification):
    def send(self):
        print(f"SMS gönderildi: {self.message}")

class PushNotification(Notification):
    def send(self):
        print(f"Push bildirimi gönderildi: {self.message}")