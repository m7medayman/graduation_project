from person import Person


class TestModel():
    def __init__(self,person:Person,period:float,hipHight) -> None:
        self.person=person
        self._period=period
        self._isrunning=False
        self._currentTestNumber=0
        self._testsNumber=5
        self._currentTime=0
        self._xData=[]
        self._yData=[]
        self.precentList=[]
        self.isEnd=False
        self.hipHeight=hipHight*100 # to make it mm 
        self.tanAngle12=0.22169466
        self.maxSway=self.hipHeight*self.tanAngle12
        self.condtions=['COND1: Normal Vision , Fixed Support','COND2: Absent Vision , Fixed Support','COND3: Sway Referenced Vision , Fixed Support',
                        'COND4: Normal Vision , Sway Referenced Support','COND5: Absent Vision , Sway Referenced Support','COND6: Sway Referenced Vision , Sway Referenced Support']
    def _runTest(self):
        self._isrunning=True
        self._xData=[]
        self._yData=[]
    def getPrecentList(self):
        return self.precentList
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
        xSensorPrecent=self.getResultPrecent(values=self._xData)
        ySensorPrecent=self.getResultPrecent(values=self._yData)
        print(f'precentx : {xSensorPrecent}')
        print(f'precenty : {ySensorPrecent}')
        totalPrecent=(xSensorPrecent+ySensorPrecent)/2
        self.precentList.append(totalPrecent)
        self._currentTime=0
        self.isEnd=True
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
    def getCondText(self):
        text=self.condtions[self._currentTestNumber]
        return text
    def caluateTheResult(self,maxValue,minValue):
        percent=(self.maxSway-(maxValue-minValue))/self.maxSway
        return percent
    def getResultPrecent(self,values):
        results = 0
        count=0
        for i in range(0, len(values), 10):
            chunk = values[i:i + 10]
            count+=1
            max_value = max(chunk)
            min_value = min(chunk)
            v=self.caluateTheResult(maxValue=max_value,minValue=min_value)
            result +=v  # Example operation (replace with your actual operation)
        return results/count

