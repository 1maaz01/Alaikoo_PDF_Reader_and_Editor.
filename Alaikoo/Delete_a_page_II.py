from tkinter import messagebox

class Delete_Page:
    def __init__(self, document):
        self.pdf_document = document

    def delete_page(self, page_number):
        if not self.pdf_document:
            messagebox.showerror("Error", "No PDF is currently open.")
            return

        # Check if the page number is valid
        if page_number < 0 or page_number >= len(self.pdf_document):
            messagebox.showerror("Error", "Invalid page number.")
            return

        # Delete the specified page (0-indexed)
        self.pdf_document.delete_page(page_number)
        messagebox.showinfo("Success", f"Page {page_number + 1} deleted successfully.")
