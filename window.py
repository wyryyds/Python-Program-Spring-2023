import tkinter as tk


class Window:
    def __init__(self):
        self._window = tk.Tk()
        self._window.title('Word 助手')
        self._window.geometry('600x400')
        self.label = tk.Label(self._window, text='欢迎使用Word助手')
        self.label.pack()
        self._button = tk.Button(self._window, text='Word文档转PDF文档')
        self._button.pack()

    def run(self):
        self._window.mainloop()

    def set_word_2_pdf_button(self, func):
        self._button.config(command=func)
