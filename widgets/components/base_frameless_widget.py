import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import *


class BaseFramelessWidget(QWidget):
    """
    无边框的窗体基类
    """
    __start_pos = None
    __end_pos = None
    __is_tracking = False
    __is_need_move = True

    def __init__(self, parent=None):
        """
        窗体初始化操作:
        顺序 UI----样式----信号----剩余部分
        :param parent:
        """
        super(BaseFramelessWidget, self).__init__(parent=parent)
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
        self.setStyleSheet("QWidget{background-color:white; font: 18px; font-weight:bold; }")
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
        # 设置无边框状态
        self.setWindowFlag(Qt.FramelessWindowHint)

    def set_is_need_move(self, is_need: bool):
        """
        是否允许移动
        """
        self.__is_need_move = is_need

    def mouseMoveEvent(self, event_: QMouseEvent):
        if not self.__is_need_move:
            return
        if self.__is_tracking == True:
            self.__end_pos = event_.pos() - self.__start_pos
            self.move(self.pos() + self.__end_pos)

    def mousePressEvent(self, event_: QMouseEvent):
        if not self.__is_need_move:
            return
        if event_.button() == Qt.LeftButton:
            self.__is_tracking = True
            self.__start_pos = QPoint(event_.x(), event_.y())

    def mouseReleaseEvent(self, event_: QMouseEvent):
        if not self.__is_need_move:
            return
        if event_.button() == Qt.LeftButton:
            self.__is_tracking = False
            self.__start_pos = None
            self.__end_pos = None


if __name__ == '__main__':
    # 测试功能
    app = QApplication(sys.argv)
    widget = BaseFramelessWidget()
    widget.setFixedSize(200, 300)
    widget.show()
    sys.exit(app.exec_())
