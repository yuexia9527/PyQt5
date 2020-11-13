import sys
import vtk
import serial
import serial.tools.list_ports
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer,QUrl
from ui_MainWindow import Ui_Form
import pyqtgraph as pg
import traceback
import psutil
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.style as mplStyle  #一个模块
from  matplotlib.backends.backend_qt5agg import (FigureCanvas,
            NavigationToolbar2QT as NavigationToolbar)
import numpy as np
import time


class Pyqt5_Serial(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(Pyqt5_Serial, self).__init__()
        self.ui = Ui_Form()
        self.setupUi(self)
        self.init()
        self.setWindowTitle("姿态信息显示助手")
        self.ser = serial.Serial()
        self.port_check()

        # 接收数据和发送数据数目置零
        self.data_num_received = 0
        self.lineEdit.setText(str(self.data_num_received))
        self.data_num_sended = 0
        self.lineEdit_2.setText(str(self.data_num_sended))


    def init(self):

        #设置主窗口图标
        self.setWindowIcon(QtGui.QIcon('./QtApp/images/11.ico'))

        #设置主窗口的位置
        self.setGeometry(450, 100, 1075, 865)

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

        #Pose_3d
        self.Pose_3d()

        # 绘制CPU使用率曲线
        self.Draw_cpu()

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
        self.timer.start(2)

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
            #读取发送端信息
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

    # 接收数据
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
            else:
                # 串口接收到的字符串为b'123',要转化成unicode字符串才能输出到窗口中去
                self.s2__receive_text.insertPlainText(data.decode('iso-8859-1'))

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

    def Pose_3d(self):
        self.browser = self.webEngineView
        #设置本地的网页地址
        self.browser.load(QUrl('http://www.baidu.com'))

    def Draw_cpu(self):

        self.main_layout1 = QtWidgets.QGridLayout()  # 创建一个网格布局
        self.main_layout2 = QtWidgets.QGridLayout()  # 创建一个网格布局
        self.main_layout3 = QtWidgets.QGridLayout()  # 创建一个网格布局
        self.main_layout4 = QtWidgets.QGridLayout()  # 创建一个网格布局

        self.centralWidget1.setLayout(self.main_layout1)  # 设置主部件的布局为网格
        self.centralWidget2.setLayout(self.main_layout2)  # 设置主部件的布局为网格
        self.centralWidget3.setLayout(self.main_layout3)  # 设置主部件的布局为网格
        self.centralWidget4.setLayout(self.main_layout4)  # 设置主部件的布局为网格

        self.plot_widget1 = QtWidgets.QWidget()  # 实例化一个widget部件作为K线图部件
        self.plot_widget2 = QtWidgets.QWidget()  # 实例化一个widget部件作为K线图部件
        self.plot_widget3 = QtWidgets.QWidget()  # 实例化一个widget部件作为K线图部件
        self.plot_widget4 = QtWidgets.QWidget()  # 实例化一个widget部件作为K线图部件

        self.plot_layout1 = QtWidgets.QGridLayout()  # 实例化一个网格布局层
        self.plot_layout2 = QtWidgets.QGridLayout()  # 实例化一个网格布局层
        self.plot_layout3 = QtWidgets.QGridLayout()  # 实例化一个网格布局层
        self.plot_layout4 = QtWidgets.QGridLayout()  # 实例化一个网格布局层

        self.plot_widget1.setLayout(self.plot_layout1)  # 设置K线图部件的布局层
        self.plot_widget2.setLayout(self.plot_layout2)  # 设置K线图部件的布局层
        self.plot_widget3.setLayout(self.plot_layout3)  # 设置K线图部件的布局层
        self.plot_widget4.setLayout(self.plot_layout4)  # 设置K线图部件的布局层

        self.plot_plt1 = pg.PlotWidget()  # 实例化一个绘图部件
        self.plot_plt2 = pg.PlotWidget()  # 实例化一个绘图部件
        self.plot_plt3 = pg.PlotWidget()  # 实例化一个绘图部件
        self.plot_plt4 = pg.PlotWidget()  # 实例化一个绘图部件

        self.plot_plt1.showGrid(x=True, y=True)  # 显示图形网格
        self.plot_plt2.showGrid(x=True, y=True)  # 显示图形网格
        self.plot_plt3.showGrid(x=True, y=True)  # 显示图形网格
        self.plot_plt4.showGrid(x=True, y=True)  # 显示图形网格

        self.plot_layout1.addWidget(self.plot_plt1)  # 添加绘图部件到K线图部件的网格布局层
        self.plot_layout2.addWidget(self.plot_plt2)  # 添加绘图部件到K线图部件的网格布局层
        self.plot_layout3.addWidget(self.plot_plt3)  # 添加绘图部件到K线图部件的网格布局层
        self.plot_layout4.addWidget(self.plot_plt4)  # 添加绘图部件到K线图部件的网格布局层
        # 将上述部件添加到布局层中
        self.main_layout1.addWidget(self.plot_widget1, 1, 0, 3, 3)
        self.main_layout2.addWidget(self.plot_widget2, 1, 0, 3, 3)
        self.main_layout3.addWidget(self.plot_widget3, 1, 0, 3, 3)
        self.main_layout4.addWidget(self.plot_widget4, 1, 0, 3, 3)
        #设置每个列表的Y轴范围
        self.plot_plt1.setYRange(max=200, min=0)
        self.plot_plt2.setYRange(max=200, min=0)
        self.plot_plt3.setYRange(max=200, min=0)
        self.plot_plt4.setYRange(max=200, min=0)
        #设置四个列表，用来存放数据
        self.data_list1 = []
        self.data_list2 = []
        self.data_list3 = []
        self.data_list4 = []
        self.timer_start()

    # 启动定时器 时间间隔秒
    def timer_start(self):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.get_cpu_info)
        self.timer.start(0.0001)

    # 获取CPU使用率
    def get_cpu_info(self):
        try:
            cpu = "%0.2f" % psutil.cpu_percent(interval=0.0001)
            #设置四个数据列表，存放待显示的数据信息
            self.data_list1.append(float(cpu)+5)
            self.data_list2.append(float(cpu)+10)
            self.data_list3.append(float(cpu)+15)
            self.data_list4.append(float(cpu)+20)
            #以不同颜色显示每个数据列表中的数据信息
            self.plot_plt1.plot().setData(self.data_list1, pen='y')
            self.plot_plt2.plot().setData(self.data_list2, pen='r')
            self.plot_plt3.plot().setData(self.data_list3, pen='b')
            self.plot_plt4.plot().setData(self.data_list4, pen='w')
        except Exception as e:
            print(traceback.print_exc())

if __name__ == '__main__':

    #异常获取模块
    _oldExceptionCatch = sys.excepthook
    def _exceptionCatch(exceptionType, value, traceback):
        _oldExceptionCatch(exceptionType, value, traceback)
    # 由于Qt界面中的异常捕获不到
    # 把系统的全局异常获取函数进行重定向
    sys.excepthook = _exceptionCatch

    #QT显示模块
    app = QtWidgets.QApplication(sys.argv)
    myshow = Pyqt5_Serial()
    myshow.show()
    sys.exit(app.exec_())



