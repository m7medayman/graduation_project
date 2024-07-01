class TimeLine:
    def __init__(self,intervalLength):
        self.intervalLength=intervalLength
        self.startTime=0
        self.currentTime=0
        self.timeLine=[self.startTime]

    def whenTimeExceededInterval(self):
        if(len(self.timeLine)>self.intervalLength):
            self.timeLine.pop(0)
    def run(self):
        self.whenTimeExceededInterval()
        self.currentTime+=1
        self.timeLine.append(self.currentTime)
        return self.timeLine


class XAxsis:
    def __init__(self,intervalLength):
        self.intervalLength=intervalLength
        self.startValue=0
        self.currentValue=0
        self.vlaueLine=[self.startValue]

        
    def whenTimeExceededInterval(self):
        if(len(self.vlaueLine)>self.intervalLength):
            self.vlaueLine.pop(0)
    def run(self,currentValue):
        self.whenTimeExceededInterval()
        self.currentValue=currentValue
        self.vlaueLine.append(self.currentValue)
        return self.vlaueLine
