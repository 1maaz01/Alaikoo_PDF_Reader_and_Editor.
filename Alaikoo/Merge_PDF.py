from tkinter import filedialog, messagebox
import PyPDF2


def merge_pdfs():
    selected_files = []

    while True:
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")],
                                               title="Select a PDF file (Cancel to finish)")
        if not file_path:
            break
        selected_files.append(file_path)

    if not selected_files:
        messagebox.showerror("Error", "No PDFs selected for merging.")
        return

    pdf_merger = PyPDF2.PdfMerger()

    for file_path in selected_files:
        pdf_merger.append(file_path)

    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if save_path:
        pdf_merger.write(save_path)
        pdf_merger.close()
        messagebox.showinfo("Success", f"PDFs merged successfully and saved to {save_path}")

