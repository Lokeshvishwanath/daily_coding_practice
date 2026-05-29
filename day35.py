# Day 34 - Expense Tracker with CSV Export

import csv
from datetime import datetime

class ExpenseTracker:

    def __init__(self):
        self.expenses = []

    def add_expense(self, title, amount):
        self.expenses.append({
            "title": title,
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d")
        })

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return

        total = 0

        print("\n===== EXPENSES =====")

        for expense in self.expenses:
            print(
                f"{expense['date']} | "
                f"{expense['title']} | "
                f"₹{expense['amount']}"
            )

            total += expense["amount"]

        print(f"\nTotal Spent: ₹{total}")

    def export_csv(self):
        with open("expenses.csv", "w", newline="") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=["title", "amount", "date"]
            )

            writer.writeheader()
            writer.writerows(self.expenses)

        print("Expenses exported to expenses.csv")


def main():

    tracker = ExpenseTracker()

    while True:

        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Export CSV")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":

            title = input("Expense Name: ")
            amount = float(input("Amount: ₹"))

            tracker.add_expense(title, amount)

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.export_csv()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()