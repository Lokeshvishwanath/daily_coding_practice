# Day 33 - File Organizer

import os
import shutil

class FileOrganizer:

    def __init__(self, folder_path):
        self.folder_path = folder_path

    def organize_files(self):

        for file in os.listdir(self.folder_path):

            file_path = os.path.join(self.folder_path, file)

            if os.path.isfile(file_path):

                extension = file.split(".")[-1].lower()

                target_folder = os.path.join(
                    self.folder_path,
                    extension.upper() + "_Files"
                )

                os.makedirs(target_folder, exist_ok=True)

                shutil.move(
                    file_path,
                    os.path.join(target_folder, file)
                )

        print("Files organized successfully!")


def main():

    path = input("Enter folder path: ")

    organizer = FileOrganizer(path)

    organizer.organize_files()


if __name__ == "__main__":
    main()