"""
Function of the code: This porogram is meant to control 3 LEDs in such a way that a wave is achieved from left to right.

Way it is designed:

"""

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
PWM_PIN_1 = 19
PWM_PIN_2 = 13
PWM_PIN_3 = 12
GPIO.setup(PWM_PIN_1, GPIO.OUT)
GPIO.setup(PWM_PIN_2, GPIO.OUT)
GPIO.setup(PWM_PIN_3, GPIO.OUT)

pwm1 = GPIO.PWM(PWM_PIN_1, 1000)
pwm2 = GPIO.PWM(PWM_PIN_2, 1000)
pwm3 = GPIO.PWM(PWM_PIN_3, 1000)

try:
    pwm1.start(33)
    pwm2.start(66)
    pwm3.start(100)
    while True:
        print("running..")
        sleep(1)
except KeyboardInterrupt:
    print(" -> Execution aborted")
    pass
finally:
    pwm1.stop()
    pwm2.stop()
    pwm3.stop()