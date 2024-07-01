import RPi.GPIO as GPIO
import VL53L1X

class VlxGpioInput():
    def __init__(self) -> None:
        self.XSHUT1 = 16  # GPIO pin for XSHUT of sensor 1
        self.XSHUT2 = 18  # GPIO pin for XSHUT of sensor 2
        
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.XSHUT1, GPIO.OUT)
        GPIO.setup(self.XSHUT2, GPIO.OUT)

        # Initialize sensor 1
        GPIO.output(self.XSHUT1, GPIO.HIGH)
        GPIO.output(self.XSHUT2, GPIO.LOW)  # Keep sensor 2 in reset
        try:
            self.tof1 = VL53L1X.VL53L1X(i2c_bus=0, i2c_address=0x29)
            self.tof1.open()
        except:
            self.tof1 = VL53L1X.VL53L1X(i2c_bus=0, i2c_address=0x2A)
            self.tof1.open()
            self.tof1.change_address(0x29)
        self.tof1.close()

        # Initialize sensor 2
        GPIO.output(self.XSHUT2, GPIO.HIGH)  # Enable sensor 2
        GPIO.output(self.XSHUT1,GPIO.LOW)
        try:
            self.tof2 = VL53L1X.VL53L1X(i2c_bus=0, i2c_address=0x2A)
            self.tof2.open()
        except:
            self.tof2 = VL53L1X.VL53L1X(i2c_bus=0, i2c_address=0x29)
            self.tof2.open()
            self.tof2.change_address(0x2A)
            self.tof2 = VL53L1X.VL53L1X(i2c_bus=0, i2c_address=0x2A)
            self.tof2.open()
        
        # Reopen sensor 1 with new address
        GPIO.output(self.XSHUT2, GPIO.HIGH)  # Enable sensor 2
        GPIO.output(self.XSHUT1,GPIO.HIGH)
        self.tof1 = VL53L1X.VL53L1X(i2c_bus=0, i2c_address=0x29)
        self.tof1.open()

        self.tof1.start_ranging(2)
        self.tof2.start_ranging(2)
        self.tof1.set_timing_budget(1000) 
        self.tof2.set_timing_budget(1000)  
        self.tof1.set_inter_measurement_period(15)
        self.tof2.set_inter_measurement_period(15)

    def getFirstSensorGpio(self) -> float:
        distance = self.tof1.get_distance()
        if distance > 0:
            return float(distance)
        else:
            return -1

    def getSecondSensorFromGpio(self) -> float:
        distance = self.tof2.get_distance()
        if distance > 0:
            return float(distance)
        else:
            return -1
