from widgets.base_widget import BaseWidget
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from configs.settings import TITLE_NAME
from widgets.components.base_button import BaseButton,ButtonType, ButtonSize
from utils.time_utils import TimeUtils, datetime
import random


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
        
        
        # 标题----》我的物品
        hbox_layout = QHBoxLayout()
        self.layout.addLayout(hbox_layout,0)
        title = f"全部的电子产品"
        self.title_label = QLabel()
        self.title_label.setText(title)
        self.title_label.setFixedHeight(30)
        self.title_label.setFixedWidth(200)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        hbox_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        hbox_layout.addStretch(5)
        hbox_layout.addWidget(self.title_label)
        hbox_layout.addStretch(5)

        # 设备推流，屏幕捕捉， 多媒体文件推流 按钮增加
        self.tool_button_group = QButtonGroup()
        button_hbox_layout = QHBoxLayout()
        self.layout.addLayout(button_hbox_layout,20)
        button_hbox_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        
        button_hbox_layout = QHBoxLayout()
        self.layout.addLayout(button_hbox_layout,20)
        button_hbox_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
                # listWidget 存放按钮
                
        tool_list_hbox_layout = QHBoxLayout()
        self.layout.addLayout(tool_list_hbox_layout,20)
        self.tool_list_widget = QListWidget()
        self.tool_list_widget.setFlow(QListView.Flow.LeftToRight)
        self.tool_list_widget.setViewMode(QListView.ViewMode.IconMode)
        # self.tool_list_widget.setStyleSheet("QListWidgetItem{}")
        for i in range(0,10):
            list_widget_item = QListWidgetItem()
            list_widget_item.setText(f"122{i}adaaaa")
            tool_btn = BaseButton()
            tool_btn.init_button("测试","",ButtonType.BUTTON_INFO)
            tool_btn.set_radius(0)
            # tool_btn.setStyleSheet(tool_btn.styleSheet() + "QPushButton{border-color: red; border: 10px;}")
            tool_btn.setMinimumWidth(300)
            self.tool_list_widget.addItem(list_widget_item)
            self.tool_list_widget.setItemWidget(list_widget_item,tool_btn)
        tool_list_hbox_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        tool_list_hbox_layout.addWidget(self.tool_list_widget)




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
