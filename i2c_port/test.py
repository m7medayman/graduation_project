from pyqtgraph.Qt import QtGui
from PyQt5.QtWidgets import QApplication
import pyqtgraph as pg
import os
import mpu6050
from numpy import linspace

if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

# Initialize the Qt application
app = QApplication([])

# Initialize the MPU6050 sensor
mpu6050 = mpu6050.mpu6050(0x68, bus=0)

# Create a window for the plot
win = pg.GraphicsLayoutWidget(title="Signal from serial port")

# Create a plot in the window
p = win.addPlot(title="Realtime plot")

# Create a curve for the plot
curve = p.plot()

windowWidth = 800
Xm = linspace(0, 0, windowWidth)
ptr = -windowWidth

# Function to read sensor data
def read_sensor_data():
    accelerometer_data = list(mpu6050.get_accel_data().values())
    return accelerometer_data

# Function to update the plot
def update():
    global curve, ptr, Xm
    Xm[:-1] = Xm[1:]
    value = read_sensor_data()[0]
    Xm[-1] = float(value)
    ptr += 1
    curve.setData(Xm)

# Timer for updating the plot
timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)  # Update plot every 50 milliseconds

# Show the plot window
win.show()

# Start the Qt event loop
app.exec_()