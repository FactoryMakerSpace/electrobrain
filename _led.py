#!/usr/bin/env python2.7
# script by Alex Eames http://RasPi.tv
#http://RasPi.tv/2013/how-to-use-soft-pwm-in-rpi-gpio-pt-2-led-dimming-and-motor-speed-control
# Modified by Jim O'Connell 
# http://github.com/jimoconnell/electrobrain

# Using PWM with RPi.GPIO pt 2 - requires RPi.GPIO 0.5.2a or higher

import RPi.GPIO as GPIO # always needed with RPi.GPIO
from time import sleep  # pull in the sleep function from time module
import os # this lets us grab the machine load
from random import randint
# import numpy #not needed yet, but probably later
GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM

GPIO.setup(25, GPIO.OUT)# set GPIO 25 as output for white led
GPIO.setup(24, GPIO.OUT)# set GPIO 26 as output for red led

white = GPIO.PWM(25, 100)    # create object white for PWM on port 25 at 100 Hertz
red = GPIO.PWM(24, 66)      # create object red for PWM on port 24 at 66 Hertz

white.start(0)              # start white led on 0 percent duty cycle (off) #test comment
red.start(100)              # red fully on (100%)

# now the fun starts, we'll vary the duty cycle to 
# dim/brighten the leds, so one is bright while the other is dim

#pause_time = 0.06           # you can change this to slow down/speed up
try:
    while True:
        loads = os.getloadavg()
        #print(loads[1])
        pause_time = (1. / loads[1]) / 100
        #print(pause_time)

######### WHITE SECTION 
        for i in range(15,101,5):      # 101 because it stops when it finishes 100
            white.ChangeDutyCycle(i)
            sleep(pause_time)
        for i in range(100,15,-1):      # from 100 to zero in steps of -1
            white.ChangeDutyCycle(i)
            sleep(pause_time)

######### RED SECTION 
        for i in range(15,101,5):      # 101 because it stops when it finishes 100
            red.ChangeDutyCycle(100 - (i - randint(1, 5)))
            sleep(pause_time)
        for i in range(100,15,-1):      # from 100 to zero in steps of -1
            red.ChangeDutyCycle(100 - (i - randint(1, 5)))
            sleep(pause_time)

except KeyboardInterrupt:
    white.stop()            # stop the white PWM output
    red.stop()              # stop the red PWM output
    #GPIO.cleanup()          # clean up GPIO on CTRL+C exit
