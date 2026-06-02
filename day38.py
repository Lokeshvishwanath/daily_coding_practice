# Day 38 - Bulk File Renamer

import os

class FileRenamer:

    def __init__(self, folder_path):
        self.folder_path = folder_path

    def rename_files(self, prefix):

        files = os.listdir(self.folder_path)

        count = 1

        for file in files:

            old_path = os.path.join(self.folder_path, file)

            if os.path.isfile(old_path):

                extension = os.path.splitext(file)[1]

                new_name = f"{prefix}_{count}{extension}"

                new_path = os.path.join(
                    self.folder_path,
                    new_name
                )

                os.rename(old_path, new_path)

                count += 1

        print("Files renamed successfully!")


def main():

    print("===== BULK FILE RENAMER =====")

    folder = input("Enter folder path: ")

    prefix = input("Enter new file prefix: ")

    renamer = FileRenamer(folder)

    try:
        renamer.rename_files(prefix)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()