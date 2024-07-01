import queue
import threading
import time
from .vlx_gpio_configration import VlxGpioInput
class VlxModule():
    def __init__(self)->None:
        self.queue1 = queue.Queue()
        self.queue2 = queue.Queue()
        self._centerX=0
        self._centerY=0
        self.start_reading()
    
    def getSensorX(self):
        sensorRead = self.getFirstSensorValue()
        return round(self._centerX - sensorRead, 3)

    def getSensorY(self):
        sensorRead = self.getSecondSensorValue()
        return round(self._centerY - sensorRead, 3)
    def getSensorOneAbs(self):
        return self.getFirstSensorValue()
    def getSensorTwoAbs(self):
        return self.getSecondSensorValue
    def setCenterX(self,newCenterX:float):
        self._centerX=newCenterX
    def setCenterY(self,newCenterY:float):
        self._centerY=newCenterY
    def start_reading(self):
        self.running = True
        threading.Thread(target=self._read_loop).start()
    
    def _read_loop(self):
        self.vlxSensor= VlxGpioInput()
        while self.running:
            print("running")
            new_value1 = self.vlxSensor.getFirstSensorGpio()
            new_value2 = self.vlxSensor.getSecondSensorFromGpio()
            self.queue1.put(new_value1)
            self.queue2.put(new_value2)
            time.sleep(0.01)  # Adjust the delay as needed

    def getFirstSensorValue(self) -> float:
        try:
            value = self.queue1.get()
            if isinstance(value, float):
                return float(f"{value:.3f}")
            else:
                return -1
        except queue.Empty:
            return -1
        
    def getSecondSensorValue(self) -> float:
        try:
            value = self.queue2.get()
            if isinstance(value, float):
                return float(f"{value:.3f}")
            else:
                return -1
        except queue.Empty:
            return -1