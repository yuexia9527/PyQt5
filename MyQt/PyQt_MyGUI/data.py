import sys
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
from PyQt5.QtSql import *
import pyqtgraph as pg
import serial
import GL   # GL.py 中存放了程序需要用到的全局变量

# COM端口选择
print('You selected %s, baudrate %d, %d byte.' % (GL.comport, int(GL.baudrate), GL.bytes))
serialport = serial.Serial(GL.comport, int(GL.baudrate), timeout=0.5, parity=serial.PARITY_NONE, rtscts=1)   # 定义串口接受数据的参数（初始化串口）

class WorkThread(QThread):
    receive = pyqtSignal()
    def run(self):
        while True:
            if (GL.bytes == 51):
                data = serialport.readline()
            if data != '':
                data1 = data.decode()
                data1 = data1.strip().split()
                data1 = [str(i) for i in data1[:6]]
                GL.data2 = data1
                self.receive.emit()

class DataGrid(QWidget):

    def createTableAndInit(self):
        # 添加数据库
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        # 设置数据库名称
        self.db.setDatabaseName('./db/DataBase.db')
        # 判断是否打开
        if not self.db.open():
            return False
        # 声明数据库查询对象
        query = QSqlQuery()
        # 创建表
        query.exec("create table device(id int , time int  , name vchar, sex vchar, age int, deparment int )")
        # 添加记录
        sql = "insert into device(id,time,name,sex,age,deparment) values(%d,%d,%d,%d,%d,%d)"%(
        GL.list[0], GL.list[1], GL.list[2], GL.list[3], GL.list[4], GL.list[5])
        query.exec(sql)
        return True

    def __init__(self):
        super().__init__()
        self.setWindowTitle("磁定位数据汇集点")
        self.resize(600, 750)
        self.createTableAndInit()
        # 当前页
        self.currentPage = 0
        # 总页数
        self.totalPage = 0
        # 总记录数
        self.totalRecrodCount = 0
        # 每页显示记录数
        self.PageRecordCount = 6
        self.initUI()
        self.plt = self.graphicsView.addPlot(title='传感器曲线')

    def initUI(self):
        # 创建窗口
        self.createWindow()
        # 设置表格
        self.setTableView()
        self.workthread = WorkThread()

        # 信号槽连接
        self.prevButton.clicked.connect(self.onPrevButtonClick)
        self.nextButton.clicked.connect(self.onNextButtonClick)
        self.workthread.receive.connect(self.update_data)
        self.switchPageButton.clicked.connect(self.onSwitchPageButtonClick)
        self.workthread.start()

    def update_data(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString("yyyyMMdd hh:mm:ss dddd")
        if GL.data2 != []:
            self.temperature.setText(GL.data2[0])
            self.pressure.setText(GL.data2[1])
            self.flow.setText(GL.data2[2])
            self.address.setText(GL.data2[5])
            GL.list[0] = int(GL.list[0] + 1)
            GL.list[1] = timeDisplay[9:17]
            GL.list[2] = int(GL.data2[1])
            GL.list[3] = int(GL.data2[0])
            GL.list[4] = int(GL.data2[2])
            GL.list[5] = GL.data2[5]

            GL.x_plot.append(GL.list[0])
            GL.y_plot.append(GL.list[2])
            GL.blue_plot.append(GL.list[3])
        if len(GL.x_plot) == 100:
            GL.x_plot = [0]
            GL.y_plot = [0]
            GL.blue_plot = [0]                        # 用刚刚采集到的100个点，画图

        self.plt.clear()
        self.plt.plot(GL.x_plot, GL.y_plot, pen= pg.mkPen(color='r', width=3), name="Red curve")
        self.plt.plot(GL.x_plot, GL.blue_plot, pen= pg.mkPen(color='b', width=3), name="Blue curve")
        self.db.open()
        query = QSqlQuery()
        sql_1 = """insert into device(id,time,name,sex,age,deparment) values(%d,"%s",%d,%d,%d,"%s")""" % (
        GL.list[0], GL.list[1], GL.list[2], GL.list[3], GL.list[4], GL.list[5])
        query.exec(sql_1)
        self.db.close()

    def closeEvent(self, event):
        # 关闭数据库
        self.db.close()

    # 创建窗口
    def createWindow(self):

        # 操作布局
        operatorLayout = QHBoxLayout()
        temperatureLayout = QHBoxLayout()
        pressureLayout = QHBoxLayout()
        flowLayout = QHBoxLayout()
        addressLayout = QHBoxLayout()

        # 传感器显示布局
        self.temperature = QLabel('0')
        self.temperature.setFixedWidth(200)
        self.temperature_status = QLineEdit('NO')
        self.temperature_status.setFixedWidth(200)
        self.pressure = QLabel('0')
        self.pressure.setFixedWidth(200)
        self.pressure_status = QLineEdit('NO')
        self.pressure_status.setFixedWidth(200)
        self.flow = QLabel('0')
        self.flow.setFixedWidth(200)
        self.flow_status = QLineEdit('NO')
        self.flow_status.setFixedWidth(200)
        self.address = QLabel('0')
        self.address.setFixedWidth(200)
        self.address_status = QLineEdit('NO')
        self.address_status.setFixedWidth(200)

        # 所有的状态标签
        temperature_show1 = QLabel("温度传感器:")
        temperature_show2 = QLabel("温度传感器工作状态:")
        pressure_show1 = QLabel("压力传感器:")
        pressure_show2 = QLabel("压力传感器工作状态:")
        flow_show1 = QLabel("流量传感器:")
        flow_show2 = QLabel("流量传感器工作状态:")
        address_show1 = QLabel("地址信息  :")
        address_show2 = QLabel("角度传感器工作状态:")

        # 添加布局，使用的是水平布局，然后垂直摆放
        temperatureLayout.addWidget(temperature_show1)
        temperatureLayout.addWidget(self.temperature)
        temperatureLayout.addWidget(temperature_show2)
        temperatureLayout.addWidget(self.temperature_status)
        pressureLayout.addWidget(pressure_show1)
        pressureLayout.addWidget(self.pressure)
        pressureLayout.addWidget(pressure_show2)
        pressureLayout.addWidget(self.pressure_status)
        flowLayout.addWidget(flow_show1)
        flowLayout.addWidget(self.flow)
        flowLayout.addWidget(flow_show2)
        flowLayout.addWidget(self.flow_status)
        addressLayout.addWidget(address_show1)
        addressLayout.addWidget(self.address)
        addressLayout.addWidget(address_show2)
        addressLayout.addWidget(self.address_status)

        self.prevButton = QPushButton("前一页")
        self.nextButton = QPushButton("后一页")
        self.switchPageButton = QPushButton("跳转")
        self.switchPageLineEdit = QLineEdit('0')
        self.switchPageLineEdit.setFixedWidth(40)

        switchPage = QLabel("转到第")
        page = QLabel("页")
        operatorLayout.addWidget(self.prevButton)
        operatorLayout.addWidget(self.nextButton)
        operatorLayout.addWidget(switchPage)
        operatorLayout.addWidget(self.switchPageLineEdit)
        operatorLayout.addWidget(page)
        operatorLayout.addWidget(self.switchPageButton)
        operatorLayout.addWidget(QSplitter())

        # 状态布局
        statusLayout = QHBoxLayout()
        self.totalPageLabel = QLabel()
        self.totalPageLabel.setFixedWidth(70)
        self.currentPageLabel = QLabel()
        self.currentPageLabel.setFixedWidth(70)

        self.totalRecordLabel = QLabel()
        self.totalRecordLabel.setFixedWidth(70)

        statusLayout.addWidget(self.totalPageLabel)
        statusLayout.addWidget(self.currentPageLabel)
        statusLayout.addWidget(QSplitter())
        statusLayout.addWidget(self.totalRecordLabel)

        # 设置表格属性
        self.tableView = QTableView()

        # 表格宽度的自适应调整
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 创建图形
        self.graphicsView = pg.GraphicsLayoutWidget()

        # 创建界面
        mainLayout = QVBoxLayout(self)
        mainLayout.addLayout(operatorLayout)
        mainLayout.addWidget(self.tableView)        #加入表格
        mainLayout.addLayout(temperatureLayout)
        mainLayout.addLayout(pressureLayout)
        mainLayout.addLayout(flowLayout)
        mainLayout.addLayout(addressLayout)
        mainLayout.addWidget(self.graphicsView)     #加入曲线
        mainLayout.addLayout(statusLayout)
        self.setLayout(mainLayout)

    def setTableView(self):

        # 声明查询模型
        self.queryModel = QSqlQueryModel(self)

        # 设置当前页
        self.currentPage = 1

        # 得到总记录数
        self.totalRecrodCount = self.getTotalRecordCount()

        # 得到总页数
        self.totalPage = self.getPageCount()

        # 刷新状态
        self.updateStatus()

        # 设置总页数文本
        self.setTotalPageLabel()

        # 设置总记录数
        self.setTotalRecordLabel()

        # 记录查询
        self.recordQuery(0)

        # 设置模型
        self.tableView.setModel(self.queryModel)
        print('totalRecrodCount=' + str(self.totalRecrodCount))
        print('totalPage=' + str(self.totalPage))

        # 设置表格表头
        self.queryModel.setHeaderData(0, Qt.Horizontal, "设备编号")
        self.queryModel.setHeaderData(1, Qt.Horizontal, "采集时间")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "压力")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "温度")
        self.queryModel.setHeaderData(4, Qt.Horizontal, "流量")
        self.queryModel.setHeaderData(5, Qt.Horizontal, "地址")

    # 得到记录数
    def getTotalRecordCount(self):
        self.queryModel.setQuery("select * from device")
        rowCount = self.queryModel.rowCount()
        print('rowCount=' + str(rowCount))
        return rowCount

    # 得到页数
    def getPageCount(self):
        if self.totalRecrodCount % self.PageRecordCount == 0:
            return (self.totalRecrodCount / self.PageRecordCount)
        else:
            return (self.totalRecrodCount / self.PageRecordCount + 1)

    # 记录查询
    def recordQuery(self, limitIndex):
        szQuery = ("select * from device limit %d,%d" % (limitIndex, self.PageRecordCount))
        print('query sql=' + szQuery)
        self.queryModel.setQuery(szQuery)

    # 刷新状态
    def updateStatus(self):
        szCurrentText = ("当前第%d页" % self.currentPage)
        self.currentPageLabel.setText(szCurrentText)

        # 设置按钮是否可用
        if self.currentPage == 1:
            self.prevButton.setEnabled(False)
            self.nextButton.setEnabled(True)
        elif self.currentPage == self.totalPage:
            self.prevButton.setEnabled(True)
            self.nextButton.setEnabled(False)
        else:
            self.prevButton.setEnabled(True)
            self.nextButton.setEnabled(True)

    # 设置总数页文本
    def setTotalPageLabel(self):
        szPageCountText = ("总共%d页" % self.totalPage)
        self.totalPageLabel.setText(szPageCountText)

    # 设置总记录数
    def setTotalRecordLabel(self):
        szTotalRecordText = ("共%d条" % self.totalRecrodCount)
        print('*** setTotalRecordLabel szTotalRecordText=' + szTotalRecordText)
        self.totalRecordLabel.setText(szTotalRecordText)

    # 前一页按钮按下
    def onPrevButtonClick(self):
        print('*** onPrevButtonClick ')
        limitIndex = (self.currentPage - 2) * self.PageRecordCount
        self.recordQuery(limitIndex)
        self.currentPage -= 1
        self.updateStatus()

    # 后一页按钮按下
    def onNextButtonClick(self):
        print('*** onNextButtonClick ')
        limitIndex = self.currentPage * self.PageRecordCount
        self.recordQuery(limitIndex)
        self.currentPage += 1
        self.updateStatus()

    # 转到页按钮按下
    def onSwitchPageButtonClick(self):

        # 得到输入字符串
        szText = self.switchPageLineEdit.text()

        # 得到页数
        pageIndex = int(szText)

        # 判断是否有指定页
        if pageIndex > self.totalPage or pageIndex < 1:
            QMessageBox.information(self, "提示", "没有指定的页面，请重新输入")
            return

        # 得到查询起始行号
        limitIndex = (pageIndex - 1) * self.PageRecordCount

        # 记录查询
        self.recordQuery(limitIndex)

        # 设置当前页
        self.currentPage = pageIndex

        # 刷新状态
        self.updateStatus()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建窗口
    example = DataGrid()

    # 显示窗口
    example.show()
    sys.exit(app.exec_())