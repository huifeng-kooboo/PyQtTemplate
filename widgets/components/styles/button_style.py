from widgets.ui_types import ButtonType, ButtonSize
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


########## 按钮颜色配置 ##################################


class ButtonStyle:
    """
    按钮风格类
    """

    @staticmethod
    def get_style_sheet(button_type: ButtonType):
        '''
        获取基础样式表
        :param button_type:
        :return:
        '''
        if button_type == ButtonType.BUTTON_PRIMARY:
            return ButtonStyle._generate_style("rgb(64, 158, 255)", 'rgb(255, 255, 255)', 'rgb(121, 187, 255)',
                                               'rgb(255, 255, 255)',
                                               "rgb(51, 126, 204)", 'rgb(255, 255, 255)')
        elif button_type == ButtonType.BUTTON_INFO:
            return ButtonStyle._generate_style("rgb(64, 158, 255)", 'rgb(255, 255, 255)', 'rgb(121, 187, 255)',
                                               'rgb(255, 255, 255)',
                                               "rgb(51, 126, 204)", 'rgb(255, 255, 255)')
        elif button_type == ButtonType.BUTTON_DANGER:
            return ButtonStyle._generate_style("rgb(64, 158, 255)", 'rgb(255, 255, 255)', 'rgb(121, 187, 255)',
                                               'rgb(255, 255, 255)',
                                               "rgb(51, 126, 204)", 'rgb(255, 255, 255)')
        elif button_type == ButtonType.BUTTON_SUCCESS:
            return ButtonStyle._generate_style("rgb(64, 158, 255)", 'rgb(255, 255, 255)', 'rgb(121, 187, 255)',
                                               'rgb(255, 255, 255)',
                                               "rgb(51, 126, 204)", 'rgb(255, 255, 255)')
        elif button_type == ButtonType.BUTTON_WARNING:
            return ButtonStyle._generate_style("rgb(64, 158, 255)", 'rgb(255, 255, 255)', 'rgb(121, 187, 255)',
                                               'rgb(255, 255, 255)',
                                               "rgb(51, 126, 204)", 'rgb(255, 255, 255)')

    @staticmethod
    def get_button_size(button_size: ButtonSize):
        '''
        获取按钮大小参数
        :param button_size:目前提供了MINI，NORMAL，LARGE三个选项，可以自己扩展.....
        :return:
        '''
        if button_size == ButtonSize.MINI_SIZE:
            return QSize(50, 60)
        elif button_size == ButtonSize.NORMAL_SIZE:
            return QSize(180, 30)
        elif button_size == ButtonSize.LARGE_SIZE:
            return QSize(200, 100)

    @staticmethod
    def _generate_style(background_color: str, color: str, hover_background_color: str = "", hover_color: str = "",
                        pressed_background_color: str = "", pressed_color: str = ""):
        '''
        生成ButtonStyleSheet
        :param background_color:
        :param color:
        :param hover_background_color:
        :param hover_color:
        :param pressed_background_color:
        :param pressed_color:
        :return:
        '''
        style_sheet = "QPushButton{background-color: %1; color: %2 ; border-radius: 5px;}"
        style_ = style_sheet.replace("%1", background_color).replace("%2", color)
        if hover_background_color != "" and hover_color != "":
            style_sheet_hover = "QPushButton:hover {background-color: %1; color: %2 }"
            style_hover = style_sheet_hover.replace("%1", hover_background_color).replace("%2", hover_color)
            style_ += style_hover

        if pressed_background_color != "" and pressed_color != "":
            style_sheet_pressed = "QPushButton:pressed {background-color: %1; color: %2 }"
            style_pressed = style_sheet_pressed.replace("%1", pressed_background_color).replace("%2", pressed_color)
            style_ += style_pressed

        return style_
