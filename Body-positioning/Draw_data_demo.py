# -*- coding: utf-8 -*-
'''
TODO:LQD
'''
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FC
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QVBoxLayout, QWidget
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer

class QtDraw(QMainWindow):

    # flag_btn_start = True

    def __init__(self):
        super(QtDraw, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(800, 600)
        self.setWindowTitle('PyQt5 Draw')

        # TODO:这里是结合的关键
        self.fig = plt.Figure()
        self.canvas = FC(self.fig)
        # self.btn_start = QPushButton(self)
        # self.btn_start.setText('draw')
        # self.btn_start.clicked.connect(self.slot_start)

        # 定时器绘制数据
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.slot_start)
        self.timer.start()

        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        # layout.addWidget(self.btn_start)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    #提取数据
    def extract_array(self):
        file = open("Data.txt", "r")
        list_arr = file.readlines()  # 读取数据文件的每一行
        lists = []  # 生成列表

        for index, x in enumerate(list_arr[3:-3]):
            x = x.strip()
            if x != "":
                x = x[5:]
                x = x.strip('[]')
                x = x.split(" ")
                lists.append(x)
        array = np.array(lists)
        array = array.astype(int)

        return array

    def slot_start(self):
        try:
            array = self.extract_array()
            ax = self.fig.add_subplot(111)
            ax.cla()  # TODO:删除原图，让画布上只有新的一次的图
            for i in range(array.shape[1]):
                ax.plot(array[:, i])
            self.canvas.draw()  # TODO:这里开始绘制
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # 异常获取模块
    _oldExceptionCatch = sys.excepthook

    def _exceptionCatch(exceptionType, value, traceback):
        _oldExceptionCatch(exceptionType, value, traceback)

    # 由于Qt界面中的异常捕获不到
    # 把系统的全局异常获取函数进行重定向
    sys.excepthook = _exceptionCatch


    # QT显示模块
    app = QtWidgets.QApplication(sys.argv)
    myshow = QtDraw()
    myshow.show()
    sys.exit(app.exec_())
