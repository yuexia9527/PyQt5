import sys

from PyQt5.QtWidgets import QApplication,QMainWindow

import ui_uart_tools


class myMainWindow(QMainWindow,ui_uart_tools.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # 绑定信号与槽
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = myMainWindow()
    mainWindow.show()

    sys.exit(app.exec_())
