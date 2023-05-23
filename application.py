from window import Window
from word_config import WordConfig


class Application:
    def __init__(self):
        self._window = Window()
        self._word_config = WordConfig()
        self.window_bind_func()

    def window_bind_func(self):
        window = self._window
        word_config = self._word_config
        path = word_config.get_word_file_path()
        input_path = path + 'input.docx'
        output_path = path + 'output.pdf'
        # 初始化 word 2 pdf 功能的按钮
        window.set_word_2_pdf_button(word_config.word_2_pdf(input_path,output_path))

    def get_window(self):
        return self._window

    def get_word_config(self):
        return self._word_config

    def run(self):
        self._window.run()
