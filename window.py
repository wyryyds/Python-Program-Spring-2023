import tkinter as tk


class Window:
    def __init__(self):
        self._window = tk.Tk()
        self._window.title('Word 助手')
        self._window.geometry('600x400')
        self.label = tk.Label(self._window, text='欢迎使用Word助手')
        self.label.pack()
        self._button1 = tk.Button(self._window, text='Word文档转PDF文档')
        self._button1.pack()
        self._button2 = tk.Button(self._window, text='统计Word文档页数')
        self._button2.pack()

    def new_top_level(self, info):
        top = tk.Toplevel(self._window)
        top.title('提示信息')
        top.geometry('400x200')
        label = tk.Label(top, text=info)
        label.pack()

    def run(self):
        self._window.mainloop()

    def set_word_2_pdf_btn(self, func):
        self._button1.bind('<Button-1>', func)

    def set_count_pages_btn(self, func):
        self._button2.bind('<Button-1>', func)
