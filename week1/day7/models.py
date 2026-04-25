from datetime import datetime

class Expense:
    def __init__(self, amount, category, date=None):
        self.amount = amount
        self.category = category
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def __str__(self):
        return f"{self.date} - {self.category}: {self.amount}TL"

class Budget:
    def __init__(self, limit):
        self.limit = limit
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def total_expense(self):
        return sum(exp.amount for exp in self.expenses)

    def average_expense(self):
        return self.total_expense() / len(self.expenses) if self.expenses else 0

    def is_limit_exceeded(self):
        return self.total_expense() > self.limit