from pyqtgraph.Qt import QtGui
from filter import KFilter ,MeanFilter,HighPassFilter,LowPassFilter,ChangeFilter
from PyQt5.QtWidgets import QApplication
import pyqtgraph as pg
import numpy as np
import os
import time
import mpu6050
from numpy import linspace
from filterpy.kalman import KalmanFilter
import sys
sys.path.append('/home/pi/body balance seeker/plot_module/live_plot_module ')
from live_plot import LivePlot


if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')
position=0
speed=0

# Initialize the MPU6050 sensor
mpu6050 = mpu6050.mpu6050(0x68, bus=0)
app = QApplication([])
# Create a window for the plot

win = pg.GraphicsLayoutWidget(title="Signal from serial port",size=(700,500))
livePlot1=LivePlot(win=win,row=0,col=0)
livePlot2=LivePlot(win=win,row=0,col=1)
livePlot3=LivePlot(win=win,row=1,col=0)

def read_sensor_data():
    accelerometer_data = list(mpu6050.get_accel_data().values())
    return accelerometer_data[0]
# Function to update the plot

kFilter=KFilter(value=read_sensor_data())
meanFilter=MeanFilter(value=read_sensor_data(),sampleNumber=3)
# calculate the error position 

for i in range(0,5):
    value = read_sensor_data()
    kValue=kFilter.stimate(value)
    meanValue=meanFilter.getTheMean(kValue)
    time.sleep(0.001)
emean=kValue
print(meanValue)
time=10*0.001
lpf=LowPassFilter(initial_value=emean,alpha=0.7)
cFilter=ChangeFilter(value=emean,sampleNumber=5,tsv=0.1)
# print(ePosition)
def update():
    global speed , position,ePosition,time,emean,cFilter
    value = read_sensor_data()
    kValue=kFilter.stimate(value)
    meanValue=lpf.apply(kValue)-emean
    cfValue=cFilter.getValueCheck(meanValue)
    print(f"Lpf:{meanValue}")
    print(f"cf:{cfValue}")
    speed+=kValue*time
    position+=speed*time+0.5*kValue*time-ePosition
    livePlot1.update(value)
    livePlot2.update(kValue)
    livePlot3.update(cfValue)

# Timer for updating the plot
timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(10)  # Update plot every 50 milliseconds

# Show the plot window
win.showMaximized()

# Start the Qt event loop
app.exec_()