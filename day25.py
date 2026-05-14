# Day 25 - Library Management System

class Library:
    def __init__(self):
        self.books = [
            "Python Basics",
            "Data Structures",
            "Machine Learning",
            "Web Development"
        ]

    def display_books(self):
        print("\n=== Available Books ===")

        for index, book in enumerate(self.books, start=1):
            print(f"{index}. {book}")

    def issue_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"Book '{book_name}' issued successfully!")
        else:
            print("Book not available.")

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"Book '{book_name}' returned successfully!")


def main():
    library = Library()

    while True:
        print("\n===== LIBRARY MENU =====")
        print("1. Display Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_books()

        elif choice == "2":
            book = input("Enter book name to issue: ")
            library.issue_book(book)

        elif choice == "3":
            book = input("Enter book name to return: ")
            library.return_book(book)

        elif choice == "4":
            print("Library system closed.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()