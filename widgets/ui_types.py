from enum import Enum, unique


@unique
class ButtonType(Enum):
    """
    按钮类型
    """
    BUTTON_NONE = 0
    BUTTON_PRIMARY = 1
    BUTTON_SUCCESS = 2
    BUTTON_INFO = 3
    BUTTON_WARNING = 4
    BUTTON_DANGER = 5


@unique
class ButtonSize(Enum):
    """
    按钮大小的枚举
    """
    NORMAL_SIZE = 0
    MINI_SIZE = 1
    LARGE_SIZE = 2