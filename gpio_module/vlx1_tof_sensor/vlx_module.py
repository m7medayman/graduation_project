import inspect
import queue
import threading
import time
from .vlx_gpio_configration import VlxGpioInput
from gpio_module.filter import KFilter ,MeanFilter,HighPassFilter,LowPassFilter,ChangeFilter
import ctypes

class VlxModule():
    def __init__(self)->None:

        self.dataX = queue.Queue()
        self.dataY = queue.Queue()
        self._centerX=0
        self._centerY=0
        self.LPFX=LowPassFilter(alpha=0.5)
        self.LPFY=LowPassFilter(alpha=0.5)
        self.meanFilterX=MeanFilter(value=0,sampleNumber=5)
        self.meanFilterY=MeanFilter(value=0,sampleNumber=5)
        self.stop_event = threading.Event()
        
        
        self.start_reading()
   
        
    
    def getSensorX(self):
        sensorRead = self.getFirstSensorValue()
        return round( sensorRead-self._centerX, 3)

    def getSensorY(self):
        sensorRead = self.getSecondSensorValue()
        return round(sensorRead-self._centerY, 3)
    def getSensorOneAbs(self):
        sensorRead = self.getFirstSensorValue()
        return sensorRead
    def getSensorTwoAbs(self):
        sensorRead = self.getSecondSensorValue()
        return sensorRead
    def setCenterX(self,newCenterX:float):
        self._centerX=newCenterX
        print(f"new centerx={self._centerX}")
    def setCenterY(self,newCenterY:float):
        self._centerY=newCenterY
        print(f"new centery={self._centerY}")
    def start_reading(self):
        self.running = True
        threading.Thread(target=self._read_loop).start()
    
    def _read_loop(self):
        self.vlxSensor= VlxGpioInput()
        while self.running and not self.stop_event.is_set():
            new_valueX = self.vlxSensor.getFirstSensorGpio()
            newValueY = self.vlxSensor.getSecondSensorFromGpio()
            newXFilterd=self._getFilterXsensor(new_valueX)
            newYFilterd=self._getFilterYsensor(newValueY)
            self.dataX.put(newXFilterd)
            self.dataY.put(newYFilterd)
            # print("running")
            # time.sleep(0.0001)  # Adjust the delay as needed

    def getFirstSensorValue(self) -> float:
        try:
            value = self.dataX.get()

            if isinstance(value, float):
                return float(f"{value:.3f}")
            else:
                return -1
        except queue.Empty:
            return -1
        
    def getSecondSensorValue(self) -> float:
        try:
            value = self.dataY.get()
            if isinstance(value, float):
                return float(f"{value:.3f}")
            else:
                return -1
        except queue.Empty:
            return -1
    def _getFilterXsensor(self,x):
        xValue=x
        LXV=self.LPFX.apply(xValue)
        MXV=self.meanFilterX.getTheMean(LXV)
        return MXV
    def _getFilterYsensor(self,y):
        yValue=y
        LYV=self.LPFY.apply(yValue)
        MYV=self.meanFilterY.getTheMean(LYV)
        return MYV
    def reset(self):
        self.dataX=queue.Queue()
        self.dataY=queue.Queue()

    def kill(self):
        self.stop_event.set()
    

class Data():
    def __init__(self):
        self._value=0
    def get(self):
        return self._value
    def put(self,v):
        self._value=v
    

