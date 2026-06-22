# Day 56 - PDF to Text Converter

from PyPDF2 import PdfReader

class PDFToTextConverter:

    def convert_pdf_to_text(self, pdf_file):

        try:

            reader = PdfReader(pdf_file)

            text = ""

            for page in reader.pages:
                text += page.extract_text() + "\n"

            output_file = "output.txt"

            with open(output_file, "w", encoding="utf-8") as file:
                file.write(text)

            print(f"\nText extracted successfully!")
            print(f"Saved as: {output_file}")

        except Exception as e:
            print("Error:", e)


def main():

    print("===== PDF TO TEXT CONVERTER =====")

    pdf_file = input("Enter PDF file path: ")

    converter = PDFToTextConverter()

    converter.convert_pdf_to_text(pdf_file)


if __name__ == "__main__":
    main()