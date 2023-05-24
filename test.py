import os
import tkinter as tk
from tkinter import filedialog
def open_file_dialog():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_path.delete(0, tk.END)  # 清空路径框
        entry_path.insert(0, file_path)  # 显示选取的文件路径
        if os.path.isfile(file_path):
            os.startfile(file_path)


window = tk.Tk()

button = tk.Button(window, text="选择文件", command=open_file_dialog)
button.pack()

entry_path = tk.Entry(window, width=50)
entry_path.pack()


window.mainloop()


