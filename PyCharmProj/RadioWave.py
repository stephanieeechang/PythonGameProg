import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDockWidget, QHBoxLayout
import pyqtgraphdev.pyqtgraph as pt
from pyqtgraphdev.pyqtgraph import PlotWidget
import numpy as np
import time

class CosGraph(QDockWidget):
    def __init__(self, parent=None):
        super(CosGraph, self).__init__(parent=parent)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        # container for cosine graph
        self.host = QtWidgets.QWidget(self)
        self.host.setObjectName("hostCosine")
        self.host.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        self.host.setMinimumSize(200, 400)
        # define the graph
        self.graph = PlotWidget(self)
        # horizontal, vertical lines, thickness
        self.graph.plotItem.showGrid(True, True, 0.7)
        self.setObjectName("cosplot")
        self.graph.raise_()
        # add graph container to layout
        self.horizontalLayout = QHBoxLayout(self.host)
        self.horizontalLayout.addWidget(self.graph)

    def plot(self, data):
        """
        :param data: dictionary with x, y data
        :return: none
        """
        X = data['X']
        Y = data['Y']
        colorLine = data['pen']
        self.graph.plot(X, Y, pen=colorLine, clear=True)

    def resizeEvent(self, e):
        self.host.setGeometry(10, 10, e.size().width(), e.size().height())
        self.graph.setGeometry(10, 10, e.size().width(), 0.9*e.size().height())


class SinGraph(QDockWidget):
    def __init__(self, parent=None):
        super(SinGraph, self).__init__(parent=parent)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        # container for sine graph
        self.host = QtWidgets.QWidget(self)
        self.host.setObjectName("hostSine")
        self.host.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        self.host.setMinimumSize(200, 400)
        # define the graph
        self.graph = PlotWidget(self)
        # horizontal, vertical lines, thickness
        self.graph.plotItem.showGrid(True, True, 0.7)
        self.setObjectName("sinplot")
        self.graph.raise_()
        # add graph container to layout
        self.horizontalLayout = QHBoxLayout(self.host)
        self.horizontalLayout.addWidget(self.graph)

    def plot(self, data):
        """
        :param data: dictionary with x, y data
        :return: none
        """
        X = data['X']
        Y = data['Y']
        colorLine = data['pen']
        self.graph.plot(X, Y, pen=colorLine, clear=True)

    def resizeEvent(self, e):
        self.host.setGeometry(10, 10, e.size().width(), e.size().height())
        self.graph.setGeometry(10, 10, e.size().width(), 0.9*e.size().height())


class RadioGraph(QDockWidget):
    def __init__(self, parent=None):
        super(RadioGraph, self).__init__(parent=parent)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        # container for cosine graph
        self.host = QtWidgets.QWidget(self)
        self.host.setObjectName("hostRadio")
        self.host.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        self.host.setMinimumSize(200, 400)
        # define the graph
        self.graph = PlotWidget(self)
        # horizontal, vertical lines, thickness
        self.graph.plotItem.showGrid(True, True, 0.7)
        self.setObjectName("radioplot")
        self.graph.raise_()
        # add graph container to layout
        self.horizontalLayout = QHBoxLayout(self.host)
        self.horizontalLayout.addWidget(self.graph)

    def plot(self, data):
        """
        :param data: dictionary with x, y data
        :return: none
        """
        X = data['X']
        Y = data['Y']
        colorLine = data['pen']
        self.graph.plot(X, Y, pen=colorLine, clear=True)

    def resizeEvent(self, e):
        self.host.setGeometry(10, 10, e.size().width(), e.size().height())
        self.graph.setGeometry(10, 10, e.size().width(), 0.9*e.size().height())


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks | QtWidgets.QMainWindow.AnimatedDocks)
        # create docks
        self.dockCos = CosGraph()
        self.dockSin = SinGraph()
        self.dockRadio = RadioGraph()
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dockCos)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dockSin)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dockRadio)
        self.update()

    def update(self):
        Npoints = 2000
        f_m = 0.1
        f_c = 1
        A = 5
        M = 0.8
        X = np.arange(0, 20, 20/Npoints)
        Ycos = np.cos(2*np.pi*f_m*X)
        Ysin = A*np.sin(2*np.pi*f_c*X)
        Yradio = (1+M*np.cos(2*np.pi*f_m*X))*A*np.sin(2*np.pi*f_c*X)
        # change color every second
        c = pt.hsvColor(time.time() / 5%1, alpha=.5)
        pen = pt.mkPen(color=c, width=2)
        cosdata = {'X':X, 'Y':Ycos, 'pen':pen}
        sindata = {'X':X, 'Y':Ysin, 'pen':pen}
        radiodata = {'X':X, 'Y':Yradio, 'pen':pen}
        self.dockCos.plot(cosdata)
        self.dockSin.plot(sindata)
        self.dockRadio.plot(radiodata)
        # refresh
        QtCore.QTimer.singleShot(100, self.update)


class SandBoxApp(QtWidgets.QApplication):
    # define class constructor
    def __init__(self, *args, **kwargs):
        super(SandBoxApp, self).__init__(*args)
        self.mainwindow = MainWindow()
        self.mainwindow.setGeometry(50, 100, 1200, 750)
        self.mainwindow.show()
        # disable context menu (the menu that appears when user right clicks mouse)
        self.mainwindow.setContextMenuPolicy(Qt.NoContextMenu)


# entry point for Python program
def main():
    app = SandBoxApp(sys.argv)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
