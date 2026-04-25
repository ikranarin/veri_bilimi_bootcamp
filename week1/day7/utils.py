from models import Expense

def get_user_expenses():
    expenses = []
    while True:
        try:
            val = float(input("Harcama tutarı (Bitirmek için 0): "))
            if val == 0: break
            cat = input("Kategori: ")
            expenses.append(Expense(val, cat))
        except ValueError:
            print("Geçerli bir sayı giriniz!")
    return expenses