# Day 26 - ATM Simulation Project

class ATM:
    def __init__(self, balance=5000):
        self.balance = balance

    def check_balance(self):
        print(f"\nCurrent Balance: ₹{self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully!")


def main():
    atm = ATM()

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            atm.check_balance()

        elif choice == "2":
            amount = float(input("Enter amount to deposit: ₹"))
            atm.deposit(amount)

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: ₹"))
            atm.withdraw(amount)

        elif choice == "4":
            print("Thank you for using ATM.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()