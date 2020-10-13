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

    for index, a in enumerate(array):

        #设置坐标系的显示范围
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_zlim(-10, 10)

        # Make the grid
        x, y, z = np.meshgrid(a[0],a[1],a[2])  # 坐标点（x,y,z）

        # Make the direction data for the arrows
        u = a[3]
        v = a[4]
        w = a[5]  # 方向（u,v,w）

        ax.quiver(x, y, z, u, v, w, length=3, normalize=True)  # 模长设置为1
        plt.show()


if __name__ == '__main__':
    array = extract_array()
    plt_show(array)
