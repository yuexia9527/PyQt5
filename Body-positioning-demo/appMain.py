# -*- coding: utf-8 -*-

##  GUI应用程序主程序入口

import sys
from PyQt5.QtWidgets import QApplication
from myMainWindow import Pyqt5_Serial
import matplotlib.pyplot as plt
import numpy as np
import time

if __name__ == '__main__':

    #主程序应用
    app = QApplication(sys.argv)  # 创建GUI应用程序
    #串口调试窗口
    mainform = Pyqt5_Serial()  # 创建主窗体
    mainform.show()  # 显示主窗体
    #VTK3D显示窗口
    sys.exit(app.exec_())


    # 异常获取模块
    _oldExceptionCatch = sys.excepthook
    def _exceptionCatch(exceptionType, value, traceback):
        _oldExceptionCatch(exceptionType, value, traceback)
    # 由于Qt界面中的异常捕获不到
    # 把系统的全局异常获取函数进行重定向
    sys.excepthook = _exceptionCatch