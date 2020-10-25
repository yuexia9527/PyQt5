# -*- coding: utf-8 -*-

##  GUI应用程序主程序入口

import sys
from PyQt5.QtWidgets import QApplication
from myMainWindow import Pyqt5_Serial
import matplotlib.pyplot as plt
import numpy as np
import time

def extract_array():

    file = open("Magnetic positioning.txt", "r")
    list_arr = file.readlines() #读取数据文件的每一行

    lists = [] #生成列表

    for index, x in enumerate(list_arr):
        x = x.strip()
        x = x[:-1]
        x = x.strip('[]')
        x = x.split(", ")
        lists.append(x)
    array = np.array(lists)
    array = array.astype(float)

    return array


def plt_show(array):

    for index, a in enumerate(array):

        fig = plt.figure()
        ax = fig.gca(projection='3d')

        # Make the grid
        x = np.array([a[0]])
        print(x)
        y = np.array([a[1]])
        z = np.array([a[2]])  # 坐标点（x,y,z）

        # Make the direction data for the arrows
        u = np.array([a[3]])
        v = np.array([a[4]])
        w = np.array([a[5]])  # 方向（u,v,w）

        ax.quiver(x, y, z, u, v, w, length=0.2, normalize=True)  # 模长设置为1
        #设置坐标系的显示范围
        ax.set_xlim(-0.1, 0.1)
        ax.set_ylim(-0.1, 0.1)
        ax.set_zlim(-1, 1)
        plt.show()
        time.sleep(0.1)


if __name__ == '__main__':

    app = QApplication(sys.argv)  # 创建GUI应用程序

    mainform = Pyqt5_Serial()  # 创建主窗体

    mainform.show()  # 显示主窗体

    # mainform.iren.Initialize()  # Need this line to actually show the render inside Qt

    sys.exit(app.exec_())

    # 数据读取与可视化
    array = extract_array()
    plt_show(array)

    # 异常获取模块
    _oldExceptionCatch = sys.excepthook
    def _exceptionCatch(exceptionType, value, traceback):
        _oldExceptionCatch(exceptionType, value, traceback)
    # 由于Qt界面中的异常捕获不到
    # 把系统的全局异常获取函数进行重定向
    sys.excepthook = _exceptionCatch