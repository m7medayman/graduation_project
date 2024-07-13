import time as ti
from gpio_module.filter import KFilter ,MeanFilter,HighPassFilter,LowPassFilter,ChangeFilter
from gpio_module.vlx1_tof_sensor.vlx_module import VlxModule
class PlayerYController:
    def __init__(self)->None:
        self.vlxModule=VlxModule()
        self._sensorXFilter=KFilter(value=self.vlxModule.getSensorX())
        self._sensorYFilter=KFilter(value=self.vlxModule.getSensorY())
        self._sensorXValue=self._sensorXFilter.stimate(self.vlxModule.getSensorX())
        self._sensorYValue=self._sensorYFilter.stimate(self.vlxModule.getSensorY())
        self.LPFX=LowPassFilter(alpha=0.5)
        self.LPFY=LowPassFilter(alpha=0.5)
        self.LPFXabs=LowPassFilter(alpha=0.5)
        self.LPFYabs=LowPassFilter(alpha=0.5)
        self.meanFilterX=MeanFilter(value=self._sensorXValue,sampleNumber=5)
        self.meanFilterY=MeanFilter(value=self._sensorYValue,sampleNumber=5)
        self.maxPlayerPostionX=200
        self.maxPlayerPostionY=200
        
    
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
        self._sensorXValue=self.getMeanFilterX()
        return int(self._sensorXValue)
    
    def getSensorY(self):
        self._sensorYValue=self.getMeanFilterY()
        return int(self._sensorYValue)
    def getSensorXAbs(self):
        v=self.vlxModule.getSensorXAbs()
        value=self.LPFXabs.apply(v)
        return value
    def getSensorYAbs(self):
        v=self.vlxModule.getSensorYAbs()
        value=self.LPFYabs.apply(v)
        return value

    def _updateSensors(self):
        valueX=self.vlxModule.getSensorX()
        valueY=self.vlxModule.getSensorY()
        fx= self._sensorXFilter.stimate(valueX)
        fy= self._sensorYFilter.stimate(valueY)
        self.LPFX.apply(fx)
        self.LPFY.apply(fy)
    def updateLoop(self):
        self._updateSensors()
    def getFilterdX(self):
        value=self._sensorXFilter.stimate(self.vlxModule.getSensorX())
        filterdValue=self.LPFX.apply(value)
        return filterdValue 
    def getFilterdY(self):
        value=self._sensorYFilter.stimate(self.vlxModule.getSensorY())
        filterdValue=self.LPFY.apply(value)
        return filterdValue 
    def getMeanFilterX(self):
        value=self.getFilterdX()
        fv= self.meanFilterX.getTheMean(value)
        return fv
    def getMeanFilterY(self):
        value=self.getFilterdY()
        fv= self.meanFilterY.getTheMean(value)
        return fv
    

    def getPosstionX(self):
        ## that mean 0 will out  0.5 
        # the range will be between -100 to 100 becase the max is 200
        miniRange=self.maxPlayerPostionX//2
        xSensor=self.vlxModule.getSensorX()
        value=xSensor+miniRange
        value=value/self.maxPlayerPostionX
        
        if(value>1):
            return 1
        if value<0:
            return 0
        return value        
    def reset(self):
        self.vlxModule.reset()
    def close(self):
        self.vlxModule.kill()


        