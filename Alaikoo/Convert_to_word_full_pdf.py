import fitz  # PyMuPDF
from tkinter import filedialog, messagebox
from docx import Document


class To_Word:
    def __init__(self):
        self.pdf_document = None

    def open_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            self.pdf_document = fitz.open(file_path)
            messagebox.showinfo("PDF Loaded", f"Successfully loaded {file_path}")

    def convert_pdf_to_word(self):
        if not self.pdf_document:
            messagebox.showerror("Error", "No PDF is currently open.")
            return

        word_file_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Files", "*.docx")])
        if not word_file_path:
            return

        doc = Document()


        for page_num in range(len(self.pdf_document)):
            page = self.pdf_document[page_num]

            page_text = page.get_text()
            if page_text.strip():
                doc.add_paragraph(page_text)
            if page_num < len(self.pdf_document) - 1:
                doc.add_page_break()

        doc.save(word_file_path)
        messagebox.showinfo("Success", f"PDF has been converted to Word and saved at {word_file_path}")
