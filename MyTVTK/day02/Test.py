# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication

from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication

from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import sys
import vtk
from tvtk.api import tvtk
from tvtkfunc import ivtk_scene, event_loop



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(603, 553)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.gridlayout = QtWidgets.QGridLayout(self.centralWidget)
        self.vtkWidget = QVTKRenderWindowInteractor(self.centralWidget)
        self.gridlayout.addWidget(self.vtkWidget, 0, 0, 100, 100)
        self.buttonLeft = QtWidgets.QPushButton("Left")
        self.gridlayout.addWidget(self.buttonLeft, 96, 48, 1, 1)
        self.buttonRight = QtWidgets.QPushButton("Right")
        self.gridlayout.addWidget(self.buttonRight, 96, 52, 1, 1)
        self.buttonUp = QtWidgets.QPushButton("Up")
        self.gridlayout.addWidget(self.buttonUp, 94, 50, 1, 1)
        self.buttonDown = QtWidgets.QPushButton("Down")
        self.gridlayout.addWidget(self.buttonDown, 98, 50, 1, 1)
        self.buttonFire = QtWidgets.QPushButton("Fire Torpedo")
        self.gridlayout.addWidget(self.buttonFire, 95, 50, 3, 1)
        MainWindow.setCentralWidget(self.centralWidget)



class SimpleView(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ren = tvtk.Renderer()
        self.ui.tvtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.ui.tvtkWidget.GetRenderWindow().GetInteractor()

        # Create source
        source = tvtk.STLReader(file_name="robot.STL")

        # Create a mapper
        mapper = tvtk.PolyDataMapper(input_connection=source.output_port)

        # Create an actor
        actor = tvtk.Actor(mapper=mapper)
        self.ren.AddActor(actor)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleView()
    window.show()
    window.iren.Initialize()  # Need this line to actually show the render inside Qt
    sys.exit(app.exec_())
