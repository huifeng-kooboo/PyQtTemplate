from widgets.base_widget import BaseWidget
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from configs.settings import TITLE_NAME
from widgets.components.base_button import BaseButton,ButtonType, ButtonSize


class MainWidget(BaseWidget):
    '''
    主窗体程序 主程序部分
    '''
    def __init__(self, parent=None):
        super(MainWidget,self).__init__(parent=parent)
        self.__init_ui()
        self.__init_style()
        self.__init_signals()
        self.__init_others()

    def __init_ui(self):
        """
        初始化UI：主要是控件的增加以及总体的布局
        :return:
        """
        # 设置窗体最小大小
        self.setMinimumSize(QSize(800, 800))
        # 设置窗口标题
        self.setWindowTitle(TITLE_NAME)
        # 总体布局设置成VBoxLayOut
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)

        # 添加标题左侧----有光推流客户端 右侧---->有光号
        hbox_layout = QHBoxLayout()
        self.layout.addLayout(hbox_layout,0)

        title_label = QLabel()
        title_label.setText(TITLE_NAME)
        title_label.setFixedHeight(30)
        title_label.setFixedWidth(200)
        self.__yg_number = '000000'  # 有光号
        self.ui_youguang_number_label = QLabel()  # 有光的ui_label控件
        self.ui_youguang_number_label.setText(f"有光号:{self.__yg_number}")
        self.ui_youguang_number_label.setFixedHeight(30)
        self.ui_youguang_number_label.setFixedWidth(200)

        hbox_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        # # 添加label
        hbox_layout.addStretch(5)
        hbox_layout.addWidget(title_label)
        hbox_layout.addStretch(20)
        hbox_layout.addWidget(self.ui_youguang_number_label)
        hbox_layout.addStretch(5)

        # hbox_layout.setGeometry(QRect=QRect(12,12,11,22))

        # 设备推流，屏幕捕捉， 多媒体文件推流 按钮增加
        self.tool_button_group = QButtonGroup()
        button_hbox_layout = QHBoxLayout()
        self.layout.addLayout(button_hbox_layout,20)
        button_hbox_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # 创建三个按钮
        device_plug_button = BaseButton()
        device_plug_button.init_button(title="设备推流", icon="", button_type=ButtonType.BUTTON_PRIMARY)
        device_plug_button.set_button_size(ButtonSize.NORMAL_SIZE)
        screen_capture_button = BaseButton()
        screen_capture_button.init_button(title="屏幕捕捉", icon="", button_type=ButtonType.BUTTON_SUCCESS)
        screen_capture_button.set_button_size(ButtonSize.NORMAL_SIZE)
        media_file_button = BaseButton()
        media_file_button.init_button(title="多媒体文件推流", icon="", button_type=ButtonType.BUTTON_DANGER)
        media_file_button.set_button_size(ButtonSize.NORMAL_SIZE)
        media_file_button.setDisabled(True)

        button_hbox_layout.addStretch(15)
        button_hbox_layout.addWidget(device_plug_button)
        button_hbox_layout.addStretch(10)
        button_hbox_layout.addWidget(screen_capture_button)
        button_hbox_layout.addStretch(10)
        button_hbox_layout.addWidget(media_file_button)
        button_hbox_layout.addStretch(15)


        # 添加group
        self.tool_button_group.addButton(device_plug_button)
        self.tool_button_group.addButton(screen_capture_button)
        self.tool_button_group.addButton(media_file_button)

        # # 预览Layout
        # preview_hbox_layout = QHBoxLayout()
        # self.layout.addLayout(preview_hbox_layout,5)



    def __init_style(self):
        """
        初始化样式QSS
        :return:
        """
        # 设置工具按钮的图片大小
        for button in self.tool_button_group.buttons():
            button.setStyleSheet(button.styleSheet() + "QPushButton{font:12px;}")

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
