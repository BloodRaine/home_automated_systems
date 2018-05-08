print('scanning household systems')

#################################
#   Author: Robinson Merillat
#   Date  : May 2, 2018
#   Desc. : Script to check household systems via Amazon Alexa commands
#           

import time
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
currTime = 0
startTime = time.time()
maxTime = 3
arduinoPin = 21
GPIO.setup(arduinoPin, GPIO.OUT)

try:
    while currTime < maxTime:
        currTime = time.time()-startTime
        print("Running...", currTime)
        GPIO.output(arduinoPin, GPIO.HIGH)
    print("finished...")
    GPIO.output(arduinoPin, GPIO.LOW)
except:
    print("error")
