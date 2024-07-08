from person import Person


class TestModel():
    def __init__(self,person:Person,period:float) -> None:
        self.person=person
        self._period=period
        self._isrunning=False
        self._currentTestNumber=0
        self._testsNumber=2
        self._currentTime=0
        self._xData=[]
        self._yData=[]
    def _runTest(self):
        self._isrunning=True
        self._xData=[]
        self._yData=[]
    def _endWithOutSavign(self):
        self._isrunning=False
        self._currentTime=0
    def startButtonFunction(self):
        if(self._isrunning):
            self._endWithOutSavign()
        else:
            if(self._currentTestNumber<self._testsNumber):
                self._runTest()
            else:
                self.exportData()
    def _endTest(self):
        self._isrunning=False
        self._currentTestNumber+=1
        self.person.addTest(xData=self._xData,yData=self._yData)
        self._currentTime=0
    def updateLoop(self,xRead,yRead):
        if(self._isrunning and self._currentTime<self._period):
            self.attachDataToPerson(xRead=xRead,yRead=yRead)
            self._currentTime+=1
        if(self._currentTime>=self._period):
            self._endTest()

    def attachDataToPerson(self,xRead,yRead):
        self._xData.append(xRead)
        self._yData.append(yRead)
       
    def exportData(self):
        self.person.exportAllPersonData()
        self._currentTestNumber=0
    def getTestTimepercent(self):
        value=(self._currentTime/self._period)*100
        return int(value)
    def getSatausText(self):
        if(self._isrunning):
            return "stop test"
        else:
            if(self._currentTestNumber<self._testsNumber):
                return "run test"
            else:
                return "export data"
    def getCurrentTestNumber(self):
        return self._currentTestNumber