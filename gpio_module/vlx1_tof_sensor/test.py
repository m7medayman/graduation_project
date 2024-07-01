import os
import time 
import VL53L1X
import RPi.GPIO as GPIO


if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')



# VCC = 18
XSHUT = 16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(XSHUT,GPIO.OUT)
# GPIO.setup(VCC,GPIO.OUT)
# GPIO.output(VCC,GPIO.HIGH)
GPIO.output(XSHUT,GPIO.HIGH)
try:
    tof1=VL53L1X.VL53L1X(i2c_bus=0, i2c_address=0x2A)
    tof1.open()

except:
    tof1 = VL53L1X.VL53L1X(i2c_bus=0, i2c_address=0x29)
    tof1.open()
    tof1.change_address(new_address = 0x2A)
    # GPIO.output(XSHUT, GPIO.LOW)
    GPIO.setup(XSHUT,GPIO.IN)
    tof1.open()
tof2 = VL53L1X.VL53L1X(i2c_bus=0, i2c_address=0x29)
tof2.open()

tof1.start_ranging(2)                   # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range
tof2.start_ranging(2)                   # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range
try:
    while True:
        # Grab the range in mm, this function will block until
        # a reading is returned.
        distance_in_mm = tof1.get_distance()
        print("Distance1:", distance_in_mm, "mm")
        # distance_in_mm = tof2.get_distance()
        # print("Distance2:", distance_in_mm, "mm")
        # time.sleep(0.1)  # Wait for a short time before the next reading

except KeyboardInterrupt:
    # This block allows you to gracefully exit the loop by pressing Ctrl+C
    # It stops the ranging process and closes the sensor before exiting.
    tof2.stop_ranging()
    tof1.stop_ranging()    