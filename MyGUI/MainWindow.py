import sys
import PyQt5.QtWidgets as qw
from PyQt5.QtWidgets import QApplication, QMainWindow

import ui_uart_tools


class myMainWindow(QMainWindow, ui_uart_tools.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 绑定信号与槽
        self.comboBox_baud.currentIndexChanged.connect(self.comboBox_baud_cb)  # 波特率
        self.comboBox_databit.currentIndexChanged.connect(self.comboBox_databit_cb)  # 数据位
        self.comboBox_polarity.currentIndexChanged.connect(self.comboBox_polarity_cb)  # 校验位
        self.comboBox_stopbit.currentIndexChanged.connect(self.comboBox_stopbit_cb)  # 停止位
        self.comboBox_flow.currentIndexChanged.connect(self.comboBox_flow_cb)  # 流控

        self.btn_send.clicked.connect(self.btn_send_cb)

        self.action_start.triggered.connect(self.action_start_cb)
        self.action_pause.triggered.connect(self.action_pause_cb)
        self.action_stop.triggered.connect(self.action_stop_cb)
        self.action_clean.triggered.connect(self.action_clean_cb)

        self.radioButton_recv_ascii.toggled.connect(self.radioButton_recv_ascii_cb)
        self.radioButton_send_ascii.toggled.connect(self.radioButton_send_ascii_cb)
        self.radioButton_recv_hex.toggled.connect(self.radioButton_recv_hex_cb)
        self.radioButton_send_hex.toggled.connect(self.radioButton_send_hex_cb)

        # 默认勾选中自动换行功能
        # self.checkBox_auto_line.setChecked(True)

        self.checkBox_auto_line.toggled.connect(self.checkBox_auto_line_cb)
        self.checkBox_show_send.toggled.connect(self.checkBox_show_send_cb)
        self.checkBox_show_time.toggled.connect(self.checkBox_show_time_cb)
        self.checkBox_repeat_send.toggled.connect(self.checkBox_repeat_send_cb)

        # 初始化窗口
        # 设置左下角的状态栏显示以及设定相应的显示时间
        self.statusbar.showMessage("status:ok", 5000)

        # 初始化界面
        self.radioButton_recv_ascii.setChecked(True)
        self.radioButton_send_ascii.setChecked(True)

    def comboBox_baud_cb(self):
        content = self.comboBox_baud.currentText()
        print("combox's value is", content)
        text = "您当前选中了%s" % content
        qw.QMessageBox.information(self, "提示", text, qw.QMessageBox.Cancel | qw.QMessageBox.Ok)

    def comboBox_databit_cb(self):
        content = self.comboBox_databit.currentText()
        print("combox's value is", content)
        text = "您当前选中了%s" % content
        qw.QMessageBox.information(self, "提示", text, qw.QMessageBox.Cancel | qw.QMessageBox.Ok)

    def comboBox_polarity_cb(self):
        content = self.comboBox_polarity.currentText()
        print("combox's value is", content)
        text = "您当前选中了%s" % content
        qw.QMessageBox.information(self, "提示", text, qw.QMessageBox.Cancel | qw.QMessageBox.Ok)

    def comboBox_stopbit_cb(self):
        content = self.comboBox_stopbit.currentText()
        print("combox's value is", content)
        text = "您当前选中了%s" % content
        qw.QMessageBox.information(self, "提示", text, qw.QMessageBox.Cancel | qw.QMessageBox.Ok)

    def comboBox_flow_cb(self):
        content = self.comboBox_flow.currentText()
        print("combox's value is", content)
        text = "您当前选中了%s" % content
        qw.QMessageBox.information(self, "提示", text, qw.QMessageBox.Cancel | qw.QMessageBox.Ok)

    def btn_send_cb(self):
        print("you clicked btn_send.")
        text = self.textEdit_get.toPlainText()
        print('text is', text)
        # 将内容加载到comboBox_uart的下拉选项中
        self.comboBox_uart.addItem(text)

    def action_start_cb(self):
        print("you clicked action start")

    def action_pause_cb(self):
        print("you clicked action pause")

    def action_stop_cb(self):
        print("you clicked action stop")

    def action_clean_cb(self):
        print("you clicked action clean")

    def radioButton_recv_ascii_cb(self):
        print("you selected radioButton_recv_ascii")

    def radioButton_send_ascii_cb(self):
        print("you selected radioButton_send_ascii")

    def radioButton_recv_hex_cb(self):
        print("you selected radioButton_recv_hex")

    def radioButton_send_hex_cb(self):
        print("you selected radioButton_send_hex")

    def checkBox_auto_line_cb(self):
        print("you selected checkBox_auto_line")
        res_auto_line = self.checkBox_auto_line_isChecked()
        print("res_auto_line is ", res_auto_line)
        res_show_send = self.checkBox_show_send_isChecked()
        print("res_show_send is ", res_show_send)
        res_show_time = self.checkBox_show_time_isChecked()
        print("res_show_time is ", res_show_time)
        res_repeat_send = self.checkBox_repeat_send_isChecked()
        print("res_repeat_send is ", res_repeat_send)

    def checkBox_show_send_cb(self):
        print("you selected checkBox_show_send")

    def checkBox_show_time_cb(self):
        print("you selected checkBox_show_time")

    def checkBox_repeat_send_cb(self):
        print("you selected checkBox_repeat_send")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = myMainWindow()
    mainWindow.show()

    sys.exit(app.exec_())
