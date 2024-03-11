from pyqtgraph.Qt import QtGui

from PyQt5.QtWidgets import QApplication
import pyqtgraph as pg
import numpy as np
import os
import mpu6050
from numpy import linspace
from filterpy.kalman import KalmanFilter
import sys
sys.path.append('/home/pi/body balance seeker/plot_module/live_plot_module ')
from live_plot import LivePlot


if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


# Create a Kalman filter object for a one-dimensional system
kf = KalmanFilter(dim_x=1, dim_z=1)

# Define the state transition matrix (assume constant acceleration)
dt = 1.0  # Time step
kf.F = np.array([[1]])

# Define the measurement function
kf.H = np.array([[1]])

# Define the measurement noise covariance matrix
kf.R = 1  # Measurement noise (adjust as needed)

# Define the process noise covariance matrix
q = 0.1  # Process noise (adjust as needed)
kf.Q = np.array([[q]])

# Initialize the state estimate and covariance matrix
kf.x = np.array([0])  # Initial acceleration estimate
kf.P *= 1000  # Initial covariance matrix


# Initialize the MPU6050 sensor
mpu6050 = mpu6050.mpu6050(0x68, bus=0)
app = QApplication([])
# Create a window for the plot

win = pg.GraphicsLayoutWidget(title="Signal from serial port",size=(700,500))
livePlot=LivePlot(win=win,row=0,col=0)
# # Create a plot in the window
# p = win.addPlot(title="Realtime plot",row=0,col=0)
# p2 = win.addPlot(title="Realtime plot",row=2,col=0)
# # Create a curve for the plot
# curve = p.plot()
# curve1=p2.plot()
# windowWidth = 800
# Xm = linspace(0, 0, windowWidth)
# sXm=linspace(0, 0, windowWidth)
# t=linspace(0, windowWidth, windowWidth)
# Function to read sensor data
def read_sensor_data():
    accelerometer_data = list(mpu6050.get_accel_data().values())
    return accelerometer_data
def stimate(v):
    global kf
    kf.predict()
    # Update with the new measurement
    kf.update(v)
    return kf.x[0]

# Function to update the plot
def update():
    # global curve, Xm,sXm,t
    # Xm[:-1] = Xm[1:]
    # sXm[:-1] = sXm[1:]
    value = read_sensor_data()[0]
    # svalue= stimate(value)
    # Xm[-1] = float(value)
    # sXm[-1]=float(svalue)
    # print(f"vlaue:{value}")
    # print(f"sValue: {svalue}")
    # print("*****************")
    # curve.setData(t,Xm )
    # curve1.setData(sXm)
    livePlot.update(value)

# Timer for updating the plot
timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)  # Update plot every 50 milliseconds

# Show the plot window
win.showMaximized()

# Start the Qt event loop
app.exec_()