import sys
from utils.log import g_log
from configs.settings import APP_NAME
from PyQt5 import QtWidgets
from widgets.main_widget import MainWidget


def start_app(app_name: str):
    '''
    启动相关的App
    :param app_name: 程序名称
    :return:
    '''
    if app_name == APP_NAME:
        g_log.info(f"启动{APP_NAME}客户端")
        app = QtWidgets.QApplication([""])
        widget = MainWidget()
        widget.show()
        ret = app.exec_()
        sys.exit(ret)


if __name__ == '__main__':
    g_log.info("exe start")
    try:
        start_app(app_name=APP_NAME)
    except Exception:
        g_log.error("exe stop abnormal...")
    g_log.info('exe end')
