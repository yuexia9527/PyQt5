# Author: yuxiang wang
# Date:2020-11-25

import sys
import vtk
import serial
import threading
import numpy as np
import serial.tools.list_ports
import matplotlib.pyplot as plt
from PyQt5.QtCore import QTimer
from ui_MainWindow import Ui_Form
from PyQt5.QtWebEngineWidgets import *
from mpl_toolkits.mplot3d import Axes3D
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FC
import time
import psutil
import traceback
import pyqtgraph as pg
import matplotlib as mpl
import matplotlib.style as mplStyle  # 一个模块
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from matplotlib.backends.backend_qt5agg import (FigureCanvas,
                                                NavigationToolbar2QT as NavigationToolbar)


class Pyqt5_Serial(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(Pyqt5_Serial, self).__init__()
        self.ui = Ui_Form()
        self.setupUi(self)
        self.init()
        self.setWindowTitle("人体姿态信息显示助手")
        self.ser = serial.Serial()
        self.port_check()

        # 接收数据和发送数据数目置零
        self.data_num_received = 0
        self.lineEdit.setText(str(self.data_num_received))
        self.data_num_sended = 0
        self.lineEdit_2.setText(str(self.data_num_sended))

        # 将需要保存的数据清空
        self.Data = ''

    def init(self):

        # 设置主窗口图标
        self.setWindowIcon(QtGui.QIcon('./QtApp/images/11.ico'))

        # 设置主窗口的位置
        self.setGeometry(200, 120, 1500, 800)

        # 串口检测按钮
        self.s1__box_1.clicked.connect(self.port_check)

        # 串口信息显示
        self.s1__box_2.currentTextChanged.connect(self.port_imf)

        # 打开串口按钮
        self.open_button.clicked.connect(self.port_open)

        # 关闭串口按钮
        self.close_button.clicked.connect(self.port_close)

        # 发送数据按钮
        self.s3__send_button.clicked.connect(self.data_send)

        # 定时发送数据
        self.timer_send = QTimer()
        self.timer_send.timeout.connect(self.data_send)
        self.timer_send_cb.stateChanged.connect(self.data_send_timer)

        # 定时器接收数据
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.data_receive)

        # 清除发送窗口
        self.s3__clear_button.clicked.connect(self.send_data_clear)

        # 清除接收窗口
        self.s2__clear_button.clicked.connect(self.receive_data_clear)

        # 绘制CPU使用率曲线
        self.Draw_data()

    # 串口检测
    def port_check(self):
        # 检测所有存在的串口，将信息存储在字典中
        self.Com_Dict = {}
        port_list = list(serial.tools.list_ports.comports())
        self.s1__box_2.clear()
        for port in port_list:
            self.Com_Dict["%s" % port[0]] = "%s" % port[1]
            self.s1__box_2.addItem(port[0])
        if len(self.Com_Dict) == 0:
            self.state_label.setText(" 无串口")

    # 串口信息
    def port_imf(self):
        # 显示选定的串口的详细信息
        imf_s = self.s1__box_2.currentText()
        if imf_s != "":
            self.state_label.setText(self.Com_Dict[self.s1__box_2.currentText()])

    # 打开串口
    def port_open(self):
        self.ser.port = self.s1__box_2.currentText()
        self.ser.baudrate = int(self.s1__box_3.currentText())
        self.ser.bytesize = int(self.s1__box_4.currentText())
        self.ser.stopbits = int(self.s1__box_6.currentText())
        self.ser.parity = self.s1__box_5.currentText()

        try:
            self.ser.open()
        except:
            QMessageBox.critical(self, "Port Error", "此串口不能被打开！")
            return None

        # 打开串口接收定时器，周期为2ms
        self.timer.start(0.1)

        if self.ser.isOpen():
            self.open_button.setEnabled(False)
            self.close_button.setEnabled(True)
            self.formGroupBox1.setTitle("串口状态（已开启）")

    # 关闭串口
    def port_close(self):
        self.timer.stop()
        self.timer_send.stop()
        try:
            self.ser.close()
        except:
            pass
        self.open_button.setEnabled(True)
        self.close_button.setEnabled(False)
        self.lineEdit_3.setEnabled(True)
        # 接收数据和发送数据数目置零
        self.data_num_received = 0
        self.lineEdit.setText(str(self.data_num_received))
        self.data_num_sended = 0
        self.lineEdit_2.setText(str(self.data_num_sended))
        self.formGroupBox1.setTitle("串口状态（已关闭）")

    # 发送数据
    def data_send(self):
        if self.ser.isOpen():
            # 读取发送端信息
            input_s = self.s3__send_text.toPlainText()
            if input_s != "":
                # 非空字符串
                if self.hex_send.isChecked():
                    # hex发送
                    input_s = input_s.strip()
                    send_list = []
                    while input_s != '':
                        try:
                            num = int(input_s[0:2], 16)
                        except ValueError:
                            QMessageBox.critical(self, 'wrong data', '请输入十六进制数据，以空格分开!')
                            return None
                        input_s = input_s[2:].strip()
                        send_list.append(num)
                    input_s = bytes(send_list)
                else:
                    # ascii发送
                    input_s = (input_s + '\r\n').encode('utf-8')

                num = self.ser.write(input_s)
                self.data_num_sended += num
                self.lineEdit_2.setText(str(self.data_num_sended))
        else:
            pass

    # 接收数据并将数据以字符串out_s的形式显示并保存在Data.txt中
    def data_receive(self):
        try:
            num = self.ser.inWaiting()
        except:
            self.port_close()
            return None
        if num > 0:
            data = self.ser.read(num)
            num = len(data)
            # hex显示
            if self.hex_receive.checkState():
                out_s = ''
                for i in range(0, len(data)):
                    out_s = out_s + '{:02X}'.format(data[i]) + ' '
                self.s2__receive_text.insertPlainText(out_s)
                self.save_data(out_s)
            else:
                # 串口接收到的字符串为b'123',要转化成unicode字符串才能输出到窗口中去
                self.s2__receive_text.insertPlainText(data.decode('iso-8859-1'))
                out_s = data.decode('iso-8859-1')
                self.save_data(out_s)
            # 统计接收字符的数量
            self.data_num_received += num
            self.lineEdit.setText(str(self.data_num_received))

            # 获取到text光标
            textCursor = self.s2__receive_text.textCursor()
            # 滚动到底部
            textCursor.movePosition(textCursor.End)
            # 设置光标到text中去
            self.s2__receive_text.setTextCursor(textCursor)
        else:
            pass

    # 定时发送数据
    def data_send_timer(self):
        if self.timer_send_cb.isChecked():
            self.timer_send.start(int(self.lineEdit_3.text()))
            self.lineEdit_3.setEnabled(False)
        else:
            self.timer_send.stop()
            self.lineEdit_3.setEnabled(True)

    # 清除显示
    def send_data_clear(self):
        self.s3__send_text.setText("")

    def receive_data_clear(self):
        self.s2__receive_text.setText("")

    # 用matplotlib绘制Data的主程序
    def Draw_data(self):
        # TODO:这里是结合的关键
        self.fig1 = plt.Figure()
        self.canvas1 = FC(self.fig1)
        self.fig2 = plt.Figure()
        self.canvas2 = FC(self.fig2)

        # 定时器绘制数据
        self.timer_draw = QTimer(self)
        self.timer_draw.timeout.connect(self.plot_start)
        self.timer_draw.start(0.1)

        # 定时器绘制数据
        self.timer_draw_3d = QTimer(self)
        self.timer_draw_3d.timeout.connect(self.pose_estimation_3d)
        self.timer_draw_3d.start(0.1)

        layout1 = QVBoxLayout()
        layout1.addWidget(self.canvas1)
        self.centralWidget1.setLayout(layout1)
        layout2 = QVBoxLayout()
        layout2.addWidget(self.canvas2)
        self.centralWidget2.setLayout(layout2)
        self.plot_start()

    # 从保存的Data.txt文件中提取数据
    def extract_array(self):
        file = open("Data.txt", "r")
        list_arr = file.readlines()  # 读取数据文件的每一行
        lists = []  # 生成列表
        for index, x in enumerate(list_arr[-43:-3]):
            x = x.strip()
            if x != "":
                x = x[5:-1]
                x = x.strip('[]')
                x = x.split(",")
                lists.append(x)
        array = np.array(lists)
        array = array.astype(int)
        return array

    # 图像的绘制与更新
    def plot_start(self):
        try:
            array = self.extract_array()
            # 自动选择需要显示的通道，0为显示全部，共有13个通道
            self.channel_choose = int(self.comboBox.currentText())
            ax = self.fig1.add_subplot(111)
            ax.cla()  # TODO:删除原图，让画布上只有新的一次的图
            for i in range(array.shape[1]):
                if self.channel_choose == 0:
                    ax.plot(array[:, i])
                else:
                    ax.plot(array[:, self.channel_choose - 1])
            self.canvas1.draw()  # TODO:这里开始绘制
        except Exception as e:
            pass

    # 3d图像的绘制与更新
    def pose_estimation_3d(self):
        try:
            # 加载外部的web界面
            self.browser.load(QUrl('https://www.baidu.com'))
        except Exception as e:
            pass

    # 将串口获取到的out_s保存到Data.txt
    def save_data(self, contents):
        self.Data += contents
        # print(self.Data)
        fh = open('Data.txt', 'w')
        fh.write(self.Data)
        fh.close()


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
    myshow = Pyqt5_Serial()
    myshow.show()

    add_thread1 = threading.Thread(target=Pyqt5_Serial().data_receive())
    add_thread1.start()
    add_thread2 = threading.Thread(target=Pyqt5_Serial().extract_array())
    add_thread2.start()
    add_thread3 = threading.Thread(target=Pyqt5_Serial().plot_start())
    add_thread3.start()
    add_thread4 = threading.Thread(target=Pyqt5_Serial().plot_start_3d())
    add_thread4.start()

    sys.exit(app.exec_())
