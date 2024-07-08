from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QFrame
import numpy as np
import pyqtgraph as pg
from pyqtgraph import PlotWidget


class PointPlotWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.maxX=400 # 400 mm range for sensor x 
        self.maxY=400 # 400 mm range for sensor y

        # Initialize GUI
        self.initUI()

    def initUI(self):
        # Set up the layout
        layout = QVBoxLayout(self)
        self.setLayout(layout)

        # Create a plot widget
        self.plotWidget = PlotWidget()
        layout.addWidget(self.plotWidget)


        # Remove the grid
        self.plotWidget.showGrid(x=False, y=False)

        # Initialize plot data
        self.scatter = self.plotWidget.plot([], [], pen=None, symbol='o', symbolPen=None, symbolSize=15, symbolBrush=(255, 0, 0))

        # Draw axes lines and circles
        self.drawAxes()
        self.drawCircles()

        # Set axis ranges
        self.plotWidget.setXRange(-5, 5)
        self.plotWidget.setYRange(-5, 5)

        # Initialize point position
        self.x = 0
        self.y = 0

        # Update plot timer
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.updatePlot)
        self.timer.start(50)  # Update plot every 50 ms

    def drawAxes(self):
        # Draw the x-axis line
        x_axis_pen = pg.mkPen(color=(0, 0, 255), width=1)  # Blue color, bold line
        self.plotWidget.plot([-5, 5], [0, 0], pen=x_axis_pen)

        # Draw the y-axis line
        y_axis_pen = pg.mkPen(color=(0, 0, 255), width=1)  # Blue color, bold line
        self.plotWidget.plot([0, 0], [-5, 5], pen=y_axis_pen)

    def drawCircles(self):
        for radius in range(1, 5):
            theta = np.linspace(0, 2 * np.pi, 100)
            x = radius * np.cos(theta)
            y = radius * np.sin(theta)
            circle_pen = pg.mkPen(color=(0, 0, 255), width=1)  # Blue circles with width 1
            self.plotWidget.plot(x, y, pen=circle_pen)

    def updatePlot(self):
        # Update plot data
        self.scatter.setData([self.x], [self.y])

    def setPosition(self, x, y):
        self.x = (x/self.maxX)*5
        self.y = (y/self.maxY)*5