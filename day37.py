# Day 37 - PDF Merger Tool

from PyPDF2 import PdfMerger

class PDFMergerTool:

    def __init__(self):
        self.merger = PdfMerger()

    def merge_pdfs(self, pdf_files, output_file):

        for pdf in pdf_files:
            self.merger.append(pdf)

        self.merger.write(output_file)
        self.merger.close()

        print(f"Merged PDF saved as '{output_file}'")


def main():

    print("===== PDF MERGER TOOL =====")

    num_files = int(input("How many PDFs do you want to merge? "))

    pdf_files = []

    for i in range(num_files):
        file_name = input(f"Enter PDF {i + 1} path: ")
        pdf_files.append(file_name)

    output_file = input("Enter output file name: ")

    merger = PDFMergerTool()

    try:
        merger.merge_pdfs(pdf_files, output_file)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()