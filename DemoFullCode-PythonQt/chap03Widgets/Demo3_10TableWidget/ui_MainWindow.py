# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(837, 471)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitterMain = QtWidgets.QSplitter(self.centralWidget)
        self.splitterMain.setOrientation(QtCore.Qt.Horizontal)
        self.splitterMain.setObjectName("splitterMain")
        self.groupBox = QtWidgets.QGroupBox(self.splitterMain)
        self.groupBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.btnInsertRow = QtWidgets.QPushButton(self.groupBox)
        self.btnInsertRow.setObjectName("btnInsertRow")
        self.gridLayout.addWidget(self.btnInsertRow, 3, 0, 1, 1)
        self.btnAppendRow = QtWidgets.QPushButton(self.groupBox)
        self.btnAppendRow.setObjectName("btnAppendRow")
        self.gridLayout.addWidget(self.btnAppendRow, 3, 1, 1, 1)
        self.chkBoxHeaderH = QtWidgets.QCheckBox(self.groupBox)
        self.chkBoxHeaderH.setChecked(True)
        self.chkBoxHeaderH.setObjectName("chkBoxHeaderH")
        self.gridLayout.addWidget(self.chkBoxHeaderH, 9, 0, 1, 1)
        self.chkBoxEditable = QtWidgets.QCheckBox(self.groupBox)
        self.chkBoxEditable.setChecked(True)
        self.chkBoxEditable.setObjectName("chkBoxEditable")
        self.gridLayout.addWidget(self.chkBoxEditable, 8, 0, 1, 1)
        self.btnReadToText = QtWidgets.QPushButton(self.groupBox)
        self.btnReadToText.setMinimumSize(QtCore.QSize(0, 25))
        self.btnReadToText.setObjectName("btnReadToText")
        self.gridLayout.addWidget(self.btnReadToText, 7, 0, 1, 2)
        self.chkBoxRowColor = QtWidgets.QCheckBox(self.groupBox)
        self.chkBoxRowColor.setChecked(True)
        self.chkBoxRowColor.setObjectName("chkBoxRowColor")
        self.gridLayout.addWidget(self.chkBoxRowColor, 8, 1, 1, 1)
        self.radioSelectItem = QtWidgets.QRadioButton(self.groupBox)
        self.radioSelectItem.setChecked(True)
        self.radioSelectItem.setObjectName("radioSelectItem")
        self.gridLayout.addWidget(self.radioSelectItem, 10, 1, 1, 1)
        self.chkBoxHeaderV = QtWidgets.QCheckBox(self.groupBox)
        self.chkBoxHeaderV.setChecked(True)
        self.chkBoxHeaderV.setObjectName("chkBoxHeaderV")
        self.gridLayout.addWidget(self.chkBoxHeaderV, 9, 1, 1, 1)
        self.radioSelectRow = QtWidgets.QRadioButton(self.groupBox)
        self.radioSelectRow.setChecked(False)
        self.radioSelectRow.setObjectName("radioSelectRow")
        self.gridLayout.addWidget(self.radioSelectRow, 10, 0, 1, 1)
        self.btnIniData = QtWidgets.QPushButton(self.groupBox)
        self.btnIniData.setMinimumSize(QtCore.QSize(0, 25))
        self.btnIniData.setObjectName("btnIniData")
        self.gridLayout.addWidget(self.btnIniData, 2, 0, 1, 2)
        self.spinRowCount = QtWidgets.QSpinBox(self.groupBox)
        self.spinRowCount.setMinimum(2)
        self.spinRowCount.setProperty("value", 8)
        self.spinRowCount.setObjectName("spinRowCount")
        self.gridLayout.addWidget(self.spinRowCount, 1, 1, 1, 1)
        self.btnSetHeader = QtWidgets.QPushButton(self.groupBox)
        self.btnSetHeader.setMinimumSize(QtCore.QSize(0, 25))
        self.btnSetHeader.setObjectName("btnSetHeader")
        self.gridLayout.addWidget(self.btnSetHeader, 0, 0, 1, 2)
        self.btnSetRows = QtWidgets.QPushButton(self.groupBox)
        self.btnSetRows.setMinimumSize(QtCore.QSize(0, 25))
        self.btnSetRows.setObjectName("btnSetRows")
        self.gridLayout.addWidget(self.btnSetRows, 1, 0, 1, 1)
        self.btnAutoHeight = QtWidgets.QPushButton(self.groupBox)
        self.btnAutoHeight.setObjectName("btnAutoHeight")
        self.gridLayout.addWidget(self.btnAutoHeight, 6, 0, 1, 1)
        self.btnAutoWidth = QtWidgets.QPushButton(self.groupBox)
        self.btnAutoWidth.setObjectName("btnAutoWidth")
        self.gridLayout.addWidget(self.btnAutoWidth, 6, 1, 1, 1)
        self.btnClearContents = QtWidgets.QPushButton(self.groupBox)
        self.btnClearContents.setObjectName("btnClearContents")
        self.gridLayout.addWidget(self.btnClearContents, 4, 1, 1, 1)
        self.btnDelCurRow = QtWidgets.QPushButton(self.groupBox)
        self.btnDelCurRow.setObjectName("btnDelCurRow")
        self.gridLayout.addWidget(self.btnDelCurRow, 4, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.splitterMain)
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setFrameShadow(QtWidgets.QFrame.Plain)
        self.splitter.setLineWidth(2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tableInfo = QtWidgets.QTableWidget(self.splitter)
        self.tableInfo.setAlternatingRowColors(True)
        self.tableInfo.setRowCount(5)
        self.tableInfo.setColumnCount(4)
        self.tableInfo.setObjectName("tableInfo")
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/boy.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.tableInfo.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.tableInfo.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/girl.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.tableInfo.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.tableInfo.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setItem(4, 3, item)
        self.tableInfo.horizontalHeader().setDefaultSectionSize(100)
        self.tableInfo.verticalHeader().setDefaultSectionSize(30)
        self.textEdit = QtWidgets.QPlainTextEdit(self.splitter)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.splitterMain)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Demo3_10, QTableWidget的使用"))
        self.btnInsertRow.setText(_translate("MainWindow", "插入行"))
        self.btnAppendRow.setText(_translate("MainWindow", "添加行"))
        self.chkBoxHeaderH.setText(_translate("MainWindow", "显示行表头"))
        self.chkBoxEditable.setText(_translate("MainWindow", "表格可编辑"))
        self.btnReadToText.setText(_translate("MainWindow", "读取表格内容到文本"))
        self.chkBoxRowColor.setText(_translate("MainWindow", "间隔行底色"))
        self.radioSelectItem.setText(_translate("MainWindow", "单元格选择"))
        self.chkBoxHeaderV.setText(_translate("MainWindow", "显示列表头"))
        self.radioSelectRow.setText(_translate("MainWindow", "行选择"))
        self.btnIniData.setText(_translate("MainWindow", "初始化表格数据"))
        self.btnSetHeader.setText(_translate("MainWindow", "设置表头"))
        self.btnSetRows.setText(_translate("MainWindow", "设置行数"))
        self.btnAutoHeight.setText(_translate("MainWindow", "自动调节行高"))
        self.btnAutoWidth.setText(_translate("MainWindow", "自动调节列宽"))
        self.btnClearContents.setText(_translate("MainWindow", "清空表格内容"))
        self.btnDelCurRow.setText(_translate("MainWindow", "删除当前行"))
        item = self.tableInfo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "列1"))
        item = self.tableInfo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "列2"))
        item = self.tableInfo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "列3"))
        __sortingEnabled = self.tableInfo.isSortingEnabled()
        self.tableInfo.setSortingEnabled(False)
        item = self.tableInfo.item(0, 0)
        item.setText(_translate("MainWindow", "0行，0列"))
        item = self.tableInfo.item(0, 1)
        item.setText(_translate("MainWindow", "0行，1列"))
        item = self.tableInfo.item(0, 2)
        item.setText(_translate("MainWindow", "1行，2列"))
        item = self.tableInfo.item(0, 3)
        item.setText(_translate("MainWindow", "0行，3列"))
        item = self.tableInfo.item(1, 0)
        item.setText(_translate("MainWindow", "1行，0列"))
        item = self.tableInfo.item(1, 1)
        item.setText(_translate("MainWindow", "1行，1列"))
        item = self.tableInfo.item(2, 0)
        item.setText(_translate("MainWindow", "2行，0列"))
        item = self.tableInfo.item(3, 0)
        item.setText(_translate("MainWindow", "3行，0列"))
        item = self.tableInfo.item(4, 0)
        item.setText(_translate("MainWindow", "4行，0列"))
        item = self.tableInfo.item(4, 3)
        item.setText(_translate("MainWindow", "4行，3列"))
        self.tableInfo.setSortingEnabled(__sortingEnabled)

import res_rc
