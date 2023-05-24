from word_config import WordConfig
from gui import Gui


class Application:
    def __init__(self):
        self._window = Gui()
        self._word_config = WordConfig()
        self.window_bind_func()

    def window_bind_func(self):
        window = self._window
        word_config = self._word_config
        path = word_config.get_word_file_path()
        input_path = path + 'input.docx'
        output_path = path + 'output.pdf'

        def btn1_callback(event):
            window.new_top_level('转换成功')
            word_config.word_2_pdf(input_path, output_path)

        def btn2_callback(event):
            count = word_config.get_word_pages_count(input_path)
            window.new_top_level('该word文档的页数为：{}'.format(count))
        # 初始化 word 2 pdf 功能的按钮
        # window.set_word_2_pdf_btn(btn1_callback)
        # window.set_get_pages_btn(btn2_callback)

    def get_window(self):
        return self._window

    def get_word_config(self):
        return self._word_config

    def run(self):
        self._window.run()
