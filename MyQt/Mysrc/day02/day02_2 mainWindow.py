import sys
import day02_2

from PyQt5.QtWidgets import QApplication,QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = day02_2.Ui_Form()
    #向主窗口上添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

