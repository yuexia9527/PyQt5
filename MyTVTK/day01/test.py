from numpy import sin, cos
import numpy as np
from mayavi_test import mlab

x, y, z = np.ogrid[-2:2:40j, -2:2:40j, -2:0:40j]# #((40, 1, 1), (1, 40, 1), (1, 1, 40))
s = 2/np.sqrt((x-1)**2 + y**2 + z**2) + 1/np.sqrt((x+1)**2 + y**2 + z**2)#广播运算
"体素呈像没有对应的函数，需要我们自己创建流水线："
field = mlab.pipeline.scalar_field(s)
mlab.pipeline.volume(field, vmin=1.5, vmax=10)#它们指定标量值的润色范围，即只绘制标量值在vmin到vmax之间的区域
mlab.show()