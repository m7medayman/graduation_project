import sys
sys.path.append('/home/pi/body balance seeker/i2c_port')
from module import SerialPort

class  SensorInput:
    def __init__(self) -> None:
        self.serialPort= SerialPort()
        self.maxValue=1024
    def getVlaue(self):
        #in this function we will get the gyro value and change it to be the range form (0,1)
        sensorValue= self.serialPort.getSensorValue()
        return sensorValue/self.maxValue
