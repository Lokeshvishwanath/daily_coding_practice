# Day 53 - PDF Password Protector

from PyPDF2 import PdfReader, PdfWriter

class PDFProtector:

    def protect_pdf(self, input_pdf, output_pdf, password):

        reader = PdfReader(input_pdf)

        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        writer.encrypt(password)

        with open(output_pdf, "wb") as file:
            writer.write(file)

        print(f"\nProtected PDF saved as '{output_pdf}'")


def main():

    print("===== PDF PASSWORD PROTECTOR =====")

    input_pdf = input("Enter PDF file path: ")

    output_pdf = input("Enter output PDF name: ")

    password = input("Enter password: ")

    protector = PDFProtector()

    try:

        protector.protect_pdf(
            input_pdf,
            output_pdf,
            password
        )

    except Exception as e:

        print("Error:", e)


if __name__ == "__main__":
    main()