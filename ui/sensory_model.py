import time as ti
from gpio_module.filter import KFilter ,MeanFilter,HighPassFilter,LowPassFilter,ChangeFilter
from gpio_module.vlx1_tof_sensor.vlx_module import VlxModule
class SensoryModel:
    def __init__(self)->None:
        self.vlxModule=VlxModule()
        self._sensorX=KFilter(value=self.vlxModule.getSensorX())
        self._sensorY=KFilter(value=self.vlxModule.getSensorY())
        self.sensorXVlaue=0
        self.sensorYVlaue=0
    
    def setCenter(self):
        meanSensorX=0
        meanSensorY=0
        for i in range(0,50):
            valueX = self.vlxModule.getSensorX
            valueY = self.vlxModule.getSensorY
            meanSensorX+=valueX
            meanSensorY+=valueY
            self.sensorXValue=self.kFilter.stimate(valueX)
            self.sensorYValue=self.kFilter.stimate(valueY)
            ti.sleep(0.001)
        meanSensorX=meanSensorX/50
        meanSensorY=meanSensorY/50
        self.vlxModule.setCenterX(meanSensorX)
        self.vlxModule.setCenterY(meanSensorY)

    def getSensorX(self):
        sensorX=self._sensorX.stimate(self.vlxModule.getSensorX())
        return sensorX
    
    def getSensorY(self):
        sensorY=self._sensorX.stimate(self.vlxModule.getSensorY())
        return sensorY

    def _updateSensors(self):
        self.sensorXValue=self._sensorX.stimate(self.vlxModule.getSensorX())
        self.sensorYValue=self._sensorY.stimate(self.vlxModule.getSensorY())

    def updateLoop(self):
        self._updateSensors()



        