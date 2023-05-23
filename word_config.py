import os
import win32com.client


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

    def word_2_pdf(self, input_file, output_file):
        # 创建 Word 应用程序对象
        word = self._word
        word.Visible = False

        # 打开输入的 Word 文档
        doc = word.Documents.Open(input_file)

        # 将 Word 文档保存为 PDF
        doc.SaveAs(output_file, FileFormat=17)

        print('已将word文档转为pdf文档')

        # 关闭 Word 文档和应用程序
        # doc.Close()
        # word.Quit()

    def get_word_pages_count(self, filepath):
        try:
            word = self._word
            doc = word.Documents.Open(filepath)
            count = doc.ComputeStatistics(2)  # 2 表示统计页面数量
            doc.Close()
            word.Quit()
            return count
        except Exception as e:
            print("Error:", e)

