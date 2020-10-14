from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection = '3d')

# Make the grid
x,y,z = np.meshgrid(np.array([1]),
                    np.array([1]),
                    np.array([1])) #起点（1,1,1）

# Make the direction data for the arrows
u=np.array([2])
v=np.array([4])
w=np.array([5])  #方向（2,4,5）

ax.quiver(x,y,z,u,v,w,length=1,normalize=True) #模长设置为1
ax.set_xlim(0,2)
ax.set_ylim(0,2)
ax.set_zlim(0,2)
plt.show()

