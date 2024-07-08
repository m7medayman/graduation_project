import sys
import os
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QFrame
import pyqtgraph as pg
from pyqtgraph import PlotWidget
if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QFrame, QPushButton
from PyQt5.QtCore import QTimer
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class BarChartWidget(QWidget):
    def __init__(self, percentages):
        super().__init__()
        self.percentages = percentages
        self.initUI()

    def initUI(self):
        # Create a Figure object
        self.figure = Figure()

        # Create a FigureCanvas object and add it to the layout
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        # Plot the bar chart
        self.plot_bar_chart()

    def plot_bar_chart(self):
        ax = self.figure.add_subplot(111)
        ax.clear()

        # Set background color
        self.figure.patch.set_facecolor('black')
        ax.set_facecolor('black')

        # Create the bar chart
        categories = [f"Item {i+1}" for i in range(len(self.percentages))]
        bars = ax.bar(categories, self.percentages, color='gray')

        # Customize chart elements
        ax.set_title("Percentages Bar Chart", color='gray')
        ax.set_xlabel("Items", color='gray')
        ax.set_ylabel("Percentage", color='gray')
        ax.set_ylim(0, 100)

        # Customize tick labels
        ax.tick_params(axis='x', colors='gray')
        ax.tick_params(axis='y', colors='gray')

        # Customize spines
        ax.spines['bottom'].set_color('gray')
        ax.spines['top'].set_color('gray')
        ax.spines['left'].set_color('gray')
        ax.spines['right'].set_color('gray')

        # Draw the canvas
        self.canvas.draw()

    def update_chart(self, new_percentages):
        self.percentages = new_percentages
        self.plot_bar_chart()

class MainWindow(QMainWindow):
    def __init__(self, percentages):
        super().__init__()
        self.setWindowTitle("Bar Chart Example")
        self.setGeometry(100, 100, 800, 600)
        self.initUI(percentages)

    def initUI(self, percentages):
        # Create a frame
        frame = QFrame(self)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setGeometry(50, 50, 700, 500)  # Adjust the position and size as needed

        # Set layout for the frame
        frame_layout = QVBoxLayout()
        frame.setLayout(frame_layout)

        # Create and add the bar chart widget to the frame
        self.bar_chart_widget = BarChartWidget(percentages)
        frame_layout.addWidget(self.bar_chart_widget)

        # Add an update button
        update_button = QPushButton("Update Chart", self)
        update_button.setGeometry(50, 570, 100, 30)  # Adjust the position and size as needed
        update_button.clicked.connect(self.update_chart)

        # Set up a timer for periodic updates
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_chart)
        self.timer.start(5000)  # Update every 5 seconds

    def update_chart(self):
        # Generate new random percentages for demonstration
        new_percentages = [random.randint(0, 100) for _ in range(7)]
        self.bar_chart_widget.update_chart(new_percentages)

if __name__ == '__main__':
    import random

    app = QApplication(sys.argv)

    # Initial list of percentages
    percentages = []

    main_window = MainWindow(percentages)
    main_window.show()

    sys.exit(app.exec_())