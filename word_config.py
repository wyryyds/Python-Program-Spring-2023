import os
import win32com.client
from tkinter import filedialog


class WordConfig:
    def __init__(self):
        self._word = win32com.client.Dispatch("Word.Application")
        # 获取当前脚本（或模块）的绝对路径
        self._current_path = os.path.abspath(__file__)
        # 获取当前脚本（或模块）所在的目录路径
        self._project_directory = os.path.dirname(self._current_path)
        self._word_file_path = self._project_directory + '\WordFile\\'

    def get_word_file_path(self):
        return self._word_file_path

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self._word_file_path = file_path
            if os.path.isfile(file_path):
                os.startfile(file_path)

    def word_2_pdf(self):
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf")
        # 创建 Word 应用程序对象
        word = self._word
        word.Visible = False

        # 打开输入的 Word 文档
        doc = word.Documents.Open(os.path.abspath(self._word_file_path))

        # 将 Word 文档保存为 PDF
        doc.SaveAs(os.path.abspath(output_file), FileFormat=17)

        print('已将word文档转为pdf文档')

    def get_word_pages_count(self):
        try:
            word = self._word
            doc = word.Documents.Open(os.path.abspath(self._word_file_path))
            count = doc.ComputeStatistics(2)  # 2 表示统计页面数量
            return count
        except Exception as e:
            print("Error:", e)
