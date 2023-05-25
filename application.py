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
                self.show_info_window('转换成功') if word_config.word_2_pdf() else self.show_info_window('操作取消')
            else:
                self.show_info_window('请先选择一个文档')

        def btn2_callback(event):
            if word_config.word_is_open:
                count = word_config.get_word_pages_count()
                self.show_info_window('该word文档的页数为：{}'.format(count))
            else:
                self.show_info_window('请先选择一个文档')

        def btn3_callback(event):
            if word_config.word_is_open:
                table_info_list = word_config.get_word_table()
                self.show_info_list_window('文档目录', table_info_list) if table_info_list \
                    else self.show_info_window('该文档无目录')
            else:
                self.show_info_window('请先选择一个文档')

        window.set_load_file_btn(word_config.open_file)
        window.set_word_2_pdf_btn(btn1_callback)
        window.set_get_pages_btn(btn2_callback)
        window.set_directory_btn(btn3_callback)

    def show_info_window(self, info):
        self._window.new_top_level(info)

    def show_info_list_window(self, title, info_list):
        self._window.new_top_level_for_list(title, info_list)

    def get_window(self):
        return self._window

    def get_word_config(self):
        return self._word_config

    def run(self):
        self._window.run()
