import pandas as pd
class Person():
    def __init__(self,name:str)->None:
        self.excelVersion=0
        self.name=name
        self._testData={}
        self._testCount=0
    def exportAllPersonData(self):
            data = self._testData
            df = pd.DataFrame(data)
                # Saving to an Excel file
            df.to_excel(f'{self.name}_{self.excelVersion}.xlsx', index=False)
            self.excelVersion+=1
    
    def addTest(self,xData:list,yData:list):
         self._testData[f"Column{self._testCount}"]=xData
         self._testData[f"Column{self._testCount+1}"]=yData
         self._testCount+=2

         
         