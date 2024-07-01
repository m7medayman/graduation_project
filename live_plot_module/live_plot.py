from .modle import TimeLine , XAxsis
import pyqtgraph as pg

class LivePlot:
    def __init__(self,win:pg.GraphicsLayoutWidget,row,col) -> None:
        self.timeLine=TimeLine(intervalLength=50)
        self.xAxsis=XAxsis(intervalLength=50)
        self.win=win
        self.p=self.win.addPlot(row=row,col=col)
        self.curve = self.p.plot()
    def update(self,currentValue):
        t=self.timeLine.run()
        x=self.xAxsis.run(currentValue)
        self.curve.setData(t,x)
    
