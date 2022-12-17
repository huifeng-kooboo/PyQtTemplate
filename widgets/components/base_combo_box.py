# 下拉框
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class BaseComboBox(QComboBox):
    def __init__(self, parent=None):
        super(QComboBox, self).__init__(parent=parent)
        self.__init_ui()
        self.__init_style()
        self.__init_signals()
        self.__init_others()

    def __init_ui(self):
        pass

    def __init_style(self):
        # tip color :170, 171, 179
        self.setStyleSheet("QComboBox{ background-color:rgb(42, 45, 66); color: white;"
                           "border-radius: 3px; font: 12px; height: 32px;padding-left: 8px;}"
                           "QComboBox QAbstractItemView {"
                           "outline: 0px;"
                           "height: 32px;"
                           "background-color:rgb(42, 45, 66);"
                           "color: white;"
                           "}"
                           "QComboBox QAbstractItemView::item {"
                           "background-color:rgb(42, 45, 66); "
                           "height: 32px;"
                           "}")
        # 标准框大小199，32
        self.setFixedSize(QSize(199,32))
        pass

    def __init_signals(self):
        pass

    def __init_others(self):
        pass