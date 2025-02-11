import pikepdf
from tkinter import filedialog, Tk, messagebox
from customtkinter import *


def lock_pdf(input_pdf, password):
    try:
        old_pdf = pikepdf.Pdf.open(input_pdf)

        locked_pdf = pikepdf.Permissions(extract=False)

        old_pdf.save(filedialog.asksaveasfilename(filetypes=[("PDF Files", "*.pdf")]),
            encryption=pikepdf.Encryption(
                user=password,
                owner="Maaz",
                allow=locked_pdf ))

        messagebox.showinfo("Success", "PDF saved successfully.")

    except FileNotFoundError:
        messagebox.showerror("Error", "File not found error.")

    except pikepdf.PdfError as e:
        pass

    except Exception as e:
        messagebox.showerror("Error", "The PDF is already locked. You cannot lock it again, but you can modify its password.")