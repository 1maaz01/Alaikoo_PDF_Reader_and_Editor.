import fitz  # PyMuPDF
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def remove_watermark(input_pdf, output_pdf):
    doc = fitz.open(input_pdf)

    for page_num in range(len(doc)):
        page = doc[page_num]

        for img in page.get_images(full=True):
            xref = img[0]
            page.delete_image(xref)

        for annot in page.annots() or []:
            if "Watermark" in (annot.info.get("title", "") or ""):
                page.delete_annot(annot)

    doc.save(output_pdf)
    print(f"Watermark removed and saved to: {output_pdf}")



def main():
    root = tk.Tk()
    root.withdraw()

    input_pdf = askopenfilename(title="Select Watermarked PDF", filetypes=[("PDF Files", "*.pdf")])
    if not input_pdf:
        return

    output_pdf = asksaveasfilename(title="Save Cleaned PDF As", defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if not output_pdf:
        return

    remove_watermark(input_pdf, output_pdf)

if __name__ == "__main__":
     main()
