# Day 60A - File Encryption & Decryption Tool

from cryptography.fernet import Fernet


class FileEncryptor:

    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

        with open("secret.key", "wb") as key_file:
            key_file.write(self.key)

    def encrypt_file(self, input_file, output_file):

        with open(input_file, "rb") as file:
            data = file.read()

        encrypted_data = self.cipher.encrypt(data)

        with open(output_file, "wb") as file:
            file.write(encrypted_data)

        print(f"\nEncrypted file saved as '{output_file}'")

    def decrypt_file(self, encrypted_file, output_file):

        with open(encrypted_file, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = self.cipher.decrypt(encrypted_data)

        with open(output_file, "wb") as file:
            file.write(decrypted_data)

        print(f"\nDecrypted file saved as '{output_file}'")


def main():

    encryptor = FileEncryptor()

    while True:

        print("\n===== FILE ENCRYPTION TOOL =====")
        print("1. Encrypt File")
        print("2. Decrypt File")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":

            input_file = input("Enter file path: ")
            output_file = input("Encrypted file name: ")

            encryptor.encrypt_file(input_file, output_file)

        elif choice == "2":

            encrypted_file = input("Encrypted file path: ")
            output_file = input("Output file name: ")

            encryptor.decrypt_file(encrypted_file, output_file)

        elif choice == "3":

            print("Goodbye!")
            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":
    main()