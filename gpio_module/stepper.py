import RPi.GPIO as GPIO
from time import sleep
import os

if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')
class TB6600:
    
    def __init__(self,clkPin,dirPin):
        self.CLK_pin = clkPin
        self.DIR_pin = dirPin


        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.DIR_pin, GPIO.OUT,initial=False)
        GPIO.setup(self.CLK_pin, GPIO.OUT,initial=False)
        # delete if test() not used
  

    # Moving the motor    
    def move(self, direction, steps, sleep_delay,speedDelay):
        # pause due to a possible change direction
        str_change_direction = ' - due to a change direction.'
        print('Paused for ' + str(sleep_delay) + str_change_direction)
        sleep(sleep_delay)
        GPIO.output(self.DIR_pin, direction)
        for x in range(steps):
            print('clk')
            GPIO.output(self.CLK_pin,GPIO.HIGH)
            sleep(speedDelay) # Dictates how fast stepper motor will run
			# Set coil winding to low
            GPIO.output(self.CLK_pin,GPIO.LOW)
            sleep(speedDelay) # Dictates how fast stepper motor will run


    def forward(self, steps, speedDelay ,sleep_delay=.5):
        self.move(0, steps, sleep_delay=sleep_delay,speedDelay=speedDelay)

    def reverse(self, steps, speedDelay,sleep_delay=.5):
        self.move(1, steps, sleep_delay,speedDelay=speedDelay)



stepper=TB6600(clkPin=38,dirPin=40)
stepper.forward(steps=1000000,speedDelay=0.0007,sleep_delay=0.5)
print("stop")