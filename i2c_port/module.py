import serial
# this module will get the data from the sensor and returen the value of the sensor  
class SerialPort:
	def __init__(self) -> None:
		self.ser = serial.Serial('/dev/ttyACM0', 9600)
		self.lastValue=500
	def getSensorValue(self):
		sensor_value = self.ser.readline().strip()
		try:
			sensor_value=sensor_value.decode("utf-8")
			sensor_value=int(sensor_value)
		except:
			print("invalid")
			sensor_value=self.lastValue
		
		if(sensor_value>1023 or sensor_value<0):
			print("invalid")
			sensor_value=self.lastValue
		# print (sensor_value)
		outputValue=sensor_value
		self.lastValue=sensor_value
		return outputValue
