from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

def extract_array():
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
    return array

def plt_show(array):

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Make the grid
    x, y, z = np.meshgrid(np.array([1]),
                          np.array([1]),
                          np.array([1]))  # 起点（1,1,1）

    # Make the direction data for the arrows
    u = np.array([0])
    v = np.array([1])
    w = np.array([1])  # 方向（2,4,5）

    ax.quiver(x, y, z, u, v, w, length=1, normalize=True)  # 模长设置为1
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2)
    ax.set_zlim(0, 2)
    plt.show()
if __name__ == '__main__':
    array = extract_array()
    print(array)
    plt_show(array)
