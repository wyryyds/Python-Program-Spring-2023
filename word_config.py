import os
import win32com.client
from tkinter import filedialog


class WordConfig:
    def __init__(self):
        # 创建 Word 应用程序对象
        self._word = win32com.client.Dispatch("Word.Application")
        # 获取当前脚本（或模块）的绝对路径
        self._current_path = os.path.abspath(__file__)
        # 获取当前脚本（或模块）所在的目录路径
        self._project_directory = os.path.dirname(self._current_path)
        self._word_file_path = self._project_directory + '\WordFile\\'
        self.word_is_open = False

    def get_word_file_path(self):
        return self._word_file_path

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self._word_file_path = file_path
            if os.path.isfile(file_path):
                os.startfile(file_path)
                self.word_is_open = True

    def word_2_pdf(self):
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf")
        if output_file:
            word = self._word
            word.Visible = False
            doc = word.Documents.Open(os.path.abspath(self._word_file_path))
            # 将 Word 文档保存为 PDF
            doc.SaveAs(os.path.abspath(output_file), FileFormat=17)
            return True
        else:
            return False

    def get_word_pages_count(self):
        try:
            word = self._word
            doc = word.Documents.Open(os.path.abspath(self._word_file_path))
            count = doc.ComputeStatistics(2)
            return count
        except Exception as e:
            print("Error:", e)

    def get_word_table(self):
        word = self._word
        doc = word.Documents.Open(os.path.abspath(self._word_file_path))
        table_of_contents = doc.TablesOfContents
        if table_of_contents.Count > 0:
            toc = table_of_contents(1)
            info_list = []
            for entry in toc.Range.Paragraphs:
                info_list.append(entry.Range.Text.strip())
            return info_list
        else:
            return None
