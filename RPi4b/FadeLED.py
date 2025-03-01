"""
Function of the code: This code controls an LED and fades it in and out. LED is connected to GPIO18 -> PWM.
"""

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

pwm = GPIO.PWM(18, 1000)
pwm.start(0)

dc = 0

while True:
    if dc == 0:
        a = 10
    if dc == 100:
        a = -10
    pwm.ChangeDutyCycle(dc + a)
    
    