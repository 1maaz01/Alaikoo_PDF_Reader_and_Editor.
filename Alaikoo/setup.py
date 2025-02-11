import cx_Freeze
import sys
import os

base = None
if sys.platform == "win32":
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\alize\AppData\Local\Programs\Python\Python312\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\alize\AppData\Local\Programs\Python\Python312\tcl\tk8.6"

executables = [cx_Freeze.Executable("29.py", base=base, icon="Icon.ico")]

cx_Freeze.setup(
    name="Alaikoo",
    options={
        "build_exe": {"excludes": ["PyQt5"],
            "packages": [ "tkinter", "os", "sys",  # System & GUI
                "PIL", "fitz", "docx",  # Image & document processing
                "threading", "collections",  # Multi-threading & data structures
                "customtkinter", "webbrowser",  # GUI enhancements & web control
                "PyPDF2", "pdf2image", "pikepdf", "pypdf", "pdfplumber",  # PDF processing
                "pandas"],
            "include_files": ["Icon.ico", "tcl86t.dll", "tk86t.dll","Images","Pdfs"]
        }
    },
    version = "1.0",
    description="Alaikoo PDF Reader and Editor | Developed By Mohammed Maaz Rayeen",
    executables=executables
)
