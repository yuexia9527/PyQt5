# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import sys
import vtk

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(840, 720)
        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setGeometry(QtCore.QRect(10, 40, 201, 301))
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.s1__lb_1 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_1.setObjectName("s1__lb_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.s1__lb_1)
        self.s1__box_1 = QtWidgets.QPushButton(self.formGroupBox)
        self.s1__box_1.setAutoRepeatInterval(100)
        self.s1__box_1.setDefault(True)
        self.s1__box_1.setObjectName("s1__box_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.s1__box_1)
        self.s1__lb_2 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_2.setObjectName("s1__lb_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.s1__lb_2)
        self.s1__box_2 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_2.setObjectName("s1__box_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.s1__box_2)
        self.s1__lb_3 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_3.setObjectName("s1__lb_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.s1__lb_3)
        self.s1__box_3 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_3.setObjectName("s1__box_3")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.s1__box_3)
        self.s1__lb_4 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_4.setObjectName("s1__lb_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.s1__lb_4)
        self.s1__box_4 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_4.setObjectName("s1__box_4")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.s1__box_4)
        self.s1__lb_5 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_5.setObjectName("s1__lb_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.s1__lb_5)
        self.s1__box_5 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_5.setObjectName("s1__box_5")
        self.s1__box_5.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.s1__box_5)
        self.s1__lb_6 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_6.setObjectName("s1__lb_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.s1__lb_6)
        self.s1__box_6 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_6.setObjectName("s1__box_6")
        self.s1__box_6.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.s1__box_6)
        self.open_button = QtWidgets.QPushButton(self.formGroupBox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("QtApp/images/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_button.setIcon(icon)
        self.open_button.setObjectName("open_button")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.open_button)
        self.close_button = QtWidgets.QPushButton(self.formGroupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("QtApp/images/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button.setIcon(icon1)
        self.close_button.setObjectName("close_button")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.close_button)
        self.verticalGroupBox = QtWidgets.QGroupBox(Form)
        self.verticalGroupBox.setGeometry(QtCore.QRect(10, 390, 621, 191))
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.s2__receive_text = QtWidgets.QTextBrowser(self.verticalGroupBox)
        self.s2__receive_text.setObjectName("s2__receive_text")
        self.verticalLayout.addWidget(self.s2__receive_text)
        self.verticalGroupBox_2 = QtWidgets.QGroupBox(Form)
        self.verticalGroupBox_2.setGeometry(QtCore.QRect(630, 390, 201, 191))
        self.verticalGroupBox_2.setObjectName("verticalGroupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.verticalGroupBox_2)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.s3__send_text = QtWidgets.QTextEdit(self.verticalGroupBox_2)
        self.s3__send_text.setObjectName("s3__send_text")
        self.gridLayout.addWidget(self.s3__send_text, 1, 0, 1, 1)
        self.s3__send_button = QtWidgets.QPushButton(Form)
        self.s3__send_button.setGeometry(QtCore.QRect(720, 590, 111, 101))
        self.s3__send_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("QtApp/images/send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.s3__send_button.setIcon(icon2)
        self.s3__send_button.setIconSize(QtCore.QSize(55, 55))
        self.s3__send_button.setObjectName("s3__send_button")
        self.formGroupBox1 = QtWidgets.QGroupBox(Form)
        self.formGroupBox1.setGeometry(QtCore.QRect(10, 590, 241, 101))
        self.formGroupBox1.setObjectName("formGroupBox1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formGroupBox1)
        self.formLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout_2.setSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.formGroupBox1)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formGroupBox1)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.formGroupBox1)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formGroupBox1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.state_label = QtWidgets.QLabel(Form)
        self.state_label.setGeometry(QtCore.QRect(510, 690, 321, 21))
        self.state_label.setText("")
        self.state_label.setTextFormat(QtCore.Qt.AutoText)
        self.state_label.setScaledContents(True)
        self.state_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.state_label.setObjectName("state_label")
        self.formGroupBox_2 = QtWidgets.QGroupBox(Form)
        self.formGroupBox_2.setGeometry(QtCore.QRect(250, 590, 121, 101))
        self.formGroupBox_2.setObjectName("formGroupBox_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formGroupBox_2)
        self.formLayout_3.setContentsMargins(10, 10, 10, 10)
        self.formLayout_3.setSpacing(10)
        self.formLayout_3.setObjectName("formLayout_3")
        self.hex_receive = QtWidgets.QCheckBox(self.formGroupBox_2)
        self.hex_receive.setObjectName("hex_receive")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.hex_receive)
        self.s2__clear_button = QtWidgets.QPushButton(self.formGroupBox_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("QtApp/images/clean_receive.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.s2__clear_button.setIcon(icon3)
        self.s2__clear_button.setIconSize(QtCore.QSize(25, 25))
        self.s2__clear_button.setObjectName("s2__clear_button")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.s2__clear_button)
        self.formGroupBox_3 = QtWidgets.QGroupBox(Form)
        self.formGroupBox_3.setGeometry(QtCore.QRect(370, 590, 221, 101))
        self.formGroupBox_3.setObjectName("formGroupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.formGroupBox_3)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.timer_send_cb = QtWidgets.QCheckBox(self.formGroupBox_3)
        self.timer_send_cb.setObjectName("timer_send_cb")
        self.gridLayout_2.addWidget(self.timer_send_cb, 0, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formGroupBox_3)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 0, 2, 1, 1)
        self.dw = QtWidgets.QLabel(self.formGroupBox_3)
        self.dw.setObjectName("dw")
        self.gridLayout_2.addWidget(self.dw, 0, 3, 1, 1)
        self.formGroupBox_4 = QtWidgets.QGroupBox(Form)
        self.formGroupBox_4.setGeometry(QtCore.QRect(590, 590, 127, 104))
        self.formGroupBox_4.setObjectName("formGroupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.formGroupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.s3__clear_button = QtWidgets.QPushButton(self.formGroupBox_4)
        self.s3__clear_button.setMaximumSize(QtCore.QSize(16777215, 16777213))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("QtApp/images/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.s3__clear_button.setIcon(icon4)
        self.s3__clear_button.setIconSize(QtCore.QSize(30, 30))
        self.s3__clear_button.setObjectName("s3__clear_button")
        self.gridLayout_3.addWidget(self.s3__clear_button, 2, 0, 1, 1)
        self.hex_send = QtWidgets.QCheckBox(self.formGroupBox_4)
        self.hex_send.setObjectName("hex_send")
        self.gridLayout_3.addWidget(self.hex_send, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(220, 10, 601, 371))
        self.groupBox.setObjectName("groupBox")
        self.centralWidget = QtWidgets.QWidget(self.groupBox)
        self.centralWidget.setGeometry(QtCore.QRect(0, 20, 601, 351))
        self.centralWidget.setObjectName("centralWidget")
        self.verticalGroupBox.raise_()
        self.verticalGroupBox_2.raise_()
        self.formGroupBox.raise_()
        self.s3__send_button.raise_()
        self.formGroupBox.raise_()
        self.state_label.raise_()
        self.formGroupBox_2.raise_()
        self.formGroupBox_3.raise_()
        self.formGroupBox_4.raise_()
        self.groupBox.raise_()


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.formGroupBox.setTitle(_translate("Form", "串口设置"))
        self.s1__lb_1.setText(_translate("Form", "串口检测："))
        self.s1__box_1.setText(_translate("Form", "检测串口"))
        self.s1__lb_2.setText(_translate("Form", "串口选择："))
        self.s1__lb_3.setText(_translate("Form", "波特率："))
        self.s1__box_3.setItemText(0, _translate("Form", "115200"))
        self.s1__box_3.setItemText(1, _translate("Form", "2400"))
        self.s1__box_3.setItemText(2, _translate("Form", "4800"))
        self.s1__box_3.setItemText(3, _translate("Form", "9600"))
        self.s1__box_3.setItemText(4, _translate("Form", "14400"))
        self.s1__box_3.setItemText(5, _translate("Form", "19200"))
        self.s1__box_3.setItemText(6, _translate("Form", "38400"))
        self.s1__box_3.setItemText(7, _translate("Form", "57600"))
        self.s1__box_3.setItemText(8, _translate("Form", "76800"))
        self.s1__box_3.setItemText(9, _translate("Form", "12800"))
        self.s1__box_3.setItemText(10, _translate("Form", "230400"))
        self.s1__box_3.setItemText(11, _translate("Form", "460800"))
        self.s1__lb_4.setText(_translate("Form", "数据位："))
        self.s1__box_4.setItemText(0, _translate("Form", "8"))
        self.s1__box_4.setItemText(1, _translate("Form", "7"))
        self.s1__box_4.setItemText(2, _translate("Form", "6"))
        self.s1__box_4.setItemText(3, _translate("Form", "5"))
        self.s1__lb_5.setText(_translate("Form", "校验位："))
        self.s1__box_5.setItemText(0, _translate("Form", "N"))
        self.s1__lb_6.setText(_translate("Form", "停止位："))
        self.s1__box_6.setItemText(0, _translate("Form", "1"))
        self.open_button.setText(_translate("Form", "打开串口"))
        self.close_button.setText(_translate("Form", "关闭串口"))
        self.verticalGroupBox.setTitle(_translate("Form", "接收区"))
        self.verticalGroupBox_2.setTitle(_translate("Form", "发送区"))
        self.s3__send_text.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">S</p></body></html>"))
        self.formGroupBox1.setTitle(_translate("Form", "串口状态"))
        self.label.setText(_translate("Form", "已接收："))
        self.label_2.setText(_translate("Form", "已发送："))
        self.formGroupBox_2.setTitle(_translate("Form", "接收区控制"))
        self.hex_receive.setText(_translate("Form", "Hex接收"))
        self.s2__clear_button.setText(_translate("Form", "清除接收"))
        self.formGroupBox_3.setTitle(_translate("Form", "接收区控制"))
        self.timer_send_cb.setText(_translate("Form", "定时发送"))
        self.lineEdit_3.setText(_translate("Form", "1000"))
        self.dw.setText(_translate("Form", "ms/次"))
        self.formGroupBox_4.setTitle(_translate("Form", "发送区控制"))
        self.s3__clear_button.setText(_translate("Form", "清除发送"))
        self.hex_send.setText(_translate("Form", "Hex发送"))
        self.groupBox.setTitle(_translate("Form", "磁钉位姿显示"))

class Ui_MainWindow(object):
    def setupUi( self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.gridlayout = QtWidgets.QGridLayout(self.centralWidget)
        self.vtkWidget = QVTKRenderWindowInteractor(self.centralWidget)
        self.gridlayout.addWidget(self.vtkWidget, 0, 0, 100, 100)
        MainWindow.setCentralWidget(self.centralWidget)
