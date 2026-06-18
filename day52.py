# Day 52 - File Duplicate Finder

import os
import hashlib

class DuplicateFinder:

    def __init__(self):
        self.file_hashes = {}

    def get_file_hash(self, file_path):

        with open(file_path, "rb") as file:

            file_content = file.read()

            return hashlib.md5(file_content).hexdigest()

    def find_duplicates(self, folder_path):

        duplicates = []

        for root, dirs, files in os.walk(folder_path):

            for file in files:

                file_path = os.path.join(root, file)

                try:

                    file_hash = self.get_file_hash(file_path)

                    if file_hash in self.file_hashes:

                        duplicates.append(file_path)

                    else:

                        self.file_hashes[file_hash] = file_path

                except Exception:
                    pass

        return duplicates


def main():

    print("===== FILE DUPLICATE FINDER =====")

    folder = input("Enter folder path: ")

    finder = DuplicateFinder()

    duplicates = finder.find_duplicates(folder)

    if duplicates:

        print("\nDuplicate Files Found:")

        for file in duplicates:
            print(file)

    else:
        print("\nNo duplicate files found.")


if __name__ == "__main__":
    main()