# Day 55 - Text File Word Counter

class WordCounter:

    def count_words(self, file_path):

        try:

            with open(file_path, "r", encoding="utf-8") as file:

                content = file.read()

                words = content.split()

                characters = len(content)

                lines = len(content.splitlines())

                print("\n===== FILE ANALYSIS =====")
                print(f"Words      : {len(words)}")
                print(f"Characters : {characters}")
                print(f"Lines      : {lines}")

        except FileNotFoundError:

            print("File not found.")


def main():

    print("===== WORD COUNTER =====")

    file_path = input("Enter text file path: ")

    counter = WordCounter()

    counter.count_words(file_path)


if __name__ == "__main__":
    main()