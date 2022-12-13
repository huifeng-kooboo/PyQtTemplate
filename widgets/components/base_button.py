from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from widgets.ui_types import ButtonType, ButtonSize
from widgets.components.styles.button_style import ButtonStyle


class BaseButton(QPushButton):
    """
    基础的按钮控件基类
    """

    def __init__(self, *args):
        super(BaseButton, self).__init__(*args)

    def init_button(self, title: str = "", icon: str = "", button_type: ButtonType = ButtonType.BUTTON_NONE):
        """
        初始化按钮 [默认圆角10px]
        :param title: 标题
        :param icon: icon图标
        :param button_type: 按钮类型
        :return:
        """
        if title != "":
            self.setText(title)
        if icon != "":
            self.setIcon(QIcon(icon))
        if button_type == ButtonType.BUTTON_NONE:
            pass
        else:
            style_sheet = ButtonStyle.get_style_sheet(button_type)
            self.setStyleSheet(self.styleSheet()+style_sheet)

    def set_radius(self, radius: int):
        """
        设置Radius圆角
        :param radius:
        :return:
        """
        style_ = "QPushButton { border-radius: %1px;}"
        self.setStyleSheet(self.styleSheet() + style_.replace("%1",str(radius)))

    def set_button_size(self, button_size: ButtonSize):
        self.setFixedSize(ButtonStyle.get_button_size(button_size))
