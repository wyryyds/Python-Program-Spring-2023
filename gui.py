from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Toplevel, Label

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Python Projects\Python-final-project\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Gui:
    def __init__(self):
        self.window = Tk()
        self.window.title('Word小助手')
        self.window.geometry("617x462")
        self.window.configure(bg="#A6D6DD")

        self.canvas = Canvas(
            self.window,
            bg="#A6D6DD",
            height=462,
            width=617,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            118.0,
            231.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            426.0,
            231.0,
            image=self.image_image_2
        )

        self.get_pages_btn_image = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.get_pages_btn = Button(
            image=self.get_pages_btn_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.init_btn,
            relief="flat"
        )
        self.get_pages_btn.place(
            x=248.0,
            y=230.0,
            width=150.0,
            height=45.0
        )

        self.word_2_pdf_btn_image = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.word_2_pdf_btn = Button(
            image=self.word_2_pdf_btn_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.init_btn,
            relief="flat"
        )
        self.word_2_pdf_btn.place(
            x=241.0,
            y=97.0,
            width=161.0,
            height=52.0
        )

        self.directory_btn_img = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.directory_btn = Button(
            image=self.directory_btn_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.init_btn,
            relief="flat"
        )
        self.directory_btn.place(
            x=452.0,
            y=95.0,
            width=155.00001525878906,
            height=52.0
        )

        self.title_btn_image = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.title_btn = Button(
            image=self.title_btn_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("title btn clicked"),
            relief="flat"
        )
        self.title_btn.place(
            x=15.0,
            y=28.0,
            width=199.0,
            height=46.0
        )

        self.file_entry_image = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.file_entry_bg = self.canvas.create_image(
            441.5,
            51.5,
            image=self.file_entry_image
        )
        self.file_entry = Entry(
            bd=0,
            bg="#58BDDD",
            fg="#000716",
            highlightthickness=0
        )
        self.file_entry.place(
            x=289.0,
            y=43.0,
            width=305.0,
            height=15.0
        )

        self.load_file_btn_image = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.load_file_btn = Button(
            image=self.load_file_btn_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("load file btn clicked"),
            relief="flat"
        )
        self.load_file_btn.place(
            x=253.0,
            y=28.0,
            width=36.0,
            height=36.0
        )
        self.window.resizable(False, False)

    def run(self):
        self.window.mainloop()

    def init_btn(self):
        self.new_top_level('请先选择一个文档')

    def set_load_file_btn(self, func):
        self.load_file_btn.bind('<Button-1>', func)

    def set_word_2_pdf_btn(self, func):
        self.word_2_pdf_btn.bind('<Button-1>', func)

    def set_get_pages_btn(self, func):
        self.get_pages_btn.bind('<Button-1>', func)

    def set_directory_btn(self, func):
        self.directory_btn.bind('<Button-1>', func)

    def new_top_level(self, info):
        top = Toplevel(self.window)
        top.title('提示信息')
        top.geometry('400x200')
        label = Label(top, text=info)
        label.pack()
