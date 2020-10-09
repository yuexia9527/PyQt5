from tvtk.api import tvtk


s = tvtk.CubeSource(x_length = 1.0, y_length = 2.0, z_length = 3.0)
print(s)

print(s.x_length)

