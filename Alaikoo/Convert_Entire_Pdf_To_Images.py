import fitz
from PIL import Image
from tkinter import filedialog, messagebox
import os


class To_Image:
    def __init__(self):
        self.pdf_document = None

    def open_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            self.pdf_document = fitz.open(file_path)
            messagebox.showinfo("PDF Loaded", f"Successfully loaded {file_path}")


    def save_all_pages_as_images(self):
        if not self.pdf_document:
            messagebox.showerror("Error", "No PDF is currently open.")
            return

        folder_path = filedialog.askdirectory(title="Select Folder to Save Images")
        if not folder_path:
            return

        for page_num in range(len(self.pdf_document)):
            page = self.pdf_document[page_num]
            mat = fitz.Matrix(2, 2)
            pix = page.get_pixmap(matrix=mat)

            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            save_path = os.path.join(folder_path, f"page_{page_num + 1}.png")

            img.save(save_path)
            print(f"Saved: {save_path}")

        messagebox.showinfo("Success", f"All pages have been saved as images in {folder_path}")


