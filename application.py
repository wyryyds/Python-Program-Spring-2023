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

        def btn1_callback(event):
            if word_config.word_is_open:
                window.new_top_level('转换成功') if word_config.word_2_pdf() else window.new_top_level('操作取消')
            else:
                window.new_top_level('请先选择一个文档')

        def btn2_callback(event):
            if word_config.word_is_open:
                count = word_config.get_word_pages_count()
                window.new_top_level('该word文档的页数为：{}'.format(count))
            else:
                window.new_top_level('请先选择一个文档')

        window.set_load_file_btn(word_config.open_file)
        window.set_word_2_pdf_btn(btn1_callback)
        window.set_get_pages_btn(btn2_callback)

    def get_window(self):
        return self._window

    def get_word_config(self):
        return self._word_config

    def run(self):
        self._window.run()
