from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget


class BaseWidget(QWidget):
    """
    有边框的窗体基类
    """
    def __init__(self, parent=None):
        """
        窗体初始化操作:
        顺序 UI----样式----信号----剩余部分
        :param parent:
        """
        super(BaseWidget, self).__init__(parent=parent)
        self.__init_ui()
        self.__init_style()
        self.__init_signals()
        self.__init_others()

    def __init_ui(self):
        """
        初始化UI：主要是控件的增加
        :return:
        """
        pass

    def __init_style(self):
        """
        初始化样式
        :return:
        """
        # 全局样式设置
        self.setStyleSheet("QWidget{background-color:white; font: 18px; border: 0px; }")
        pass

    def __init_signals(self):
        """
        初始化信号
        :return:
        """
        pass

    def __init_others(self):
        """
        剩余部分初始化
        :return:
        """
        pass
