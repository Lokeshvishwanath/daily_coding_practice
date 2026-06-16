# Day 50 - Password Manager

import json

class PasswordManager:

    def __init__(self, filename="passwords.json"):
        self.filename = filename

    def save_password(self, website, username, password):

        data = {
            "website": website,
            "username": username,
            "password": password
        }

        try:
            with open(self.filename, "r") as file:
                passwords = json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            passwords = []

        passwords.append(data)

        with open(self.filename, "w") as file:
            json.dump(passwords, file, indent=4)

        print("Password saved successfully!")

    def view_passwords(self):

        try:
            with open(self.filename, "r") as file:
                passwords = json.load(file)

            print("\n===== SAVED PASSWORDS =====")

            for item in passwords:
                print(f"Website : {item['website']}")
                print(f"Username: {item['username']}")
                print(f"Password: {item['password']}")
                print("-" * 30)

        except FileNotFoundError:
            print("No passwords saved yet.")


def main():

    manager = PasswordManager()

    while True:

        print("\n===== PASSWORD MANAGER =====")
        print("1. Save Password")
        print("2. View Passwords")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            website = input("Website: ")
            username = input("Username: ")
            password = input("Password: ")

            manager.save_password(
                website,
                username,
                password
            )

        elif choice == "2":

            manager.view_passwords()

        elif choice == "3":

            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()