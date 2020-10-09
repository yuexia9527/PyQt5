from tvtk.api import tvtk
from tvtkfunc import ivtk_scene,event_loop

# 创建一个长方体数据源，并且设置其长宽高
s = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)
# 使用PolyDataMapper将数据转换为图形数据
m = tvtk.PolyDataMapper(input_connection=s.output_port)
# 创建一个Actor
a = tvtk.Actor(mapper=m)
win = ivtk_scene(a)
win.scene.isometric_view()
event_loop()
