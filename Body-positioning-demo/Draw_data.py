from extract_array import extract_array
from PyQt5.QtCore import QTimer
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import time
from myMainWindow import Pyqt5_Serial

def draw_data(array):
    for i in range(array.shape[1]):
        plt.plot(array[:,i])
    plt.show()

def save(filename, contents):
    fh = open(filename, 'w')
    fh.write(contents)
    fh.close()

if __name__ == '__main__':
    array = extract_array()
    draw_data(array)