# Day 24 - Simple Calculator Project

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b


def main():
    calc = Calculator()

    while True:
        print("\n=== SIMPLE CALCULATOR ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "5":
            print("Calculator Closed.")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", calc.add(num1, num2))

        elif choice == "2":
            print("Result:", calc.subtract(num1, num2))

        elif choice == "3":
            print("Result:", calc.multiply(num1, num2))

        elif choice == "4":
            print("Result:", calc.divide(num1, num2))

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()