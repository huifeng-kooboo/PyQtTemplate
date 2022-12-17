from widgets.components.ui_types import ButtonType, ButtonSize
from PyQt5.QtCore import *

########## 按钮颜色配置 ##################################


# 样式参考： https://element-plus.gitee.io/zh-CN/component/button.html#%E5%9F%BA%E7%A1%80%E7%94%A8%E6%B3%95


########## 按钮颜色配置 ##################################

# primary 按钮状态
PRIMARY_NORMAL_BACKGROUND_COLOR = "rgb(64, 158, 255)"
PRIMARY_NORMAL_COLOR = "rgb(255, 255, 255)"
PRIMARY_HOVER_BACKGROUND_COLOR = "rgb(121, 187, 255)"
PRIMARY_HOVER_COLOR = "rgb(255, 255, 255)"
PRIMARY_PRESSED_BACKGROUND_COLOR = "rgb(51, 126, 204)"
PRIMARY_PRESSED_COLOR = "rgb(255, 255, 255)"
PRIMARY_DISABLED_BACKGROUND_COLOR = "#92C4FF"
PRIMARY_DISABLED_COLOR = "rgb(255, 255, 255)"

# success 按钮状态 7E8187
SUCCESS_NORMAL_BACKGROUND_COLOR = "#5FB822"
SUCCESS_NORMAL_COLOR = "rgb(255, 255, 255)"
SUCCESS_HOVER_BACKGROUND_COLOR = "#447E1E"
SUCCESS_HOVER_COLOR = "rgb(255, 255, 255)"
SUCCESS_PRESSED_BACKGROUND_COLOR = "#7AC648"
SUCCESS_PRESSED_COLOR = "rgb(255, 255, 255)"
SUCCESS_DISABLED_BACKGROUND_COLOR = "#A9DC88"
SUCCESS_DISABLED_COLOR = "rgb(255, 255, 255)"

# info 按钮
INFO_NORMAL_BACKGROUND_COLOR = "#7E8187"
INFO_NORMAL_COLOR = "rgb(255, 255, 255)"
INFO_HOVER_BACKGROUND_COLOR = "#585A5E"
INFO_HOVER_COLOR = "rgb(255, 255, 255)"
INFO_PRESSED_BACKGROUND_COLOR = "#95999D"
INFO_PRESSED_COLOR = "rgb(255, 255, 255)"
INFO_DISABLED_BACKGROUND_COLOR = "#BCBDC1"
INFO_DISABLED_COLOR = "rgb(255, 255, 255)"

# warning 按钮
WARNING_NORMAL_BACKGROUND_COLOR = "#DC9027"
WARNING_NORMAL_COLOR = "rgb(255, 255, 255)"
WARNING_HOVER_BACKGROUND_COLOR = "#946320"
WARNING_HOVER_COLOR = "rgb(255, 255, 255)"
WARNING_PRESSED_BACKGROUND_COLOR = "#E3A54C"
WARNING_PRESSED_COLOR = "rgb(255, 255, 255)"
WARNING_DISABLED_BACKGROUND_COLOR = "#EEC68A"
WARNING_DISABLED_COLOR = "rgb(255, 255, 255)"

# danger 按钮
DANGER_NORMAL_BACKGROUND_COLOR = "#EB5359"
DANGER_NORMAL_COLOR = "rgb(255, 255, 255)"
DANGER_HOVER_BACKGROUND_COLOR = "#9E3D40"
DANGER_HOVER_COLOR = "rgb(255, 255, 255)"
DANGER_PRESSED_BACKGROUND_COLOR = "#EE7276"
DANGER_PRESSED_COLOR = "rgb(255, 255, 255)"
DANGER_DISABLED_BACKGROUND_COLOR = "#F4A5A7"
DANGER_DISABLED_COLOR = "rgb(255, 255, 255)"


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
            return ButtonStyle._generate_style(PRIMARY_NORMAL_BACKGROUND_COLOR, PRIMARY_NORMAL_COLOR,
                                               PRIMARY_HOVER_BACKGROUND_COLOR, PRIMARY_HOVER_COLOR,
                                               PRIMARY_PRESSED_BACKGROUND_COLOR, PRIMARY_HOVER_COLOR,
                                               PRIMARY_DISABLED_BACKGROUND_COLOR, PRIMARY_DISABLED_COLOR)
        elif button_type == ButtonType.BUTTON_INFO:
            return ButtonStyle._generate_style(INFO_NORMAL_BACKGROUND_COLOR, INFO_NORMAL_COLOR,
                                               INFO_HOVER_BACKGROUND_COLOR, INFO_HOVER_COLOR,
                                               INFO_PRESSED_BACKGROUND_COLOR, INFO_HOVER_COLOR,
                                               INFO_DISABLED_BACKGROUND_COLOR, INFO_DISABLED_COLOR)
        elif button_type == ButtonType.BUTTON_DANGER:
            return ButtonStyle._generate_style(DANGER_NORMAL_BACKGROUND_COLOR, DANGER_NORMAL_COLOR,
                                               DANGER_HOVER_BACKGROUND_COLOR, DANGER_HOVER_COLOR,
                                               DANGER_PRESSED_BACKGROUND_COLOR, DANGER_HOVER_COLOR,
                                               DANGER_DISABLED_BACKGROUND_COLOR, DANGER_DISABLED_COLOR)
        elif button_type == ButtonType.BUTTON_SUCCESS:
            return ButtonStyle._generate_style(SUCCESS_NORMAL_BACKGROUND_COLOR, SUCCESS_NORMAL_COLOR,
                                               SUCCESS_HOVER_BACKGROUND_COLOR, SUCCESS_HOVER_COLOR,
                                               SUCCESS_PRESSED_BACKGROUND_COLOR, SUCCESS_HOVER_COLOR,
                                               SUCCESS_DISABLED_BACKGROUND_COLOR, SUCCESS_DISABLED_COLOR)
        elif button_type == ButtonType.BUTTON_WARNING:
            return ButtonStyle._generate_style(WARNING_NORMAL_BACKGROUND_COLOR, WARNING_NORMAL_COLOR,
                                               WARNING_HOVER_BACKGROUND_COLOR, WARNING_HOVER_COLOR,
                                               WARNING_PRESSED_BACKGROUND_COLOR, WARNING_HOVER_COLOR,
                                               WARNING_DISABLED_BACKGROUND_COLOR, WARNING_DISABLED_COLOR)

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
                        pressed_background_color: str = "", pressed_color: str = "",
                        disabled_background_color: str = "",
                        disabled_color: str = "",
                        checked_background_color: str= "",
                        checked_color: str = "",
                        unchecked_background_color: str= "",
                        unchecked_color: str = "",):
        """生成样式表
        Args:
            background_color (str): _description_
            color (str): _description_
            hover_background_color (str, optional): _description_. Defaults to "".
            hover_color (str, optional): _description_. Defaults to "".
            pressed_background_color (str, optional): _description_. Defaults to "".
            pressed_color (str, optional): _description_. Defaults to "".
            disabled_background_color (str, optional): _description_. Defaults to "".
            disabled_color (str, optional): _description_. Defaults to "".
        Returns:
            _type_: _description_
        """
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

        if disabled_background_color != "" and disabled_color != "":
            style_sheet_disabled = "QPushButton:disabled {background-color: %1; color: %2 }"
            style_disabled = style_sheet_disabled.replace("%1", disabled_background_color).replace("%2", disabled_color)
            style_ += style_disabled

        if  checked_color != "" and checked_background_color != "":
            style_sheet_checked = "QPushButton:checked {background-color: %1; color: %2 }"
            style_checked = style_sheet_checked.replace("%1", checked_background_color).replace("%2", checked_color)
            style_ += style_checked
        else:
            style_sheet_checked = "QPushButton:checked {background-color: %1; color: %2 }"
            style_checked = style_sheet_checked.replace("%1", pressed_background_color).replace("%2", pressed_color)
            style_ += style_checked

        if  unchecked_color != "" and unchecked_background_color != "":
            style_sheet_unchecked = "QPushButton:unchecked {background-color: %1; color: %2 }"
            style_unchecked = style_sheet_unchecked.replace("%1", unchecked_background_color).replace("%2", unchecked_color)
            style_ += style_unchecked
        else:
            style_sheet_unchecked = "QPushButton:unchecked {background-color: %1; color: %2 }"
            style_unchecked = style_sheet_unchecked.replace("%1", background_color).replace("%2", color)
            style_ += style_unchecked

        return style_