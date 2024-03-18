from filterpy.kalman import KalmanFilter
import numpy as np

class KFilter:
    def __init__(self,value) -> None:

        
    # Create a Kalman filter object for a one-dimensional system
        self.kf = KalmanFilter(dim_x=1, dim_z=1)

    # Define the state transition matrix (assume constant acceleration)
        self.dt = 1.0  # Time step
        self.kf.F = np.array([[1]])

    # Define the measurement function
        self.kf.H = np.array([[1]])

    # Define the measurement noise covariance matrix
        self.kf.R = 1  # Measurement noise (adjust as needed)

    # Define the process noise covariance matrix
        self.q = 0.1  # Process noise (adjust as needed)
        self.kf.Q = np.array([[self.q]])

        # Initialize the state estimate and covariance matrix
        self.kf.x = np.array([0])  # Initial acceleration estimate
        self.kf.P *= 1000  # Initial covariance matrix
        self.value=value
    
    def stimate(self, v):
        self.kf.predict()
        # Update with the new measurement
        self.kf.update(v)
        return self.kf.x[0]
class MeanFilter:
    def __init__(self,value,sampleNumber) -> None:
        self.meanValue=value
        self.internalValues=[]
        self.sampleNumber=sampleNumber
        self.currentSample=0
    def getTheMean(self,currentVlaue:float)->float:
        self.internalValues.append(currentVlaue)
        if self.currentSample>=self.sampleNumber:
            self.meanValue=sum(self.internalValues)/len(self.internalValues)
            self.internalValues.pop(0)
            return self.meanValue
        else :
            self.meanValue=sum(self.internalValues)/len(self.internalValues)
            self.currentSample+=1
            return self.meanValue
class HighPassFilter:
    def __init__(self, alpha, initial_value=0):
        self.alpha = alpha
        self.filtered_value = initial_value
    
    def apply(self, value):
        self.filtered_value = self.alpha * (self.filtered_value + value)
        return value - self.filtered_value
        
class LowPassFilter:
    def __init__(self, alpha, initial_value=0):
        self.alpha = alpha
        self.filtered_value = initial_value
    
    def apply(self, value):
        self.filtered_value = self.alpha * value + (1 - self.alpha) * self.filtered_value
        return self.filtered_value
class ChangeFilter:
    def __init__(self,value,sampleNumber,tsv) -> None:
        self.meanValue=value
        self.internalValues=[]
        self.sampleNumber=sampleNumber
        self.currentSample=0
        self.maxV=value
        self.minV=0
        self.tsv=tsv
        
    def getValueCheck(self,currentVlaue:float)->float:
        self.internalValues.append(currentVlaue)
        self.minV=min(self.internalValues,key=abs)
        self.maxV=max(self.internalValues,key=abs)
        self.currentRead=0
        if self.currentSample>=self.sampleNumber:
            self.meanValue=sum(self.internalValues)/len(self.internalValues)
            self.internalValues.pop(0)
        else :
            self.meanValue=sum(self.internalValues)/len(self.internalValues)
            self.currentSample+=1
        if abs(self.maxV-self.minV)>=self.tsv:
            v=self.maxV-self.minV
            self.currentRead+=v
            
        else:
            self.currentRead=0
        return self.currentRead