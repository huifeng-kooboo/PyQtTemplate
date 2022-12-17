from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class BaseToolButton(QToolButton):
    def __init__(self, *args):
        super(BaseToolButton, self).__init__(*args)
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
        self.setStyleSheet("QToolButton{background-color:white; font: 18px; font-weight:bold; }")
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
