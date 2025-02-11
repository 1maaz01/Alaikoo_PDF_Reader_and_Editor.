import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import fitz
from docx import Document
from threading import Timer
from customtkinter import *
import Merge_PDF, Convert_to_word_full_pdf, Split_Pdf_II, Compress_Mini, Remove_WaterMark
import Protect_Pdf, Convert_Entire_Pdf_To_Images, Delete_a_page_II, Insert_Page, Convert_Pdf_to_excel
from collections import deque
from PyPDF2 import PdfReader, PdfWriter
from pdf2image import convert_from_path
import webbrowser
import pikepdf



class PDFReader:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Reader")
        self.root.wm_iconbitmap("Icon.ico")

########################       Images       ############################

        delete = Image.open("Images\\Delete.png")
        delete = CTkImage(light_image=delete, size=(50, 50))

        help_desk = Image.open("Images\\Help_Desk.png")
        help_desk= CTkImage(light_image = help_desk, size=(50, 50))

        add_page = Image.open("Images\\add_page.png")
        add_page = CTkImage(light_image=add_page, size=(50, 50))

        rotate_clo = Image.open("Images\\5.png")
        rotate_clo = CTkImage(light_image=rotate_clo, size=(50, 50))

        rotate_anti = Image.open("Images\\6.png")
        rotate_anti = CTkImage(light_image=rotate_anti, size=(50, 50))

        reorder = Image.open("Images\\reorder.png")
        reorder = CTkImage(light_image=reorder, size=(50, 50))

        insert_blank_page = Image.open("Images\\insert_blank_page.png")
        insert_blank_page = CTkImage(light_image=insert_blank_page, size=(50, 50))

        swap_page_photo = Image.open("Images\\Swap_pages.png")
        swap_page_photo = CTkImage(light_image=swap_page_photo, size=(50, 50))

        to_docx = Image.open("Images\\To_docx.png")
        to_docx = CTkImage(light_image=to_docx, size=(50, 50))

        close = Image.open("Images\\Cross.png")
        close = CTkImage(close)

        to_png = Image.open("Images\\To_png.png")
        to_png = CTkImage(light_image=to_png, size=(50, 50))

        to_excel = Image.open("Images\\To_excel.png")
        to_excel = CTkImage(light_image=to_excel, size=(50, 50))

        edit = Image.open("Images\\edit.png")
        edit = CTkImage(light_image=edit, size=(50, 50))

        compress = Image.open("Images\\compress.png")
        compress = CTkImage(light_image=compress, size=(50, 50))

        merge = Image.open("Images\\merge.png")
        merge = CTkImage(light_image=merge, size=(50, 50))

        lock = Image.open("Images\\lock.png")
        lock = CTkImage(light_image=lock, size=(50, 50))

        modify = Image.open("Images\\modify.png")
        modify = CTkImage(light_image=modify, size=(50, 50))

        new = Image.open("Images\\new.png")
        new = CTkImage(light_image=new, size=(50, 50))

        split = Image.open("Images\\split.png")
        split = CTkImage(light_image=split, size=(50, 50))

        add_water = Image.open("Images\\add_watermark.png")
        add_water = CTkImage(light_image=add_water, size=(50, 50))

        remove_water = Image.open("Images\\remove_water.png")
        remove_water = CTkImage(light_image=remove_water, size=(50, 50))

        next = Image.open("Images\\1.png")
        next = CTkImage(next)

        prev = Image.open("Images\\2.png")
        prev = CTkImage(prev)

        zoom_in = Image.open("Images\\3.png")
        zoom_in = CTkImage(zoom_in)

        zoom_out = Image.open("Images\\4.png")
        zoom_out = CTkImage(zoom_out)

        rotate_clock = Image.open("Images\\5.png")
        rotate_clock = CTkImage(rotate_clock)

        rotate_anti = Image.open("Images\\6.png")
        rotate_anti = CTkImage(rotate_anti)

        self.show_image = CTkImage(Image.open("Images\\show.png"), size=(20, 20))
        self.hide_image = CTkImage(Image.open("Images\\hide.png"), size=(20, 20))




        self.file_path = None
        self.pdf_document = None
        self.current_page = 0
        self.zoom_level = 1.0
        self.page_rotations = deque()

        self.resize_timer = None
        self.resize_delay = 0.2


        self.top_frame = CTkFrame(self.root, height=50, fg_color="#212121")
        self.top_frame.pack(side="top", fill="x")


###########################################      All Tools Frame       #################################################
        self.all_tools_button = CTkButton(self.top_frame, text="All Tools", fg_color="#212121", hover_color="#212121",
                                          width=10, command=self.show_all_tools)
        self.all_tools_button.pack(side="left", padx=5)

        self.edit_button = CTkButton(self.top_frame, text="Edit", fg_color="#212121", hover_color="#212121", width=10,
                                     command=self.show_edit_frame)
        self.edit_button.pack(side="left", padx=5)

        self.convert_button = CTkButton(self.top_frame, text="Convert", fg_color="#212121", hover_color="#212121",
                                        width=10, command=self.show_convert_frame)
        self.convert_button.pack(side="left", padx=5)

        self.support_button = CTkButton(self.top_frame, text="Support", fg_color="#212121", hover_color="#212121",
                                        width=10, command=self.show_support_frame)
        self.support_button.pack(side="left", padx=5)


        self.canvas = tk.Canvas(self.root, bg="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)  ###


        self.all_tools_frame = CTkFrame(self.canvas, fg_color = "#2D2D2D")

        self.all_close_frame = CTkFrame(self.all_tools_frame, fg_color="#2D2D2D")
        self.all_close_frame.pack(anchor="nw", pady=5)


        self.all_tool_label = CTkLabel(self.all_close_frame, text="    All Tools", fg_color="#2D2D2D",
                                       font=("Aerial", 20, "bold"), text_color = "white",
                                       width=10)
        self.all_tool_label.pack(side="left", padx=25)



        self.close = CTkButton(self.all_close_frame, text=" ", fg_color="#2D2D2D", hover_color="#212121",
                               width=10, command=self.hide_all_tools, image=close)
        self.close.pack(side="right")

        self.edit_pdf = CTkButton(self.all_tools_frame, image=edit, compound="right", command=self.show_edit_frame,
                                  text="Edit PDF", fg_color="#2D2D2D", hover_color="#212121",
                                  font=("Aerial", 15, "bold"), anchor = "w")
        self.edit_pdf.pack(anchor="nw", pady=5, fill="x")


        self.create = CTkButton(self.all_tools_frame, text="Create a PDF", compound="right", image=new,
                                fg_color="#2D2D2D", font=("Aerial", 15, "bold"), anchor = "w",
                                hover_color="#212121", width=10, command=self.create_pdf)
        self.create.pack(anchor="nw", pady=5, fill="x")


        self.merge_pdf = CTkButton(self.all_tools_frame, text="Merge PDF", compound="right", image=merge,
                                   fg_color="#2D2D2D", hover_color="#212121", font=("Aerial", 15, "bold"),
                                   width=10, command=Merge_PDF.merge_pdfs, anchor = "w")
        self.merge_pdf.pack(anchor="nw", pady=5, fill="x")


        self.split_pdf = CTkButton(self.all_tools_frame, text="Split PDF", compound="right", image=split,
                                   fg_color="#2D2D2D", hover_color="#212121", font=("Aerial", 15, "bold"),
                                   width=10, command=self.split, anchor = "w")
        self.split_pdf.pack(anchor="nw", pady=5, fill="x")


        self.compress_pdf = CTkButton(self.all_tools_frame, text="Compress PDF", compound="right", image=compress,
                                      fg_color="#2D2D2D", font=("Aerial", 15, "bold"),
                                      hover_color="#212121", width=10, command=self.compress_pdf, anchor = "w")
        self.compress_pdf.pack(anchor="nw", pady=5, fill="x")

        self.lock_pdf = CTkButton(self.all_tools_frame, text="Lock PDF", compound="right", image=lock, fg_color="#2D2D2D",
                                  font=("Aerial", 15, "bold"),
                                  hover_color="#212121", width=10, command=self.lock_pdf_func, anchor = "w")
        self.lock_pdf.pack(anchor="nw", pady=5, fill="x")

        self.modify_password_of_pdf = CTkButton(self.all_tools_frame, compound="right", image=modify,
                                                text="Modify Password", fg_color="#2D2D2D", font=("Aerial", 15, "bold"),
                                                hover_color="#212121", width=10, command=self.modify_password_func, anchor = "w")
        self.modify_password_of_pdf.pack(anchor="nw", pady=5, fill="x")





#########################################################      Edit tools frame     ###############################

        self.edit_tools_frame = CTkFrame(self.canvas, fg_color = "#2D2D2D")
        self.edit_close_frame = CTkFrame(self.edit_tools_frame, fg_color="#2D2D2D")
        self.edit_close_frame.pack(anchor="nw", pady=5)

        self.edit_tool_label = CTkLabel(self.edit_close_frame, text="       Edit     ", fg_color="#2D2D2D",
                                        font=("Aerial", 20, "bold"), text_color = "white",
                                        width=10)
        self.edit_tool_label.pack(side="left", padx=25)


        self.close = CTkButton(self.edit_close_frame, text=" ", fg_color="#2D2D2D", hover_color="#212121", anchor="e",
                               width=10, command=self.hide_edit_frame, image=close)
        self.close.pack(side="right")

        self.delete_page_button = CTkButton(self.edit_tools_frame, command=self.delete_currrent_page, compound="right",
                                            image=delete, text="Delete Current Page", fg_color="#2D2D2D",
                                            hover_color="#212121", font=("Aerial", 15, "bold"), anchor = "w")
        self.delete_page_button.pack(anchor="nw", pady=5, fill="x")


        self.insert_blank_page_button = CTkButton(self.edit_tools_frame, image=insert_blank_page,
                                                  text="Insert Blank Page", fg_color="#2D2D2D",
                                                  font=("Aerial", 15, "bold"), compound="right", anchor = "w",
                                                  hover_color="#212121", width=10, command=self.request_blank_page_no)
        self.insert_blank_page_button.pack(anchor="nw", pady=5, fill="x")


        self.insert_page_button = CTkButton(self.edit_tools_frame, compound="right", anchor = "w", image=add_page, text="Insert Page",
                                            fg_color="#2D2D2D", font=("Aerial", 15, "bold"),
                                            hover_color="#212121", width=10, command=self.request_image_page)
        self.insert_page_button.pack(anchor="nw", pady=5, fill="x")


        self.reorder_pages = CTkButton(self.edit_tools_frame, image=reorder, compound="right", anchor = "w", text="Reorder Pages",
                                       fg_color="#2D2D2D", font=("Aerial", 15, "bold"),
                                       hover_color="#212121", width=10, command=self.request_order)
        self.reorder_pages.pack(anchor="nw", pady=5, fill="x")

        self.swap_button = CTkButton(self.edit_tools_frame, image=swap_page_photo, compound="right", anchor = "w", text="Swap Pages",
                                     fg_color="#2D2D2D", font=("Aerial", 15, "bold"),
                                     hover_color="#212121", width=10, command=self.swap)
        self.swap_button.pack(anchor="nw", pady=5, fill="x")


        self.insert_watermark_button = CTkButton(self.edit_tools_frame, image=add_water, text="Insert Watermark", compound="right", fg_color="#2D2D2D", hover_color="#212121",
                                                 font=("Aerial", 15, "bold"), command = self.add_watermark_I, width=10, anchor = "w")
        self.insert_watermark_button.pack(anchor="nw", pady=5, fill="x")


        self.remove_watermark_button = CTkButton(self.edit_tools_frame, image=remove_water, text="Remove Watermark",  compound="right",
                                                 fg_color="#2D2D2D", font=("Aerial", 15, "bold"), hover_color="#212121", width=10,
                                                 command=self.remove_watermark, anchor = "w")
        self.remove_watermark_button.pack(anchor="nw", pady=5, fill="x")


        self.rotate_right = CTkButton(self.edit_tools_frame, text="Rotate Right", image=rotate_clo, compound="right", anchor = "w",
                                      fg_color="#2D2D2D", font=("Aerial", 15, "bold"),
                                      hover_color="#212121", width=10, command=self.rotate_clockwise)
        self.rotate_right.pack(anchor="nw", pady=5, fill="x")

        self.rotate_left = CTkButton(self.edit_tools_frame, text="Rotate Left", image=rotate_anti, compound="right", anchor = "w",
                                     fg_color="#2D2D2D", font=("Aerial", 15, "bold"),
                                     hover_color="#212121", width=10, command=self.rotate_counterclockwise)
        self.rotate_left.pack(anchor="nw", pady=5, fill="x")




######################################################      Convert Frame      ###################################################

        self.convert_frame = CTkFrame(self.canvas, fg_color = "#2D2D2D")
        self.convert_close_frame = CTkFrame(self.convert_frame, fg_color="#2D2D2D")
        self.convert_close_frame.pack(anchor="nw", pady=5)

        self.convert_label = CTkLabel(self.convert_close_frame, text="  Convert  ", fg_color="#2D2D2D",
                                      font=("Aerial", 20, "bold"), text_color = "white",
                                      width=10)
        self.convert_label.pack(side="left", padx=25)


        self.close = CTkButton(self.convert_close_frame, anchor="e", text=" ", fg_color="#2D2D2D",
                               hover_color="#212121", command=self.hide_convert_frame,
                               width=10, image=close)
        self.close.pack(side="right")

        self.convert_word = CTkButton(self.convert_frame, image=to_docx, command=self.convert_word_func,
                                      text="To Word", fg_color="#2D2D2D", hover_color="#212121", compound="right", anchor = "w",
                                      font=("Aerial", 15, "bold"))
        self.convert_word.pack(anchor="nw", pady=5, fill="x")

        self.convert_images = CTkButton(self.convert_frame, text="To Image", command=self.convert_to_images,
                                        image=to_png, fg_color="#2D2D2D", font=("Aerial", 15, "bold"),
                                        hover_color="#212121", width=10, compound="right", anchor = "w",)
        self.convert_images.pack(anchor="nw", pady=5, fill="x")

        self.convert_excel = CTkButton(self.convert_frame, text="To Excel", command=self.convert_to_excel,
                                       image=to_excel, compound="right", anchor = "w", fg_color="#2D2D2D", font=("Aerial", 15, "bold"),
                                       hover_color="#212121", width=10, text_color = "white")
        self.convert_excel.pack(anchor="nw", pady=5, fill="x")

        self.h_scrollbar = tk.Scrollbar(self.canvas, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.v_scrollbar = tk.Scrollbar(self.canvas, orient=tk.VERTICAL, command=self.canvas.yview)
        self.v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.config(xscrollcommand=self.h_scrollbar.set, yscrollcommand=self.v_scrollbar.set)




######################################       Button Frame       ####################################
        self.button_frame = tk.Frame(self.canvas, background="#212121")
        self.button_frame.pack(side=RIGHT, fill=tk.Y)

        next_button = CTkButton(self.button_frame, command=self.next_page, image=next, text="", width=10,
                                fg_color="#212121", hover_color="#212121")  # , image = self.next)
        next_button.pack(side="bottom", pady=10)


        self.total_pages = CTkLabel(self.button_frame, text="0", font=("Aerial", 20, "bold"), width=10, text_color = "white")
        self.total_pages.pack(side="bottom", pady=10)

        CTkLabel(self.button_frame, text="of", font=("Aerial", 20, "bold"), width=10, text_color = "white").pack(side="bottom", pady=10)

        self.page_label = CTkLabel(self.button_frame, text="0", font=("Aerial", 20, "bold"), width=10, text_color = "white")
        self.page_label.pack(side="bottom", pady=10)

        prev_button = CTkButton(self.button_frame, text="", command=self.previous_page, image=prev, width=10,
                                fg_color="#212121", hover_color="#212121")
        prev_button.pack(side="bottom", pady=10)

        zoom_in_button = CTkButton(self.button_frame, text="", command=self.zoom_in, image=zoom_in, width=10,
                                   fg_color="#212121", hover_color="#212121")
        zoom_in_button.pack(side="bottom", pady=10)

        zoom_out_button = CTkButton(self.button_frame, text="", command=self.zoom_out, image=zoom_out, width=10,
                                    fg_color="#212121", hover_color="#212121")
        zoom_out_button.pack(side="bottom", pady=10)

        rotate_cw_button = CTkButton(self.button_frame, text="", command=self.rotate_clockwise, width=10,
                                     image=rotate_clock, fg_color="#212121", hover_color="#212121")
        rotate_cw_button.pack(side="bottom", pady=10)

        rotate_ccw_button = CTkButton(self.button_frame, text="", command=self.rotate_counterclockwise, width=10,
                                      image=rotate_anti, fg_color="#212121", hover_color="#212121")
        rotate_ccw_button.pack(side="bottom", pady=10)




#########################        Support Frame         ###################################################
        self.support_frame = CTkFrame(self.canvas, fg_color="#2D2D2D")
        self.support_close_frame = CTkFrame(self.support_frame, fg_color="#2D2D2D")
        self.support_close_frame.pack(anchor="nw", pady=5)

        self.support_label = CTkLabel(self.support_close_frame, text="  Support  ", fg_color="#2D2D2D",
                                      font=("Aerial", 20, "bold"), width=10, text_color = "white")
        self.support_label.pack(side="left")

        self.close = CTkButton(self.support_close_frame, text=" ", fg_color="#2D2D2D",
                               hover_color="#212121", command=self.hide_support_frame,
                               width=10, image=close)
        self.close.pack(side="right")

        contact_button = CTkButton(self.support_frame, text="Contact", command=self.support, font=("Aerial", 15, "bold"),
                                      image = help_desk, fg_color="#2D2D2D", anchor = "w", hover_color="#212121", compound = RIGHT)
        contact_button.pack(anchor="nw", pady=5, fill="x")

        self.root.bind("<Configure>", self.on_window_resize)





###################################################      Menu Bar       #############################################
        menu_bar = tk.Menu(root)

        file_menu = tk.Menu(menu_bar, tearoff=0, bg="#333", fg="#fff",
                            font=("Arial", 18))  # Dark background and white text
        file_menu.add_command(label="Open PDF", background="#444", foreground="#fff",
                              activebackground="#666", activeforeground="#fff", command=self.open_pdf)
        file_menu.add_command(label="Save", background="#444", foreground="#fff",
                              activebackground="#666", activeforeground="#fff", command=self.save_pdf)
        file_menu.add_command(label="Exit Application", background="#444", foreground="#fff",
                              activebackground="#666", activeforeground="#fff", command=self.exit)

        menu_bar.add_cascade(label="File", menu=file_menu)
        root.config(menu=menu_bar)






    def open_pdf(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

        if not self.file_path:
            return


        try:
            self.pdf_document = fitz.open(self.file_path)
            if self.pdf_document.needs_pass:
                self.request_password()
            self.current_page = 0
            self.zoom_level = 1.0

            self.page_rotations = [0 for i in range(len(self.pdf_document))]

            self.display_page()

            self.total_pages.configure(text=f"{len(self.pdf_document)}")
            self.current_page = 0

        except Exception as e:
            pass


    def open_pdf_I(self):
        if not self.file_path:
            self.file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

        if not self.file_path:
            return

        try:
            self.pdf_document = fitz.open(self.file_path)
            if self.pdf_document.needs_pass:
                self.request_password()
            self.current_page = 0
            self.zoom_level = 1.0

            self.page_rotations = [0 for i in range(len(self.pdf_document))]  # Reset rotations
            self.display_page()

            self.total_pages.configure(text=f"{len(self.pdf_document)}")
            self.current_page = 0

        except Exception as e:
            pass



    def request_password(self):
        self.dialogue_box = CTkToplevel(self.root)  # Set parent window
        self.dialogue_box.resizable(False, False)
        self.dialogue_box.wm_iconbitmap("Icon.ico")

        self.dialogue_box.title("The PDF is Locked !")
        self.dialogue_box.configure(fg_color="black")
        self.dialogue_box.attributes("-topmost", True)


        CTkLabel(master=self.dialogue_box, text="This PDF file is protected.", font=("Arial", 18), fg_color = "black",
                 text_color = "white").place(relx=0.05, rely=0.05)
        CTkLabel(master=self.dialogue_box, text="Enter the password to open it.", fg_color = "black", text_color = "white",
                 font=("Arial", 18)).place(relx=0.05, rely=0.2)


        self.password = CTkEntry(master=self.dialogue_box, show="*", text_color="black", font=("Arial", 20), width=270,
                                 corner_radius=0, fg_color="white")
        self.password.place(relx=0.04, rely=0.42)


        self.show_hide_button = CTkButton(
            master=self.dialogue_box, command=self.show_hide_function,
            hover_color="white", image=self.show_image, fg_color="white",
            text_color="black", text="", font=("Arial", 12), width=40, corner_radius=0)
        self.show_hide_button.place(rely=0.42, relx=0.8)


        self.confirm_button = CTkButton(master=self.dialogue_box, command=self.confirm_function, fg_color="red",
                                        hover_color="dark red", text="Confirm", font=("Arial", 20), width=100)
        self.confirm_button.place(relx=0.1, rely=0.7)

        self.cancel_button = CTkButton(master=self.dialogue_box, command=self.cancel_function, fg_color="red",
                                       hover_color="dark red", text="Cancel", font=("Arial", 20), width=100)
        self.cancel_button.place(relx=0.55, rely=0.7)

        self.open_centered_popup(self.dialogue_box)



    def show_hide_function(self):
        if self.password.cget('show') == "*":
            self.password.configure(show="")
            self.show_hide_button.configure(image=self.hide_image)
        else:
            self.password.configure(show="*")
            self.show_hide_button.configure(image=self.show_image)



    def confirm_function(self):
        password = self.password.get().strip()

        if not password:
            messagebox.showwarning("Warning", "Password cannot be empty!")
            return

        if self.pdf_document.authenticate(password):
            messagebox.showinfo("Success", "PDF unlocked successfully!")
            self.dialogue_box.withdraw()
        else:
            messagebox.showerror("Error", "Incorrect password. Please try again.")
            self.password.delete(0, 'end')




    def cancel_function(self):
        self.dialogue_box.withdraw()

    def open_centered_popup(self, key):
        root_x = root.winfo_x()
        root_y = root.winfo_y()
        root_width = root.winfo_width()
        root_height = root.winfo_height()

        pos_x = root_x + (root_width // 2) - (root_width // 4) + (root_width // 10)
        pos_y = root_y + (root_height // 2) - (root_height // 4) + (root_height // 8)

        key.geometry(f"300x200+{pos_x}+{pos_y}")





    def display_page(self):
        if not self.pdf_document:
            return

        page = self.pdf_document[self.current_page]

        rotation = self.page_rotations[self.current_page]

        mat = fitz.Matrix(self.zoom_level * 2, self.zoom_level * 2).prerotate(rotation)
        pix = page.get_pixmap(matrix=mat)

        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)


        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        x_offset = max((canvas_width - pix.width) // 2, 0)
        y_offset = max((canvas_height - pix.height) // 2, 0)


        self.tk_image = ImageTk.PhotoImage(img)


        self.canvas.delete("all")
        self.canvas.create_image(x_offset, y_offset, anchor=tk.NW, image=self.tk_image)
        self.canvas.config(scrollregion=(0, 0, pix.width, pix.height))
        self.total_pages.configure(text=f"{len(self.pdf_document)}")

        self.page_label.configure(text=f"{self.current_page + 1}")



    def resize_page(self, event):
        self.display_page()



    def previous_page(self):
        if self.pdf_document and self.current_page > 0:
            self.current_page -= 1
            self.display_page()



    def next_page(self):
        if self.pdf_document and self.current_page < len(self.pdf_document) - 1:
            self.current_page += 1
            self.display_page()



    def zoom_in(self):
        if self.pdf_document:
            self.zoom_level += 0.2
            self.display_page()



    def zoom_out(self):
        if self.pdf_document and self.zoom_level > 0.4:
            self.zoom_level -= 0.2
            self.display_page()



    def rotate_clockwise(self):
        if self.pdf_document:
            self.page_rotations[self.current_page] = (self.page_rotations[self.current_page] + 90) % 360
            self.display_page()



    def rotate_counterclockwise(self):
        if self.pdf_document:
            self.page_rotations[self.current_page] = (self.page_rotations[self.current_page] - 90) % 360
            self.display_page()



    def save_pdf(self):
        if not self.pdf_document:
            messagebox.showerror("Error", "No PDF is currently open.")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if save_path:
            for page_num, page in enumerate(self.pdf_document):
                page.set_rotation(self.page_rotations[page_num])

            self.pdf_document.save(save_path)
            messagebox.showinfo("Success", f"PDF saved successfully to {save_path}!")




    def convert_to_word(self):
        if not self.pdf_document:
            messagebox.showerror("Error", "No PDF is currently open.")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Documents", "*.docx")])
        if save_path:
            doc = Document()
            for page_num, page in enumerate(self.pdf_document, start=1):
                text = page.get_text()
                doc.add_paragraph(f"Page {page_num}\n{text}")
            doc.save(save_path)
            messagebox.showinfo("Success", f"Word document saved successfully to {save_path}!")




    def on_window_resize(self, event):
        if self.resize_timer:
            self.resize_timer.cancel()

        self.resize_timer = Timer(self.resize_delay, self.display_page)
        self.resize_timer.start()




    def exit(self):
        self.root.quit()




    def convert_to_images(self):
        to_image = Convert_Entire_Pdf_To_Images.To_Image()
        to_image.open_pdf()
        to_image.save_all_pages_as_images()



    def convert_word_func(self):
        to_word = Convert_to_word_full_pdf.To_Word()
        to_word.open_pdf()
        to_word.convert_pdf_to_word()




    def lock_pdf_func(self):
        def confirm_function():
            if len(password.get()) == 0:
                messagebox.showerror("Error","Password cannot be empty.")
                return
            set_pass.withdraw()
            Protect_Pdf.lock_pdf(input_pdf, password.get())


        def cancel_function():
            set_pass.withdraw()



        def show_hide_function():
            if password.cget('show') == "*":
                password.configure(show="")
                show_hide_button.configure(image=self.hide_image)  # Fix image toggle
            else:
                password.configure(show="*")
                show_hide_button.configure(image=self.show_image)

        input_pdf = filedialog.askopenfilename()
        if not input_pdf :
            return


        set_pass = CTkToplevel(self.root)
        set_pass.resizable(False, False)
        set_pass.wm_iconbitmap("Icon.ico")
        set_pass.attributes("-topmost", True)

        set_pass.title("Set Password")
        set_pass.configure(fg_color="black")

        CTkLabel(master=set_pass, text="Enter then password that you", font=("Arial", 18), text_color = "white").place(relx=0.05, rely=0.05)
        CTkLabel(master=set_pass, text="want to use.", font=("Arial", 18), text_color = "white").place(relx=0.05, rely=0.2)



        password = CTkEntry(master=set_pass, show="*", text_color="black", font=("Arial", 20), width=270,
                                 corner_radius=0, fg_color="white")
        password.place(relx=0.04, rely=0.42)



        show_hide_button = CTkButton( master=set_pass, command=show_hide_function, hover_color="white", image=self.show_image, fg_color="white",
            text_color="black", text="", font=("Arial", 12), width=40, corner_radius=0)
        show_hide_button.place(rely=0.42, relx=0.8)

        confirm_button = CTkButton(master=set_pass, command=confirm_function, fg_color="red", text_color = "black",
                                        hover_color="dark red", text="Confirm", font=("Arial", 20), width=100)
        confirm_button.place(relx=0.1, rely=0.7)

        cancel_button = CTkButton(master=set_pass, command = cancel_function, fg_color="red", text_color = "black",
                                       hover_color="dark red", text="Cancel", font=("Arial", 20), width=100)
        cancel_button.place(relx=0.55, rely=0.7)

        self.open_centered_popup(set_pass)




    def modify_password_func(self):

        input_pdf = filedialog.askopenfilename()
        if not input_pdf :
            return

        try:
            pikepdf.Pdf.open(input_pdf)
            messagebox.showerror("Error", "The PDF is not locked. No password is required.")
            return

        except FileNotFoundError:
            messagebox.showerror("Error", "File not found.")

        except Exception:
            self.get_current_password(input_pdf)




    def check(self, input_pdf, current_password):
        try:
            new_pdf = pikepdf.Pdf.open(input_pdf, password=current_password)
            self.get_new_password(new_pdf)

        except pikepdf.PasswordError:
            messagebox.showerror("Error", "Incorrect Password. Please try again !")
            return


    def set_password(self, input_pdf, password):

        new_user_password = password
        new_owner_password = "MAAZ"

        modified_permissions = pikepdf.Permissions(extract=False)


        output_pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if not output_pdf_path:
            print("No save location selected. Exiting.")
            return

        input_pdf.save(
            output_pdf_path,
            encryption=pikepdf.Encryption(user=new_user_password, owner=new_owner_password, allow=modified_permissions))
        messagebox.showinfo("Success", "Pdf saved successfully.")




    def get_new_password(self, input_pdf):
        def confirm_function():
            if len(password.get()) == 0:
                messagebox.showerror("Error","Password cannot be empty.")
                return
            set_pass.withdraw()
            self.set_password(input_pdf, password.get())



        def cancel_function():
            set_pass.withdraw()



        def show_hide_function():
            if password.cget('show') == "*":
                password.configure(show="")
                show_hide_button.configure(image=self.hide_image)
            else:
                password.configure(show="*")
                show_hide_button.configure(image=self.show_image)


        set_pass = CTkToplevel(self.root)
        set_pass.resizable(False, False)
        set_pass.wm_iconbitmap("Icon.ico")
        set_pass.attributes("-topmost", True)

        set_pass.title("Update the password")
        set_pass.configure(fg_color="black")


        CTkLabel(master=set_pass, text="Enter the password that you want ", text_color = "white", font=("Arial", 18)).place(relx=0.05, rely=0.05)
        CTkLabel(master=set_pass, text="to use for the pdf.", text_color = "white", font=("Arial", 18)).place(relx=0.05, rely=0.2)



        password = CTkEntry(master=set_pass, show="*", text_color="black", font=("Arial", 20), width=270,
                                 corner_radius=0, fg_color="white")
        password.place(relx=0.04, rely=0.42)


        show_hide_button = CTkButton( master=set_pass, command=show_hide_function, hover_color="white", image=self.show_image, fg_color="white",
            text_color="black", text="", font=("Arial", 12), width=40, corner_radius=0)
        show_hide_button.place(rely=0.42, relx=0.8)

        confirm_button = CTkButton(master=set_pass, command=confirm_function, fg_color="red", text_color = "black", hover_color="dark red", text="Confirm", font=("Arial", 20), width=100)
        confirm_button.place(relx=0.1, rely=0.7)

        cancel_button = CTkButton(master=set_pass, command = cancel_function, fg_color="red", text_color = "black",hover_color="dark red", text="Cancel", font=("Arial", 20), width=100)
        cancel_button.place(relx=0.55, rely=0.7)

        self.open_centered_popup(set_pass)



    def get_current_password(self, input_pdf):
        def confirm_function():
            if len(password.get()) == 0:
                messagebox.showerror("Error","Password cannot be empty.")
                return
            set_pass.withdraw()
            self.check(input_pdf, password.get())



        def cancel_function():
            set_pass.withdraw()

        def show_hide_function():
            if password.cget('show') == "*":
                password.configure(show="")
                show_hide_button.configure(image=self.hide_image)  # Fix image toggle
            else:
                password.configure(show="*")
                show_hide_button.configure(image=self.show_image)


        set_pass = CTkToplevel(self.root)  # Set parent window
        set_pass.resizable(False, False)
        set_pass.wm_iconbitmap("Icon.ico")
        set_pass.attributes("-topmost", True)

        set_pass.title("The PDF is Locked !")
        set_pass.configure(fg_color="black")


        CTkLabel(master=set_pass, text="Enter the current password for ", text_color = "white",font=("Arial", 18)).place(relx=0.05, rely=0.05)
        CTkLabel(master=set_pass, text="the pdf", font=("Arial", 18), text_color = "white").place(relx=0.05, rely=0.2)


        password = CTkEntry(master=set_pass, show="*", text_color="black", font=("Arial", 20), width=270,
                                 corner_radius=0, fg_color="white")
        password.place(relx=0.04, rely=0.42)



        show_hide_button = CTkButton(
            master=set_pass, command=show_hide_function,
            hover_color="white", image=self.show_image, fg_color="white",
            text_color="black", text="", font=("Arial", 12), width=40, corner_radius=0)
        show_hide_button.place(rely=0.42, relx=0.8)


        confirm_button = CTkButton(master=set_pass, command=confirm_function, fg_color="red", text_color = "black",
                                        hover_color="dark red", text="Confirm", font=("Arial", 20), width=100)
        confirm_button.place(relx=0.1, rely=0.7)

        cancel_button = CTkButton(master=set_pass, command = cancel_function, fg_color="red", text_color = "black",
                                       hover_color="dark red", text="Cancel", font=("Arial", 20), width=100)
        cancel_button.place(relx=0.55, rely=0.7)

        self.open_centered_popup(set_pass)







    def show_all_tools(self):
        self.edit_tools_frame.pack_forget()
        self.convert_frame.pack_forget()
        self.support_frame.pack_forget()
        self.all_tools_frame.pack(side="left", fill="y")


    def show_support_frame(self):
        self.edit_tools_frame.pack_forget()
        self.all_tools_frame.pack_forget()
        self.convert_frame.pack_forget()
        self.support_frame.pack(side="left", fill="y")


    def hide_all_tools(self):
        self.all_tools_frame.pack_forget()

    def hide_support_frame(self):
        self.support_frame.pack_forget()

    def show_edit_frame(self):
        self.all_tools_frame.pack_forget()
        self.convert_frame.pack_forget()
        self.support_frame.pack_forget()
        self.edit_tools_frame.pack(side="left", fill="y")

    def hide_edit_frame(self):
        self.edit_tools_frame.pack_forget()

    def show_convert_frame(self):
        self.all_tools_frame.pack_forget()
        self.edit_tools_frame.pack_forget()
        self.support_frame.pack_forget()
        self.convert_frame.pack(side="left", fill="y")

    def hide_convert_frame(self):
        self.convert_frame.pack_forget()

    def split(self):
        def confirm_function():
            split_pdf = Split_Pdf_II
            split_pdf.main(password.get())
            page_no_window.withdraw()

        def cancel_function():
            page_no_window.withdraw()

        page_no_window = CTk()
        page_no_window.resizable(False, False)
        start_x_coordinate = self.root.winfo_x()
        start__ycoordinate = self.root.winfo_y()

        page_no_window.geometry(f"300x150+{start_x_coordinate + (window_width // 4)}+{start__ycoordinate + (window_height // 4)}")
        page_no_window.title("Enter the page number ")
        page_no_window.configure(fg_color="black")

        CTkLabel(master=page_no_window, text="Enter the page number where you", text_color = "white", font=("Arial", 18)).place(relx=0.05, rely=0.05)
        CTkLabel(master=page_no_window, text="want to split the PDF in two parts.", text_color = "white",font=("Arial", 18)).place(relx=0.05,
                                                                                                              rely=0.2)

        password = CTkEntry(master=page_no_window, text_color="black", font=("Arial", 20), width=270, corner_radius=0,
                            fg_color="white")
        password.place(relx=0.04, rely=0.42)

        confirm_button = CTkButton(master=page_no_window, command=confirm_function, fg_color="red", text_color = "black",
                                   hover_color="dark red", text="Ok", font=("Arial", 20), width=100)
        confirm_button.place(relx=0.1, rely=0.7)

        cancel_button = CTkButton(master=page_no_window, command=cancel_function, fg_color="red", text_color = "black",
                                  hover_color="dark red", text="Cancel", font=("Arial", 20), width=100)
        cancel_button.place(relx=0.55, rely=0.7)

        self.open_centered_popup(page_no_window)
        page_no_window.mainloop()


    def compress_pdf(self):
        Compress_Mini.compress()


    def delete_currrent_page(self):
        if len(self.page_rotations) <= 1:
            self.canvas.delete("all")
            self.page_rotations.clear()
            return

        for i in range(self.current_page, len(self.pdf_document) - 1):
            self.page_rotations[i] = self.page_rotations[i + 1]

        delete = Delete_a_page_II
        delete_pg = delete.Delete_Page(self.pdf_document)
        delete_pg.delete_page(self.current_page)

        self.page_rotations.pop()

        if self.current_page == len(self.page_rotations) - 1:
            self.current_page = self.current_page - 1

        if self.current_page == len(self.page_rotations):
            self.current_page -= 1
        self.display_page()



    def remove_watermark(self):
        remove = Remove_WaterMark
        remove.main()

    def request_blank_page_no(self):

        if len(self.page_rotations) != 0:
            self.page_rotations.append(0)
            for i in range(len(self.page_rotations) - 1, self.current_page, -1):
                self.page_rotations[i] = self.page_rotations[i - 1]
            self.page_rotations[self.current_page] = 0

            insert = Insert_Page
            messagebox.showinfo("Success", f"Blank page inserted successfully at page number {self.current_page + 1}")
            self.pdf_document = insert.insert_blank(self.current_page, self.pdf_document)
            self.display_page()

        else:
            messagebox.showerror("Error", "No pdf is currently open.")
            return



    def request_image_page(self):

        if len(self.page_rotations) != 0:
            self.page_rotations.append(0)

            for i in range(len(self.page_rotations) - 1, self.current_page, -1):
                self.page_rotations[i] = self.page_rotations[i - 1]
            self.page_rotations[self.current_page] = 0

            insert = Insert_Page
            self.pdf_document = insert.insert_image_page(self.current_page, self.pdf_document)
            messagebox.showinfo("Success", f"Page inserted successfully at page number {self.current_page + 1}")
            self.display_page()

        else:
            messagebox.showerror("Error", "No pdf is currently open.")
            return



    def create_pdf(self):

        selected_image = []

        while True:
            file_path = filedialog.askopenfilenames(
                filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.tiff"), ("All Files", "*.*")],
                title="Select Images")

            if not file_path:  # Stop when the user cancels
                break
            selected_image.append(file_path)

        if not selected_image:
            messagebox.showerror("Error", "No Images selected for merging.")
            return

        temp_pdf_path = "temp_preview.pdf"
        try:
            images = [Image.open(image_path[0]).convert("RGB") for image_path in selected_image]

            images[0].save(temp_pdf_path, save_all=True, append_images=images[1:])
        except Exception as e:
            print(f"Error generating PDF: {e}")
            return

        try:
            images[0].save(temp_pdf_path, save_all=True, append_images=images[1:])
            print(f"PDF saved successfully at: {temp_pdf_path}")
        except Exception as e:
            print(f"Error saving PDF: {e}")

        file_path = temp_pdf_path
        if not file_path:
            return


        try:
            self.pdf_document = fitz.open(file_path)

            self.current_page = 0
            self.zoom_level = 1.0

            self.page_rotations = [0 for i in range(len(self.pdf_document))]

            self.display_page()

            self.total_pages.configure(text=f"{len(self.pdf_document)}")
            self.current_page = 0

        except Exception as e:
            pass

        self.display_page()







    def request_order(self):
        def confirm(total_pages, reader):
            output_path = "Pdfs\\sample.pdf"
            if not output_path:
                return

            new_order = order.get().strip()
            writer = PdfWriter()

            self.reorder.withdraw()

            try:
                page_indices = [int(i) - 1 for i in new_order.split(",")]

                if not all(0 <= i < total_pages for i in page_indices):
                    messagebox.showerror("Error", "Invalid page numbers.")
                    return

                for i in page_indices:
                    writer.add_page(reader.pages[i])

                with open(output_path, "wb") as output_file:
                    writer.write(output_file)

                self.file_path = output_path
                self.open_pdf_I()


            except ValueError:
                print("Invalid input! Please enter a valid comma-separated list of numbers.")



        def cancel():
            self.reorder.withdraw()

        if not self.file_path:
            self.file_path = filedialog.askopenfilename(title="Select the PDF File", filetypes=[("PDF Files", "*.pdf")])


        if not self.file_path:
            return

        reader = PdfReader(self.file_path)
        total_pages = len(reader.pages)

        messagebox.showinfo("How to use", "Enter the order in which you want the PDF pages to appear. Eg - 3, 1, 2, 4. When pdf contains 4 pages. "
                                          "The numbers should be separated by commas.")

        self.reorder = CTk()
        self.reorder.resizable(False, False)

        self.reorder.title("Enter the order")
        self.reorder.configure(fg_color="black")

        label1 = CTkLabel(master=self.reorder, text="Enter the order of the pages. This", text_color = "white", font=("Arial", 18))
        label1.place(relx=0.05, rely=0.05)

        label2 = CTkLabel(master=self.reorder, text=f"pdf contains {total_pages} pages.", text_color = "white",font=("Arial", 18))
        label2.place(relx=0.05, rely=0.2)

        order = CTkEntry(master = self.reorder, text_color="black", font=("Arial", 20), width=270, corner_radius=0, fg_color="white")
        order.place(relx=0.04, rely=0.45)


        confirm_button = CTkButton(master = self.reorder, fg_color = "red", text_color = "black", command = lambda: confirm(total_pages, reader), hover_color = "dark red", text="Confirm", font=("Arial", 20), width=100)
        confirm_button.place(relx=0.1, rely=0.75)

        cancel_button = CTkButton(master=self.reorder, fg_color = "red", text_color = "black",command = cancel, hover_color = "dark red", text="Cancel", font=("Arial", 20), width=100)
        cancel_button.place(relx=0.55, rely=0.75)



        root_x = self.root.winfo_x()
        root_y = self.root.winfo_y()
        root_width = self.root.winfo_width()
        root_height = self.root.winfo_height()

        pos_x = root_x + (root_width // 2) - (root_width // 4) + (root_width // 10)
        pos_y = root_y + (root_height // 2) - (root_height // 4) + (root_height // 8)


        self.reorder.geometry(f"300x150+{pos_x}+{pos_y}")
        self.reorder.mainloop()







    def swap(self):
        def swap_pages():

            try:
                page1 = int(entry_page1.get()) - 1
                page2 = int(entry_page2.get()) - 1

                reader = PdfReader(self.file_path)
                writer = PdfWriter()
                total_pages = len(reader.pages)

                self.swap_window.withdraw()

                if not (0 <= page1 < total_pages and 0 <= page2 < total_pages):
                    messagebox.showerror("Invalid Input", "Page numbers must be within range!")
                    return

                pages = list(reader.pages)

                pages[page1], pages[page2] = pages[page2], pages[page1]

                self.page_rotations[page1], self.page_rotations[page2] = self.page_rotations[page2], self.page_rotations[page1]

                for page in pages:
                    writer.add_page(page)

                output_path = "Pdfs\\sample.pdf"
                if output_path:
                    with open(output_path, "wb") as output_file:
                        writer.write(output_file)

                    self.file_path = output_path
                    self.open_pdf_I()


            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid numbers!")

        def cancel():
            self.swap_window.withdraw()

        if not self.file_path:
            messagebox.showerror("Error", "No pdf is currently open.")
            return



        self.swap_window = CTk()  # Set parent window
        self.swap_window.resizable(False, False)

        self.swap_window.title("Enter the order")
        self.swap_window.configure(fg_color="black")

        label1 = CTkLabel(master=self.swap_window, text="Enter the page number that you", text_color= "white", font=("Arial", 18))
        label1.place(relx=0.05, rely=0.05)

        label2 = CTkLabel(master=self.swap_window, text="want to swap. For example page", font=("Arial", 18), text_color= "white")
        label2.place(relx=0.05, rely=0.17)

        label3 = CTkLabel(master=self.swap_window, text="number 4 and 10 when these two", font=("Arial", 18), text_color= "white")
        label3.place(relx=0.05, rely=0.29)

        label4 = CTkLabel(master=self.swap_window, text="pages exist in the pdf.", font=("Arial", 18), text_color= "white")
        label4.place(relx=0.05, rely=0.41)

        page1 = CTkLabel(master=self.swap_window, text="Page 1 : ", font=("Arial", 18), text_color= "white")
        page1.place(relx=0.04, rely=0.6)

        entry_page1 = CTkEntry(master=self.swap_window, text_color="black", font=("Arial", 20), width=50,
                               corner_radius=0, fg_color="white")
        entry_page1.place(relx=0.27, rely=0.6)

        page2 = CTkLabel(master=self.swap_window, text="Page 2 : ", font=("Arial", 18), text_color= "white")
        page2.place(relx=0.5, rely=0.6)

        entry_page2 = CTkEntry(master=self.swap_window, text_color="black", font=("Arial", 20), width=50,
                               corner_radius=0, fg_color="white")
        entry_page2.place(relx=0.75, rely=0.6)


        confirm_button = CTkButton(master=self.swap_window, command=swap_pages, fg_color="red", hover_color="dark red",
                                   text="Confirm", font=("Arial", 20), width=100, text_color="black")
        confirm_button.place(relx=0.1, rely=0.8)


        cancel_button = CTkButton(master=self.swap_window, command=cancel, fg_color="red", hover_color="dark red",
                                  text="Cancel", font=("Arial", 20), width=100, text_color="black")
        cancel_button.place(relx=0.55, rely=0.8)

        root_x = self.root.winfo_x()
        root_y = self.root.winfo_y()
        root_width = self.root.winfo_width()
        root_height = self.root.winfo_height()

        pos_x = root_x + (root_width // 2) - (root_width // 4) + (root_width // 10)
        pos_y = root_y + (root_height // 2) - (root_height // 4) + (root_height // 8)

        self.swap_window.geometry(f"300x220+{pos_x}+{pos_y}")
        self.swap_window.mainloop()



    def convert_to_excel(self):
        convert = Convert_Pdf_to_excel
        convert.convert_to_xls()



    def add_watermark_I(self):

        self.window = CTkToplevel(self.root, fg_color = "black")
        self.window.title("PDF Watermark Preview")

        self.window.geometry("768x576")
        self.window.resizable(False, False)
        self.window.attributes("-topmost", True)


        self.label = CTkLabel(self.window, text="Enter the text that you want to use", text_color= "white", font=("Aerial", 20, "bold"))
        self.label.place(relx=0.01, rely=0.01)

        self.label = CTkLabel(self.window, text="Enter the text that you want to use", text_color= "white", font=("Aerial", 20, "bold"))
        self.label.place(relx=0.01, rely=0.01)

        self.text_watermark = CTkEntry(self.window, width = 320, corner_radius = 0, fg_color = "white", border_width = 3,
                                  text_color = "black", font=("Aerial", 20, "bold"))
        self.text_watermark.place(relx = 0.02, rely = 0.08)

        add_text = CTkButton(self.window, text="Display Text", text_color="black", command = self.add_text,
                                  font=("Aerial", 20, "bold"), fg_color="red", hover_color="dark red")
        add_text.place(relx=0.02, rely=0.15)



        self.screen = CTkCanvas(self.window, width=512, height= 692 , bg="white")
        self.screen.place(relx=0.45, rely=0.0)


        text_size_label = CTkLabel(self.window, text="Text Size", font=("Aerial", 20, "bold"), text_color = "white")
        text_size_label.place(relx = 0.02, rely = 0.23)

        self.text_size_slider = CTkSlider(self.window, from_=1, to=200, number_of_steps=10, command = self.text_size)
        self.text_size_slider.set(0.4)
        self.text_size_slider.place(relx = 0.02, rely = 0.29)


        size_label = CTkLabel(self.window, text="Image Size", font=("Aerial", 20, "bold"), text_color = "white")
        size_label.place(relx = 0.02, rely = 0.34)

        size_slider = CTkSlider(self.window, from_=0.1, to=1, number_of_steps=10, command=self.update_size)
        size_slider.set(0.3)
        size_slider.place(relx = 0.02, rely = 0.4)


        pos_x_label = CTkLabel(self.window, text="Horizontal Position", font=("Aerial", 20, "bold"), text_color = "white")
        pos_x_label.place(relx=0.02, rely=0.45)

        self.pos_x_slider = CTkSlider(self.window, from_=0, to=1, number_of_steps=10, command=self.update_position)
        self.pos_x_slider.set(0.3)  # Default X position (30% of page width)
        self.pos_x_slider.place(relx=0.02, rely=0.51)

        pos_y_label = CTkLabel(self.window, text="Vertical Position", font=("Aerial", 20, "bold"), text_color = "white")
        pos_y_label.place(relx=0.02, rely=0.56)

        self.pos_y_slider = CTkSlider(self.window, from_=0, to=1, number_of_steps=10, command=self.update_position)
        self.pos_y_slider.set(0.3)  # Default Y position (30% of page height)
        self.pos_y_slider.place(relx=0.02, rely=0.63)

        opacity_label = CTkLabel(self.window, text="Transparency", font=("Aerial", 20, "bold"), text_color = "white")
        opacity_label.place(relx=0.02, rely=0.68)

        opacity_slider = CTkSlider(self.window, from_=0, to=1, number_of_steps=10, command=self.update_opacity)
        opacity_slider.set(0.3)  # Default opacity
        opacity_slider.place(relx=0.02, rely=0.75)

        upload_pdf = CTkButton(self.window, text="Upload PDF", command = self.upload_pdf, text_color = "black",
                                   font=("Aerial", 20, "bold"), fg_color="red", hover_color="dark red")
        upload_pdf.place(relx=0.005, rely=0.85)

        upload_img_btn = CTkButton(self.window, text="Upload Watermark", command = self.upload_image, text_color = "black",
                                   font=("Aerial", 20, "bold"), fg_color="red", hover_color="dark red")
        upload_img_btn.place(relx=0.2, rely=0.85)

        self.save_btn = CTkButton(self.window, text="Save Watermarked PDF", text_color="black", command = self.save,
                                  font=("Aerial", 20, "bold"), fg_color="red", hover_color="dark red")
        self.save_btn.place(relx=0.08, rely=0.92)





        self.pdf_path = None
        self.image_path = None
        self.output_pdf_path = "watermarked_output.pdf"
        self.opacity = 0.3
        self.pos_x = 0.3
        self.pos_y = 0.3
        self.font_size = 100
        self.size = 0.3





    def upload_pdf(self):

        if not self.pdf_path:
            self.pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

        if self.pdf_path:
            self.add_watermark(None)
            self.preview_pdf()


    def upload_image(self):

        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if self.pdf_path:
            self.add_watermark(None)
            self.preview_pdf()


    def update_opacity(self, value):

        self.opacity = float(value)
        if self.pdf_path:
            if self.image_path:
                self.add_watermark(None)
                self.preview_pdf()


    def update_position(self, value):

        self.pos_x = self.pos_x_slider.get()
        self.pos_y = self.pos_y_slider.get()
        if self.pdf_path:
            if self.image_path:
                self.add_watermark(None)
                self.preview_pdf()
            else:
                self.add_watermark(self.text_watermark.get())
                self.preview_pdf()


    def update_size(self, value):
        self.size = float(value)
        if self.pdf_path:
            if self.image_path:
                self.add_watermark(None)
                self.preview_pdf()


    def add_watermark(self, text):
        doc = fitz.open(self.pdf_path)
        page = doc[0]
        rect = page.rect

        if self.image_path:
            img = Image.open(self.image_path).convert("RGBA")

            img_width = int(rect.width * self.size)
            img_height = int(rect.height * self.size)
            img = img.resize((img_width, img_height))

            alpha = img.split()[3]
            alpha = alpha.point(lambda p: int(p * self.opacity))
            img.putalpha(alpha)

            img_path = "temp_watermark.png"
            img.save(img_path)

            position = (rect.width * self.pos_x, rect.height * self.pos_y)

            for i in range(len(doc)):
                page = doc[i]
                page.insert_image(fitz.Rect(position[0], position[1], position[0] + img_width, position[1] + img_height),
                                  filename=img_path, overlay=True)

        elif text:
            watermark_text = text
            text_rect = fitz.Rect(rect.width * self.pos_x, rect.height * self.pos_y,
                                  rect.width * self.pos_x + 200, rect.height * self.pos_y + 50)

            for i in range(len(doc)):
                page = doc[i]
                page.insert_text(
                    (rect.width * self.pos_x + 10, rect.height * self.pos_y + 10),
                    watermark_text,
                    fontsize=self.font_size,
                    color=(0,0,0),)

        doc.save(self.output_pdf_path)
        doc.close()


    def preview_pdf(self):
        images = convert_from_path(self.output_pdf_path, first_page=1, last_page=1)
        self.img = images[0]

        self.img.thumbnail((500, 600))
        self.tk_img = ImageTk.PhotoImage(self.img)

        self.screen.create_image(0, 0, anchor="nw", image=self.tk_img)
        self.save_btn.configure(state="normal")

    def add_text(self):
        self.image_path = None
        self.add_watermark(self.text_watermark.get())
        self.preview_pdf()


    def save(self):
        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if save_path:
            os.rename(self.output_pdf_path, save_path)
            self.label.configure(text="PDF saved successfully!")


    def text_size(self, value):
        self.font_size = int(value)
        self.add_watermark(self.text_watermark.get())
        self.preview_pdf()


    def support(self):
         webbrowser.open("https://www.linkedin.com/in/mohammed-maaz-rayeen-b914a4303")




if __name__ == "__main__":
    root = CTk()
    window_height = root.winfo_screenheight()
    window_width = root.winfo_screenwidth()
    root.geometry(f"{window_width}x{window_height - (window_height // 10)}+-10+0")
    pdf_reader = PDFReader(root)
    root.mainloop()