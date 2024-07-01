import time as ti
from gpio_module.filter import KFilter ,MeanFilter,HighPassFilter,LowPassFilter,ChangeFilter
from gpio_module.vlx1_tof_sensor.vlx_module import VlxModule
class SensoryModel:
    def __init__(self)->None:
        self.vlxModule=VlxModule()
        self._sensorXFilter=KFilter(value=self.vlxModule.getSensorX())
        self._sensorYFilter=KFilter(value=self.vlxModule.getSensorY())
        self._sensorXValue=self._sensorXFilter.stimate(self.vlxModule.getSensorX())
        self._sensorYValue=self._sensorYFilter.stimate(self.vlxModule.getSensorY())
        
    
    def setCenter(self):
        meanSensorX=0
        meanSensorY=0
        for i in range(0,20):
            valueX = self.vlxModule.getSensorX
            valueY = self.vlxModule.getSensorY
            self._sensorXValue=self._sensorXFilter.stimate(valueX)
            self._sensorYValue=self._sensorYFilter.stimate(valueY)
            meanSensorX+= self._sensorXValue
            meanSensorY+=self._sensorYValue
            ti.sleep(0.001)
        meanSensorX=meanSensorX/20
        meanSensorY=meanSensorY/20
        self.vlxModule.setCenterX(meanSensorX)
        self.vlxModule.setCenterY(meanSensorY)

    def getSensorX(self):
        self._sensorXValue=self._sensorXFilter.stimate(self.vlxModule.getSensorX())
        print(f"get x:{self._sensorXValue}")
        return round(self._sensorXValue,0)
    
    def getSensorY(self):
        self._sensorYValue=self._sensorYFilter.stimate(self.vlxModule.getSensorY())
        return round(self._sensorYValue,0)

    def _updateSensors(self):
        self._sensorXValue=self._sensorXFilter.stimate(self.vlxModule.getSensorX())
        self._sensorYValue=self._sensorYFilter.stimate(self.vlxModule.getSensorY())

    def updateLoop(self):
        self._updateSensors()



        