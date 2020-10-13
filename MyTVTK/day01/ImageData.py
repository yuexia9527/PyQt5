from tvtk.api import tvtk

img = tvtk.ImageData(spacing=(1, 1, 1), origin=(1, 2, 3), dimensions=(3, 4, 5))
print(img.get_point(0))

for n in range(6):
    print("%.1f,%.1f,%.1f" % img.get_point(n))
