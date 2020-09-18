# 各种 全局变量

# 串口配置的各种变量 包括COM口、波特率、字节数
comport = 'COM5'
baudrate = 38400
bytes = 51
bytes = int(bytes)

# 数据库的写入 信息
# UI显示的全局变量

num_of_device = 0   #设备编号  ，采集时间由time函数提供，不再GL.py中
time_of_collect = 3
temperature = 2
pressure = 33
flow = 44
address = 66
list = [num_of_device, time_of_collect,temperature, pressure, flow, address]  # 数据库格式

# data2 作为串口数据的缓存
data2 = []

x_plot = []
y_plot = []
blue_plot = []