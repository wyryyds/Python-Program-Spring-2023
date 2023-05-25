from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Toplevel, Label, Scrollbar, Frame

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
            command=self.init_func_btn,
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
            command=self.init_func_btn,
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
            command=self.init_func_btn,
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

    def init_func_btn(self):
        print('btn click')

    def set_load_file_btn(self, func):
        self.load_file_btn.bind('<Button-1>', lambda event: func())

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

    def new_top_level_for_list(self, title, info_list):
        top = Toplevel(self.window)
        top.title(title)
        top.geometry('400x600')

        # 创建滚动条
        scrollbar = Scrollbar(top)
        scrollbar.pack(side='right', fill='y')

        # 创建帧
        frame = Frame(top, width=400)
        frame.pack(fill='both', expand=True)

        # 创建画布
        canvas = Canvas(frame, yscrollcommand=scrollbar.set)
        canvas.pack(side='left', fill='both', expand=True)

        # 设置滚动条与画布的关联
        scrollbar.config(command=canvas.yview)

        # 创建内部帧，用于放置标签
        inner_frame = Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor='nw')

        # 添加标签到内部帧
        for t in info_list:
            label = Label(inner_frame, text=t)
            label.pack()

        # 更新画布的大小以确保能显示所有内容
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox('all'))

        # 根据内容的长度调整窗口的宽度
        label_width = max(label.winfo_reqwidth() for label in inner_frame.winfo_children())
        window_width = label_width + scrollbar.winfo_width() + 200  # 加上滚动条宽度和一些边距
        top.geometry(f'{window_width}x600')

        # 配置画布的滚动条和大小调整
        canvas.config(width=label_width, height=600)
        canvas.config(scrollregion=canvas.bbox('all'))

        def on_mousewheel(event):
            canvas.yview_scroll(-int(event.delta / 120), 'units')

        canvas.bind_all('<MouseWheel>', on_mousewheel)
