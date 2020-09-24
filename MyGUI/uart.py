import sys
import serial
import threading
from time import sleep


class Uart(object):
    def __init__(self, port, baud):
        self.err = 0
        # open serial
        try:
            self.serial = serial.Serial(port, baud)
            print("open serial success")
        except:
            print("open serial error")
            self.err = -1

    def uart_recv_thread(self):
        print("start uart_recv_thread")

        while (True):
            try:
                recv_data_raw = self.serial.readline()
                data = recv_data_raw.decode()
                if self.queue_recv.full():
                    self.queue_recv.get()
                self.queue_recv.put(data)
                data = "DEVICE---->PC:" + data
                print(data)
            except:
                print("receive data error")
                break

    def start_recv_thread(self):
        thread = threading.Thread(target=self.uart_recv_thread, daemon=True)
        thread.start()

    def send_uart_data(self,data):
        self.serial.write(data.encode())

    def uart_close(self):
        self.serial.close()

    def flush_queue_recv(self):
        while not self.queue_recv.empty():
            self.queue_recv.get()

    def is_queue_recv_empty(self):
        return self.queue_recv.empty()

    def get_queue_recv(self):
        return self.queue_recv.get()



# if __name__ == '__main__':
#     myuart = Uart("COM4", 9600)
#     if (0 == myuart.err):
#         print("Init Uart Success")
#
#     # 如果打开串口成功，启动接收线程，准备实时的接收数据
#     myuart.start_recv_thread()
#
#     while (True):
#         input_data = input("please input data...")
#         if (input_data == "quit"):
#             # 退出
#             myuart.uart_close()
#             break
#         else:
#             # 发送数据给设备
#             myuart.send_uart_data(input_data)
#         sleep(0.01)
#
#     print("exit")
