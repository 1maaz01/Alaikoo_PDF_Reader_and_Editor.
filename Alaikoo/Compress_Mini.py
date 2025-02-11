from tkinter.filedialog import askopenfilename, asksaveasfilename
from pypdf import PdfWriter

def compress():

    input_pdf_path = askopenfilename(title = "Select a PDF file", filetypes=[("PDF files", "*.pdf")])

    if input_pdf_path:
        writer = PdfWriter(clone_from = input_pdf_path)

        for page in writer.pages:
            page.compress_content_streams()

        with open(asksaveasfilename(title = "Select a PDF file", filetypes=[("PDF files", "*.pdf")]), "wb") as f:
            writer.write(f)
    else:
        print("No file selected.")


