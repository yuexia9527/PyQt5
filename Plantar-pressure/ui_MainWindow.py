# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1483, 790)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 538, 1121, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalGroupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.verticalGroupBox.setMinimumSize(QtCore.QSize(821, 0))
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.s2__receive_text = QtWidgets.QTextBrowser(self.verticalGroupBox)
        self.s2__receive_text.setEnabled(False)
        self.s2__receive_text.setGeometry(QtCore.QRect(11, 26, 799, 184))
        self.s2__receive_text.setObjectName("s2__receive_text")
        self.gridLayout_2.addWidget(self.verticalGroupBox, 0, 0, 2, 1)
        self.verticalGroupBox_2 = QtWidgets.QGroupBox(self.layoutWidget)
        self.verticalGroupBox_2.setMinimumSize(QtCore.QSize(279, 0))
        self.verticalGroupBox_2.setObjectName("verticalGroupBox_2")
        self.s3__send_text = QtWidgets.QTextEdit(self.verticalGroupBox_2)
        self.s3__send_text.setGeometry(QtCore.QRect(11, 26, 257, 71))
        self.s3__send_text.setObjectName("s3__send_text")
        self.gridLayout_2.addWidget(self.verticalGroupBox_2, 0, 1, 1, 2)
        self.formGroupBox_4 = QtWidgets.QGroupBox(self.layoutWidget)
        self.formGroupBox_4.setObjectName("formGroupBox_4")
        self.s3__clear_button = QtWidgets.QPushButton(self.formGroupBox_4)
        self.s3__clear_button.setGeometry(QtCore.QRect(12, 53, 103, 39))
        self.s3__clear_button.setMaximumSize(QtCore.QSize(16777215, 16777213))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("QtApp/images/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.s3__clear_button.setIcon(icon)
        self.s3__clear_button.setIconSize(QtCore.QSize(30, 30))
        self.s3__clear_button.setObjectName("s3__clear_button")
        self.hex_send = QtWidgets.QCheckBox(self.formGroupBox_4)
        self.hex_send.setGeometry(QtCore.QRect(12, 27, 81, 19))
        self.hex_send.setObjectName("hex_send")
        self.gridLayout_2.addWidget(self.formGroupBox_4, 1, 1, 1, 1)
        self.s3__send_button = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(104)
        sizePolicy.setHeightForWidth(self.s3__send_button.sizePolicy().hasHeightForWidth())
        self.s3__send_button.setSizePolicy(sizePolicy)
        self.s3__send_button.setMinimumSize(QtCore.QSize(131, 98))
        self.s3__send_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("QtApp/images/send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.s3__send_button.setIcon(icon1)
        self.s3__send_button.setIconSize(QtCore.QSize(55, 55))
        self.s3__send_button.setObjectName("s3__send_button")
        self.gridLayout_2.addWidget(self.s3__send_button, 1, 2, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 329, 261, 201))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formGroupBox = QtWidgets.QGroupBox(self.layoutWidget2)
        self.formGroupBox.setMaximumSize(QtCore.QSize(888, 89))
        self.formGroupBox.setObjectName("formGroupBox")
        self.label = QtWidgets.QLabel(self.formGroupBox)
        self.label.setGeometry(QtCore.QRect(11, 26, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.formGroupBox)
        self.label_2.setGeometry(QtCore.QRect(11, 57, 60, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(70, 20, 51, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formGroupBox)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 60, 51, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.formGroupBox, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.layoutWidget2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setGeometry(QtCore.QRect(20, 60, 87, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 26, 111, 16))
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.formGroupBox_3 = QtWidgets.QGroupBox(self.layoutWidget2)
        self.formGroupBox_3.setMinimumSize(QtCore.QSize(0, 0))
        self.formGroupBox_3.setMaximumSize(QtCore.QSize(16777215, 104))
        self.formGroupBox_3.setObjectName("formGroupBox_3")
        self.timer_send_cb = QtWidgets.QCheckBox(self.formGroupBox_3)
        self.timer_send_cb.setGeometry(QtCore.QRect(11, 31, 87, 19))
        self.timer_send_cb.setObjectName("timer_send_cb")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formGroupBox_3)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(11, 65, 51, 21))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.dw = QtWidgets.QLabel(self.formGroupBox_3)
        self.dw.setGeometry(QtCore.QRect(72, 65, 39, 16))
        self.dw.setObjectName("dw")
        self.gridLayout_3.addWidget(self.formGroupBox_3, 1, 0, 1, 1)
        self.formGroupBox_2 = QtWidgets.QGroupBox(self.layoutWidget2)
        self.formGroupBox_2.setObjectName("formGroupBox_2")
        self.hex_receive = QtWidgets.QCheckBox(self.formGroupBox_2)
        self.hex_receive.setGeometry(QtCore.QRect(21, 26, 81, 19))
        self.hex_receive.setObjectName("hex_receive")
        self.s2__clear_button = QtWidgets.QPushButton(self.formGroupBox_2)
        self.s2__clear_button.setGeometry(QtCore.QRect(11, 55, 98, 34))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("QtApp/images/clean_receive.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.s2__clear_button.setIcon(icon2)
        self.s2__clear_button.setIconSize(QtCore.QSize(25, 25))
        self.s2__clear_button.setObjectName("s2__clear_button")
        self.gridLayout_3.addWidget(self.formGroupBox_2, 1, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(1126, 10, 351, 751))
        self.groupBox_2.setMinimumSize(QtCore.QSize(351, 751))
        self.groupBox_2.setObjectName("groupBox_2")
        self.centralWidget2 = QtWidgets.QWidget(self.groupBox_2)
        self.centralWidget2.setGeometry(QtCore.QRect(10, 20, 331, 721))
        self.centralWidget2.setObjectName("centralWidget2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(278, 10, 841, 521))
        self.groupBox.setMinimumSize(QtCore.QSize(841, 521))
        self.groupBox.setObjectName("groupBox")
        self.centralWidget1 = QtWidgets.QWidget(self.groupBox)
        self.centralWidget1.setGeometry(QtCore.QRect(12, 27, 817, 482))
        self.centralWidget1.setMinimumSize(QtCore.QSize(420, 250))
        self.centralWidget1.setObjectName("centralWidget1")
        self.state_label = QtWidgets.QLabel(Form)
        self.state_label.setGeometry(QtCore.QRect(10, 768, 1471, 17))
        self.state_label.setText("")
        self.state_label.setTextFormat(QtCore.Qt.AutoText)
        self.state_label.setScaledContents(True)
        self.state_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.state_label.setObjectName("state_label")
        self.formGroupBox1 = QtWidgets.QGroupBox(Form)
        self.formGroupBox1.setGeometry(QtCore.QRect(10, 10, 261, 312))
        self.formGroupBox1.setMinimumSize(QtCore.QSize(203, 279))
        self.formGroupBox1.setMaximumSize(QtCore.QSize(888, 312))
        self.formGroupBox1.setObjectName("formGroupBox1")
        self.layoutWidget3 = QtWidgets.QWidget(self.formGroupBox1)
        self.layoutWidget3.setGeometry(QtCore.QRect(11, 16, 231, 291))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.s1__lb_1 = QtWidgets.QLabel(self.layoutWidget3)
        self.s1__lb_1.setMinimumSize(QtCore.QSize(75, 26))
        self.s1__lb_1.setMaximumSize(QtCore.QSize(75, 26))
        self.s1__lb_1.setObjectName("s1__lb_1")
        self.gridLayout.addWidget(self.s1__lb_1, 0, 0, 1, 1)
        self.s1__box_1 = QtWidgets.QPushButton(self.layoutWidget3)
        self.s1__box_1.setMinimumSize(QtCore.QSize(94, 28))
        self.s1__box_1.setMaximumSize(QtCore.QSize(94, 28))
        self.s1__box_1.setAutoRepeatInterval(100)
        self.s1__box_1.setDefault(True)
        self.s1__box_1.setObjectName("s1__box_1")
        self.gridLayout.addWidget(self.s1__box_1, 0, 1, 1, 1)
        self.s1__lb_2 = QtWidgets.QLabel(self.layoutWidget3)
        self.s1__lb_2.setMinimumSize(QtCore.QSize(75, 21))
        self.s1__lb_2.setMaximumSize(QtCore.QSize(75, 21))
        self.s1__lb_2.setObjectName("s1__lb_2")
        self.gridLayout.addWidget(self.s1__lb_2, 1, 0, 1, 1)
        self.s1__box_2 = QtWidgets.QComboBox(self.layoutWidget3)
        self.s1__box_2.setMinimumSize(QtCore.QSize(94, 21))
        self.s1__box_2.setMaximumSize(QtCore.QSize(94, 21))
        self.s1__box_2.setObjectName("s1__box_2")
        self.gridLayout.addWidget(self.s1__box_2, 1, 1, 1, 1)
        self.s1__lb_3 = QtWidgets.QLabel(self.layoutWidget3)
        self.s1__lb_3.setMinimumSize(QtCore.QSize(60, 21))
        self.s1__lb_3.setMaximumSize(QtCore.QSize(60, 21))
        self.s1__lb_3.setObjectName("s1__lb_3")
        self.gridLayout.addWidget(self.s1__lb_3, 2, 0, 1, 1)
        self.s1__box_3 = QtWidgets.QComboBox(self.layoutWidget3)
        self.s1__box_3.setMinimumSize(QtCore.QSize(94, 21))
        self.s1__box_3.setMaximumSize(QtCore.QSize(94, 21))
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
        self.gridLayout.addWidget(self.s1__box_3, 2, 1, 1, 1)
        self.s1__lb_4 = QtWidgets.QLabel(self.layoutWidget3)
        self.s1__lb_4.setMinimumSize(QtCore.QSize(60, 21))
        self.s1__lb_4.setMaximumSize(QtCore.QSize(60, 21))
        self.s1__lb_4.setObjectName("s1__lb_4")
        self.gridLayout.addWidget(self.s1__lb_4, 3, 0, 1, 1)
        self.s1__box_4 = QtWidgets.QComboBox(self.layoutWidget3)
        self.s1__box_4.setMinimumSize(QtCore.QSize(94, 21))
        self.s1__box_4.setMaximumSize(QtCore.QSize(94, 21))
        self.s1__box_4.setObjectName("s1__box_4")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.gridLayout.addWidget(self.s1__box_4, 3, 1, 1, 1)
        self.s1__lb_5 = QtWidgets.QLabel(self.layoutWidget3)
        self.s1__lb_5.setMinimumSize(QtCore.QSize(60, 21))
        self.s1__lb_5.setMaximumSize(QtCore.QSize(60, 21))
        self.s1__lb_5.setObjectName("s1__lb_5")
        self.gridLayout.addWidget(self.s1__lb_5, 4, 0, 1, 1)
        self.s1__box_5 = QtWidgets.QComboBox(self.layoutWidget3)
        self.s1__box_5.setMinimumSize(QtCore.QSize(94, 21))
        self.s1__box_5.setMaximumSize(QtCore.QSize(94, 21))
        self.s1__box_5.setObjectName("s1__box_5")
        self.s1__box_5.addItem("")
        self.gridLayout.addWidget(self.s1__box_5, 4, 1, 1, 1)
        self.s1__lb_6 = QtWidgets.QLabel(self.layoutWidget3)
        self.s1__lb_6.setMinimumSize(QtCore.QSize(60, 21))
        self.s1__lb_6.setMaximumSize(QtCore.QSize(60, 21))
        self.s1__lb_6.setObjectName("s1__lb_6")
        self.gridLayout.addWidget(self.s1__lb_6, 5, 0, 1, 1)
        self.s1__box_6 = QtWidgets.QComboBox(self.layoutWidget3)
        self.s1__box_6.setMinimumSize(QtCore.QSize(94, 21))
        self.s1__box_6.setMaximumSize(QtCore.QSize(94, 21))
        self.s1__box_6.setObjectName("s1__box_6")
        self.s1__box_6.addItem("")
        self.gridLayout.addWidget(self.s1__box_6, 5, 1, 1, 1)
        self.open_button = QtWidgets.QPushButton(self.layoutWidget3)
        self.open_button.setMinimumSize(QtCore.QSize(176, 29))
        self.open_button.setMaximumSize(QtCore.QSize(179, 29))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("QtApp/images/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_button.setIcon(icon3)
        self.open_button.setObjectName("open_button")
        self.gridLayout.addWidget(self.open_button, 6, 0, 1, 2)
        self.close_button = QtWidgets.QPushButton(self.layoutWidget3)
        self.close_button.setMinimumSize(QtCore.QSize(179, 29))
        self.close_button.setMaximumSize(QtCore.QSize(179, 29))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("QtApp/images/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button.setIcon(icon4)
        self.close_button.setObjectName("close_button")
        self.gridLayout.addWidget(self.close_button, 7, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.verticalGroupBox.setTitle(_translate("Form", "接收区"))
        self.verticalGroupBox_2.setTitle(_translate("Form", "发送区"))
        self.s3__send_text.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.formGroupBox_4.setTitle(_translate("Form", "发送区控制"))
        self.s3__clear_button.setText(_translate("Form", "清除发送"))
        self.hex_send.setText(_translate("Form", "Hex发送"))
        self.formGroupBox.setTitle(_translate("Form", "串口状态"))
        self.label.setText(_translate("Form", "已接收："))
        self.label_2.setText(_translate("Form", "已发送："))
        self.groupBox_3.setTitle(_translate("Form", "显示控制"))
        self.comboBox.setItemText(0, _translate("Form", "0"))
        self.comboBox.setItemText(1, _translate("Form", "1"))
        self.comboBox.setItemText(2, _translate("Form", "2"))
        self.comboBox.setItemText(3, _translate("Form", "3"))
        self.comboBox.setItemText(4, _translate("Form", "4"))
        self.comboBox.setItemText(5, _translate("Form", "5"))
        self.comboBox.setItemText(6, _translate("Form", "6"))
        self.comboBox.setItemText(7, _translate("Form", "7"))
        self.comboBox.setItemText(8, _translate("Form", "8"))
        self.comboBox.setItemText(9, _translate("Form", "9"))
        self.comboBox.setItemText(10, _translate("Form", "10"))
        self.comboBox.setItemText(11, _translate("Form", "11"))
        self.comboBox.setItemText(12, _translate("Form", "12"))
        self.comboBox.setItemText(13, _translate("Form", "13"))
        self.label_5.setText(_translate("Form", "请选择显示通道："))
        self.formGroupBox_3.setTitle(_translate("Form", "接收区控制"))
        self.timer_send_cb.setText(_translate("Form", "定时发送"))
        self.lineEdit_3.setText(_translate("Form", "1000"))
        self.dw.setText(_translate("Form", "ms/次"))
        self.formGroupBox_2.setTitle(_translate("Form", "接收区控制"))
        self.hex_receive.setText(_translate("Form", "Hex接收"))
        self.s2__clear_button.setText(_translate("Form", "清除接收"))
        self.groupBox_2.setTitle(_translate("Form", "足底压三维显示"))
        self.groupBox.setTitle(_translate("Form", "足底压信息显示"))
        self.formGroupBox1.setTitle(_translate("Form", "串口设置"))
        self.s1__lb_1.setText(_translate("Form", "串口检测："))
        self.s1__box_1.setText(_translate("Form", "检测串口"))
        self.s1__lb_2.setText(_translate("Form", "串口选择："))
        self.s1__lb_3.setText(_translate("Form", "波特率："))
        self.s1__box_3.setItemText(0, _translate("Form", "19200"))
        self.s1__box_3.setItemText(1, _translate("Form", "2400"))
        self.s1__box_3.setItemText(2, _translate("Form", "4800"))
        self.s1__box_3.setItemText(3, _translate("Form", "9600"))
        self.s1__box_3.setItemText(4, _translate("Form", "14400"))
        self.s1__box_3.setItemText(5, _translate("Form", "38400"))
        self.s1__box_3.setItemText(6, _translate("Form", "57600"))
        self.s1__box_3.setItemText(7, _translate("Form", "76800"))
        self.s1__box_3.setItemText(8, _translate("Form", "12800"))
        self.s1__box_3.setItemText(9, _translate("Form", "115200"))
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
