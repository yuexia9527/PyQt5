import numpy as np

def extract_data():
    file = open("Magnetic positioning.txt", "r")
    list_arr = file.readlines() #读取数据文件的每一行

    lists = [] #生成列表

    for index, x in enumerate(list_arr):
        x = x.strip()
        x = x[:-1]
        x = x.strip('[]')
        x = x.split(", ")
        lists.append(x)
    array = np.array(lists)
    array = array.astype(float)
    print(array)

if __name__ == '__main__':

    extract_data()