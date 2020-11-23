import serial
import serial.tools.list_ports
from myMainWindow import Pyqt5_Serial


# 获得接收数据
def data_receive():
    try:
        num = serial.Serial().inWaiting()
    except:
        Pyqt5_Serial.port_close()
        return None
    if num > 0:
        data = serial.Serial().read(num)
        # hex显示
        if Pyqt5_Serial.hex_receive.checkState():
            out_s = ''
            for i in range(0, len(data)):
                out_s = out_s + '{:02X}'.format(data[i]) + ' '
            #self.s2__receive_text.insertPlainText(out_s)

        else:
            out_s = data.decode('iso-8859-1')
            # 串口接收到的字符串为b'123',要转化成unicode字符串才能输出到窗口中去
            #self.s2__receive_text.insertPlainText(data.decode('iso-8859-1'))

