# Day 19 - Contact Book Project

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        print(f"{name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return

        print("\n--- Contact List ---")

        for name, phone in self.contacts.items():
            print(f"Name  : {name}")
            print(f"Phone : {phone}")
            print("-" * 25)

    def search_contact(self, name):
        if name in self.contacts:
            print(f"{name}'s Number: {self.contacts[name]}")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"{name} deleted successfully!")
        else:
            print("Contact not found.")


def main():
    book = ContactBook()

    book.add_contact("Rahul", "9876543210")
    book.add_contact("Anjali", "9123456780")

    book.view_contacts()

    print("\nSearching Contact:")
    book.search_contact("Rahul")

    print("\nDeleting Contact:")
    book.delete_contact("Anjali")

    print("\nUpdated Contact List:")
    book.view_contacts()


if __name__ == "__main__":
    main()