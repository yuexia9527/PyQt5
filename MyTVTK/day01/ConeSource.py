from tvtk.api import tvtk

s = tvtk.ConeSource(height = 3.0, radius = 1.0, resolution = 3.0)
print(s.height)
print(s.center)
