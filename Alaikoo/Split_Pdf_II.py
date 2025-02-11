from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PyPDF2 import PdfReader, PdfWriter


def split_pdf(input_pdf, split_page, output_pdf1, output_pdf2):
    try:
        # Read the input PDF
        reader = PdfReader(input_pdf)

        if split_page < 1 or split_page > len(reader.pages):
            print(f"Error: Split page must be between 1 and {len(reader.pages)}.")
            return

        writer1 = PdfWriter()
        writer2 = PdfWriter()

        for page in range(split_page):
            writer1.add_page(reader.pages[page])

        for page in range(split_page, len(reader.pages)):
            writer2.add_page(reader.pages[page])

        with open(output_pdf1, "wb") as file1:
            writer1.write(file1)
        with open(output_pdf2, "wb") as file2:
            writer2.write(file2)

    except Exception as e:
        print(f"An error occurred: {e}")


def main(page_no):
    try:

        input_pdf = askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if not input_pdf:
            return

        try:
            split_page = int(page_no)
        except ValueError:
            return

        output_pdf1 = asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if not output_pdf1:
            return


        output_pdf2 = asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if not output_pdf2:
            return

        split_pdf(input_pdf, split_page, output_pdf1, output_pdf2)

    except Exception as e:
        pass


if __name__ == "__main__":
    main(3)
