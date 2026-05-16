# Day 27 - URL Shortener Project

import random
import string

class URLShortener:

    def __init__(self):
        self.url_database = {}

    def generate_short_code(self, length=6):
        characters = string.ascii_letters + string.digits
        short_code = ''.join(random.choice(characters) for _ in range(length))
        return short_code

    def shorten_url(self, original_url):
        short_code = self.generate_short_code()

        self.url_database[short_code] = original_url

        short_url = f"https://short.ly/{short_code}"

        return short_url

    def get_original_url(self, short_code):
        return self.url_database.get(short_code, "URL not found")


def main():
    shortener = URLShortener()

    while True:
        print("\n===== URL SHORTENER =====")
        print("1. Shorten URL")
        print("2. Retrieve Original URL")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            original_url = input("Enter original URL: ")

            short_url = shortener.shorten_url(original_url)

            print(f"Short URL: {short_url}")

        elif choice == "2":
            code = input("Enter short code: ")

            original = shortener.get_original_url(code)

            print(f"Original URL: {original}")

        elif choice == "3":
            print("Application Closed.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()