# Day 17 - Expense Tracker Project

import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount):
        expense = {
            "category": category,
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.expenses.append(expense)

    def show_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return

        print("\nExpense History")
        print("-" * 30)

        total = 0

        for expense in self.expenses:
            print(f"Category : {expense['category']}")
            print(f"Amount   : ₹{expense['amount']}")
            print(f"Date     : {expense['date']}")
            print("-" * 30)

            total += expense["amount"]

        print(f"Total Expense: ₹{total}")

    def save_expenses(self):
        with open("expenses.json", "w") as file:
            json.dump(self.expenses, file, indent=4)

        print("Expenses saved successfully!")


def main():
    tracker = ExpenseTracker()

    tracker.add_expense("Food", 250)
    tracker.add_expense("Travel", 120)
    tracker.add_expense("Shopping", 999)

    tracker.show_expenses()

    tracker.save_expenses()


if __name__ == "__main__":
    main()