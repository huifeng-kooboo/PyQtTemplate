from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from widgets.components.ui_types import ButtonType, ButtonSize, BorderStyle
from widgets.components.styles.button_style import ButtonStyle


class BaseSlider(QSlider):
    """
    基础滑动条组件
    """
    def __init__(self, *args):
        super(BaseSlider, self).__init__(*args)
        self.__init_ui()
        self.__init_style()
        self.__init_signals()
        self.__init_others()

    def set_slider_direction(self, dir_ :int):
        """
        设置Slider方向: 0：水平 1：垂直
        """
        if dir_ == 0:
            self.setOrientation(Qt.Horizontal)
        else:
            self.setOrientation(Qt.Vertical)

    def __init_ui(self):
        pass

    def __init_style(self):
        pass

    def __init_signals(self):
        pass

    def __init_others(self):
        pass