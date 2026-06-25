# Day 60 - PDF Merger Tool

from PyPDF2 import PdfMerger
import os

class PDFMergerTool:

    def __init__(self):
        self.merger = PdfMerger()

    def merge_pdfs(self, pdf_files, output_file):

        for pdf in pdf_files:

            if os.path.exists(pdf):
                self.merger.append(pdf)
            else:
                print(f"File not found: {pdf}")

        self.merger.write(output_file)
        self.merger.close()

        print(f"\nMerged PDF saved as '{output_file}'")


def main():

    print("===== PDF MERGER TOOL =====")

    total = int(input("How many PDF files do you want to merge? "))

    pdf_files = []

    for i in range(total):

        pdf = input(f"Enter PDF {i + 1} path: ")

        pdf_files.append(pdf)

    output = input("Output PDF name (example: merged.pdf): ")

    merger = PDFMergerTool()

    try:

        merger.merge_pdfs(pdf_files, output)

    except Exception as e:

        print("Error:", e)


if __name__ == "__main__":
    main()