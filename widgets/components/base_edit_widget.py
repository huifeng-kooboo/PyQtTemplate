# 标准的输入框模块

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class BaseEditWidget(QLineEdit):
    """
    标准的输入框样式
    """

    def __init__(self, parent=None):
        super(QLineEdit, self).__init__(parent=parent)
        self.__init_ui()
        self.__init_style()
        self.__init_signals()
        self.__init_others()

    def __init_ui(self):
        pass

    def __init_style(self):
        # tip color :170, 171, 179
        self.setStyleSheet("QLineEdit{ background-color:rgb(42, 45, 66); color: white;"
                           "border-radius: 3px; font: 12px; padding-left: 8px;}")
        pass

    def __init_signals(self):
        pass

    def __init_others(self):
        pass
