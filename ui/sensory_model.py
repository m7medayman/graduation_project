import time as ti
from gpio_module.filter import KFilter ,MeanFilter,HighPassFilter,LowPassFilter,ChangeFilter
from gpio_module.vlx1_tof_sensor.vlx_module import VlxModule
class SensoryModel:
    def __init__(self)->None:
        self.vlxModule=VlxModule()
        self._sensorXFilter=KFilter(value=self.vlxModule.getSensorX())
        self._sensorYFilter=KFilter(value=self.vlxModule.getSensorY())
        self.sensorXValue=0
        self.sensorYValue=0
    
    def setCenter(self):
        meanSensorX=0
        meanSensorY=0
        self.vlxModule.reset()
        for i in range(0,50):
            valueX = self.vlxModule.getSensorXAbs()
            valueY = self.vlxModule.getSensorYAbs()
            meanSensorX+=valueX
            meanSensorY+=valueY
            self.sensorXValue=self._sensorXFilter.stimate(valueX)
            self.sensorYValue=self._sensorYFilter.stimate(valueY)
            ti.sleep(0.001)
        meanSensorX=meanSensorX/50
        meanSensorY=meanSensorY/50
        self.vlxModule.setCenterX(meanSensorX)
        self.vlxModule.setCenterY(meanSensorY)

    def getSensorX(self):
        sensorX=self._sensorXFilter.stimate(self.vlxModule.getSensorX())
        return sensorX
    
    def getSensorY(self):
        sensorY=self._sensorYFilter.stimate(self.vlxModule.getSensorY())
        return sensorY

    def _updateSensors(self):
        self.sensorXValue=self._sensorXFilter.stimate(self.vlxModule.getSensorX())
        self.sensorYValue=self._sensorYFilter.stimate(self.vlxModule.getSensorY())

    def updateLoop(self):
        self._updateSensors()
    def reset(self):
        self.vlxModule.reset()
    def kill(self):
        self.vlxModule.kill()



        