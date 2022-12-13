# 通用日志类
import logging
import os
import time


__all__ = {
    'g_log'
}

g_log = logging.getLogger()
g_log.setLevel(logging.DEBUG)
rq = "plug_flow_" + time.strftime('%Y%m%d', time.localtime(time.time()))
log_path = 'logs/'
if not os.path.exists(log_path):
    os.mkdir(log_path)
log_name = log_path + rq + '.log'
fh = logging.FileHandler(log_name, mode='a+')
fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
formatter = logging.Formatter(
    "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
g_log.addHandler(fh)
