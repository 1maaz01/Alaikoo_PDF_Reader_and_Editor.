import pdfplumber
import pandas as pd
from tkinter import filedialog, messagebox

def convert_to_xls():
    pdf_path = filedialog.askopenfilename(filetypes =[("PDF Files", "*.pdf")])
    if not pdf_path:
        messagebox.showerror("Error", "No pdf file selected.")
        return

    excel_path = filedialog.asksaveasfilename(filetypes=[("Excel File", "*.xlsx"), ("CSV (Comma delimited) (*.csv)", "*.csv")])

    if not excel_path:
        return

    tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                tables.extend(table)

    df = pd.DataFrame(tables)
    df.to_excel(excel_path, index=False, header=False)



if __name__ == "__main__":
    convert_to_xls()