"""
Function of the code: This code controls an LED and fades it in and out. LED is connected to GPIO18 -> PWM.
"""

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)  
PWM_PIN = 18  
GPIO.setup(PWM_PIN, GPIO.OUT)  

pwm = GPIO.PWM(PWM_PIN, 1000)   # 1 kHz frequency  
pwm.start(0)                    # Start PWM with 50% duty cycle

dc = 0
a = 0

def update_dc():
    global dc
    global a
    if dc == 0:
        a = 10
    if dc == 100:
        a = -10
    dc = dc + a

try:
    while True:
        update_dc()
        pwm.ChangeDutyCycle(dc)
        sleep(0.2)
except KeyboardInterrupt:
    pass
pwm.stop()
GPIO.cleanup()

