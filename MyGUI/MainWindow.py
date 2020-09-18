import sys
import PyQt5.QtWidgets as qw

import ui_uart_tools


if __name__ == "__main__":
    app = qw.QApplication(sys.argv)
    w = qw.QMainWindow()
    ui = ui_uart_tools.Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())
