import sys
import vtk
import serial
import serial.tools.list_ports
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer
from ui_MainWindow import Ui_Form
from ui_MainWindow import Ui_MainWindow
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
        self.setWindowTitle("磁定位显示助手")
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
        self.setGeometry(85, 125, 840, 720)

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


class VTKView(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init()
        self.VTK()


    def init(self):

        #设置主窗口图标
        self.setWindowIcon(QtGui.QIcon('./QtApp/images/11.ico'))

        #设置主窗口的位置
        self.setGeometry(925,125,840,720)

        #磁钉3D姿态显示
        self.setWindowTitle("磁钉3D姿态显示")


    def VTK(self):

        self.ren = vtk.vtkRenderer()
        self.ui.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.ui.vtkWidget.GetRenderWindow().GetInteractor()

        # Create source
        source = vtk.vtkCylinderSource()
        source.SetHeight(1)  # 设置柱体的高
        source.SetRadius(0.25)  # 设置柱体横截面的半径
        source.SetResolution(999)  # 设置柱体横截面的等边多边形的边数
        source.SetCenter(0, 0, 0)  # 设置柱体的起始坐标点

        # Create a mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(source.GetOutputPort())

        # Create an actor
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)


        # add the actors to the scene
        self.ren.AddActor(actor)
        colors = vtk.vtkNamedColors()
        self.ren.SetBackground(colors.GetColor3d("SlateGray"))

        axes = vtk.vtkAxesActor()
        # properties of the axes labels can be set as follows
        # this sets the x axis label to red
        #axes.GetXAxisCaptionActor2D().GetCaptionTextProperty().SetColor(colors.GetColor3d("Red"));
        #axes.GetYAxisCaptionActor2D().GetCaptionTextProperty().SetColor(colors.GetColor3d("Yellow"));
        #axes.GetZAxisCaptionActor2D().GetCaptionTextProperty().SetColor(colors.GetColor3d("Blue"));
        # the actual text of the axis label can be changed:
        # axes->SetXAxisLabelText("test");

        self.ren.AddActor(axes)
        transform = vtk.vtkTransform()
        transform.Translate(0.0, 0.0, 0.0)
        #  The axes are positioned with a user transform
        axes.SetUserTransform(transform)
        self.ren.GetActiveCamera().Azimuth(180)
        self.ren.GetActiveCamera().Elevation(0)
        self.ren.ResetCamera()

        array = extract_array()
        for index, a in enumerate(array):
            # Make the grid
            x = np.array(a[0])
            print(x)
            y = np.array(a[1])
            z = np.array(a[2])  # 坐标点（x,y,z）

            # Make the direction data for the arrows
            u = np.array(a[3])
            v = np.array(a[4])
            w = np.array(a[5])  # 方向（u,v,w）
            source.SetCenter(x, y, z)  # 设置柱体的起始坐标点
            time.sleep(0.01)

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



