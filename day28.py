# Day 28 - Expense Splitter App

class ExpenseSplitter:

    def __init__(self):
        self.members = []
        self.total_expense = 0

    def add_members(self):
        count = int(input("Enter number of members: "))

        for i in range(count):
            name = input(f"Enter member {i + 1} name: ")
            self.members.append(name)

    def add_expense(self):
        amount = float(input("Enter total expense amount: ₹"))
        self.total_expense += amount

    def split_expense(self):
        if len(self.members) == 0:
            print("No members added.")
            return

        split_amount = self.total_expense / len(self.members)

        print("\n===== Expense Split =====")

        for member in self.members:
            print(f"{member} should pay ₹{split_amount:.2f}")


def main():
    app = ExpenseSplitter()

    app.add_members()
    app.add_expense()
    app.split_expense()


if __name__ == "__main__":
    main()