# Day 47 - Clipboard Manager

import pyperclip

class ClipboardManager:

    def copy_text(self, text):

        pyperclip.copy(text)

        print("\nText copied to clipboard!")

    def paste_text(self):

        copied_text = pyperclip.paste()

        print("\nClipboard Content:")
        print(copied_text)


def main():

    manager = ClipboardManager()

    while True:

        print("\n===== CLIPBOARD MANAGER =====")
        print("1. Copy Text")
        print("2. Paste Text")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            text = input("Enter text to copy: ")

            manager.copy_text(text)

        elif choice == "2":

            manager.paste_text()

        elif choice == "3":

            print("Application Closed.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()