import sys
import serial
import threading
from time import sleep

from uart import Uart


class Tool(object):
    def __init__(self, parent):
        self.err = 0
        self.parent = parent
        print("Tool start.....")
        self.uart = Uart(self.parent.uart_port, self.parent.config_uart_baud)

    def start_listen_uart(self):
        threading.Thread(target=self.listen_uart_data_thread, daemon=True).start()

    def listen_uart_data_thread(self):
        print("start listen_uart_data_thread")
        while (True):
            print("listening...")
            sleep(3)
