import sys
import PyQt5.QtWidgets as qw
from PyQt5.QtWidgets import QApplication, QMainWindow

import ui_uart_tools


class myMainWindow(QMainWindow, ui_uart_tools.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 绑定信号与槽
        self.comboBox_baud.currentIndexChanged.connect(self.comboBox_baud_cb) #波特率
        self.comboBox_databit.currentIndexChanged.connect(self.comboBox_databit_cb) #数据位
        self.comboBox_polarity.currentIndexChanged.connect(self.comboBox_polarity_cb) #校验位
        self.comboBox_stopbit.currentIndexChanged.connect(self.comboBox_stopbit_cb) #停止位
        self.comboBox_flow.currentIndexChanged.connect(self.comboBox_flow_cb) #流控

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = myMainWindow()
    mainWindow.show()

    sys.exit(app.exec_())
