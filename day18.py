# Day 18 - Password Generator Project

import random
import string

class PasswordGenerator:
    def __init__(self, length):
        self.length = length

    def generate_password(self):
        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        password = ""

        for _ in range(self.length):
            password += random.choice(characters)

        return password


def main():
    print("=== Random Password Generator ===")

    length = int(input("Enter password length: "))

    generator = PasswordGenerator(length)

    password = generator.generate_password()

    print("\nGenerated Password:")
    print(password)


if __name__ == "__main__":
    main()