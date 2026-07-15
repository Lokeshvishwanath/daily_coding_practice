import os


class FolderAnalyzer:

    def get_folder_size(self, folder_path):

        total_size = 0

        for root, dirs, files in os.walk(folder_path):

            for file in files:

                file_path = os.path.join(root, file)

                try:
                    total_size += os.path.getsize(file_path)
                except Exception:
                    pass

        return total_size

    def convert_size(self, size):

        units = ["B", "KB", "MB", "GB", "TB"]

        index = 0

        while size >= 1024 and index < len(units) - 1:

            size /= 1024
            index += 1

        return f"{size:.2f} {units[index]}"


def main():

    print("===== FOLDER SIZE ANALYZER =====")

    folder = input("Enter folder path: ")

    analyzer = FolderAnalyzer()

    try:

        size = analyzer.get_folder_size(folder)

        print("\nFolder Size:")
        print(analyzer.convert_size(size))

    except Exception as e:

        print("Error:", e)


if __name__ == "__main__":
    main()