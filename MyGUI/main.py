import  sys
import  serial
import  threading


class Uart(object):
    def __init__(self,port,baud):
        self.err = 0
        # open serial
        try:
            self.serial = serial.Serial(port,baud)
            print("open serial success")
        except:
            print("open serial error")
            self.err = -1

    def start_recv_thread(self):
        pass

if __name__ == '__main__':
    myuart = Uart("COM4",9600)
    if (0 == myuart.err):
        print("Init Uart Success")

    #如果打开串口成功，启动接收线程，准备实时的接收数据
    myuart.start_recv_thread()

    while(True):
        input_data = input("please input data...")
        if(input_data == "quit"):
            #退出
            pass
            break
        else:
            #发送数据给设备
            pass

    print("")
