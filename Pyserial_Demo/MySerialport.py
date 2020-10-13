import sys
import serial
import serial.tools.list_ports
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox,QDesktopWidget
from PyQt5.QtCore import QTimer
from ui_demo_1 import Ui_MainWindow


class Pyqt5_Serial(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Pyqt5_Serial, self).__init__()
        self.setupUi(self)
        self.init()
        self.setWindowTitle("月下串口调试助手")
        self.ser = serial.Serial()
        self.port_check()

        # 接收数据和发送数据数目置零
        self.data_num_received = 0
        self.lineEdit.setText(str(self.data_num_received))
        self.data_num_sended = 0
        self.lineEdit_2.setText(str(self.data_num_sended))

        # 默认发送接收方式为HEX
        self.hex_send.setChecked(True)
        self.hex_receive.setChecked(True)

    def init(self):

        #设置主窗口图标
        self.setWindowIcon(QtGui.QIcon('./images/11.ico'))

        # 串口检测按钮
        self.s1__box_1.clicked.connect(self.port_check)

        # 串口信息显示
        self.s1__box_2.currentTextChanged.connect(self.port_imf)

        # 打开串口按钮
        self.action_start.triggered.connect(self.port_open)
        self.open_button.clicked.connect(self.port_open)

        # 关闭串口按钮
        self.action_close.triggered.connect(self.port_close)
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
        self.action_clear_send.triggered.connect(self.send_data_clear)
        # self.s3__clear_button.clicked.connect(self.send_data_clear)

        # 清除接收窗口
        self.action_clear_receive.triggered.connect(self.receive_data_clear)
        # self.s2__clear_button.clicked.connect(self.receive_data_clear)

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
            self.formGroupBox_1.setTitle("串口状态（已开启）")

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
        self.formGroupBox_1.setTitle("串口状态（已关闭）")

    # 发送数据
    def data_send(self):
        if self.ser.isOpen():
            # 自定义输入端的数据包格式
            input_Head = self.s3__send_Head.toPlainText()  # 数据包头部
            input_CMD = self.s3__send_CMD.toPlainText()  # 数据包CMD

            input_Data = self.s3__send_Data.toPlainText()  # 数据包的数据
            if input_Data != "":
                input_Data_str = input_Data
                if self.hex_send.isChecked():
                    input_Data = input_Data.strip()
                    send_data = []
                    while input_Data != '':
                        try:
                            #将input_Data数据没两个字符拿出，并转换成int类型的数据
                            input_num = int(input_Data[0:2],16)
                        except ValueError:
                            QMessageBox.critical(self, 'wrong data', '请输入十六进制数据，以空格分开!')
                            return None
                        #将拿出的字符切片
                        input_Data = input_Data[2:].strip()
                        #将数据按顺序放入列表中
                        send_data.append(input_num)
                    input_Data = bytes(send_data)
                else:
                    # ascii发送
                    input_Data = (input_Data + '\r\n').encode('utf-8')

                    # input_Data = input_Data.strip()
                    # send_data = []
                    # while input_Data != '':
                    #     try:
                    #         # 将input_Data数据没两个字符拿出，并转换成int类型的数据
                    #         input_num = int(input_Data[0:2])
                    #     except ValueError:
                    #         QMessageBox.critical(self, 'wrong data', '请输入十进制数据，以空格分开!')
                    #         return None
                    #     # 将拿出的字符切片
                    #     input_Data = input_Data[2:].strip()
                    #     # 将数据按顺序放入列表中
                    #     send_data.append(input_num)
                    # input_Data = send_data
            else:
                pass

            #将数据长度清除并更新显示
            self.s3__send_Length.setText("")
            input_Length = str(len(input_Data))
            self.s3__send_Length.insertPlainText(input_Length)

            #校验位置零,校验位为输入数据的总和
            input_CheckSum = 0
            for i in range(0,len(input_Data)):
                input_CheckSum = input_CheckSum + input_Data[i]

            if self.hex_send.isChecked():
                # 祛除十六进制的数据字符串中的空格
                input_Data = input_Data_str.replace(" ", "")

                input_CheckSum = str(hex(input_CheckSum))
                input_CheckSum = input_CheckSum[2:]
            else:
                # 将input_Data由列表转换为字符串
                input_Data_s = [str(i) for i in input_Data]
                input_Data = ''.join(input_Data_s)
                input_CheckSum = str(input_CheckSum)


            #将校验和清除并更新显示
            self.s3__send_CheckSum.setText("")
            self.s3__send_CheckSum.insertPlainText(input_CheckSum)

            input_s = input_Head + input_CMD + input_Length + input_Data + input_CheckSum
            print(input_s)

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
        self.s3__send_Head.setText("")
        self.s3__send_CMD.setText("")
        self.s3__send_Length.setText("")
        self.s3__send_Data.setText("")
        self.s3__send_CheckSum.setText("")


    def receive_data_clear(self):
        self.s2__receive_text.setText("")


if __name__ == '__main__':

    _oldExceptionCatch = sys.excepthook
    def _exceptionCatch(exceptionType, value, traceback):
        _oldExceptionCatch(exceptionType, value, traceback)
    # 由于Qt界面中的异常捕获不到
    # 把系统的全局异常获取函数进行重定向
    sys.excepthook = _exceptionCatch


    app = QtWidgets.QApplication(sys.argv)
    myshow = Pyqt5_Serial()
    myshow.show()
    sys.exit(app.exec_())
