# Day 31 - Password Strength Checker

import re

class PasswordChecker:

    def check_strength(self, password):

        score = 0

        if len(password) >= 8:
            score += 1

        if re.search(r"[A-Z]", password):
            score += 1

        if re.search(r"[a-z]", password):
            score += 1

        if re.search(r"\d", password):
            score += 1

        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            score += 1

        if score == 5:
            return "Very Strong Password 🔥"
        elif score >= 4:
            return "Strong Password ✅"
        elif score >= 3:
            return "Medium Password ⚠️"
        else:
            return "Weak Password ❌"


def main():

    print("===== Password Strength Checker =====")

    password = input("Enter your password: ")

    checker = PasswordChecker()

    result = checker.check_strength(password)

    print("\nResult:", result)


if __name__ == "__main__":
    main()