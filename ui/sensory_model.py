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
        for i in range(0,50):
            valueX = self.getSensorXAbs()
            valueY = self.getSensorYAbs()
            meanSensorX+= valueX
            meanSensorY+=valueY
            ti.sleep(0.001)
        meanSensorX=meanSensorX/50
        meanSensorY=meanSensorY/50
        self.vlxModule.setCenterX(meanSensorX)
        self.vlxModule.setCenterY(meanSensorY)
        

    def getSensorX(self):
        
        self._sensorXValue=self._sensorXFilter.stimate(self.vlxModule.getSensorX())
        return int(self._sensorXValue)
    
    def getSensorY(self):
        self._sensorYValue=self._sensorYFilter.stimate(self.vlxModule.getSensorY())
        return int(self._sensorYValue)
    def getSensorXAbs(self):
        value=self.vlxModule.getSensorOneAbs()
        return value
    def getSensorYAbs(self):
        value=self.vlxModule.getSensorTwoAbs()
        return value

    def _updateSensors(self):
        valueX=self.vlxModule.getSensorX()
        valueY=self.vlxModule.getSensorY()
    def updateLoop(self):
        self._updateSensors()

        