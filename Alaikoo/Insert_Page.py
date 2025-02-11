import fitz
from tkinter.filedialog import askopenfilename


def insert_blank(page_no, input_pdf):
    if not input_pdf:
        return

    input_pdf.insert_page(page_no)
    return input_pdf


def insert_image_page(page_no, input_pdf):
    if not input_pdf:
        return

    image_path = askopenfilename(title="Select the Image File", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

    img_doc = fitz.open(image_path)
    img_rect = img_doc[0].rect
    page_number = page_no

    input_pdf.insert_page(page_number, width=img_rect.width, height=img_rect.height)

    page = input_pdf[page_number]
    page.insert_image(img_rect, filename = image_path)

    return input_pdf