"""

# Function of code
This program is meant to control 3 LEDs in such a way that a wave is achieved from left to right.

# Design method
This program is based on Phantom/RPi4b/FadeLED.py, the first RPi PWM program written by me. Instead of 1 PWM signals, a total of are used in this one.

TODO: tell something about the wave functionality and how it differs from controlling 1 PWM

#Author
Eldorado

"""
# Import modules
import RPi.GPIO as GPIO
from time import sleep

# Configure GPIO
GPIO.setmode(GPIO.BCM)
PWM_PIN_1 = 19
PWM_PIN_2 = 13
PWM_PIN_3 = 12
GPIO.setup(PWM_PIN_1, GPIO.OUT)
GPIO.setup(PWM_PIN_2, GPIO.OUT)
GPIO.setup(PWM_PIN_3, GPIO.OUT)

# Start pwm instances
pwm1 = GPIO.PWM(PWM_PIN_1, 1000)
pwm2 = GPIO.PWM(PWM_PIN_2, 1000)
pwm3 = GPIO.PWM(PWM_PIN_3, 1000)

dc1 = 0
dc2 = -66
dc3 = -172
a1 = 0
a2 = 0
a3 = 0

dcList = [dc1, dc2, dc3]
aList = [a1, a2, a3]

def update_dc():
    global dcList
    global aList
    for i in range(len(dcList)):
        if dcList[i] <= 0:
            aList[i] = 1
        if dcList[i] == 100:
            aList[i] = -1
        dcList[i] = dcList[i] + aList[i]

# Use try/except blocks to run code and exit if ctrl+c is pressed
try:
    # Start PWMs on GPIO pins
    pwm1.start(0)
    pwm2.start(0)
    pwm3.start(0)
    while True:
        update_dc()
        if dcList[0] <= 0:
            pwm1.ChangeDutyCycle(dcList[0])
        if dcList[1] <= 0:
            pwm2.ChangeDutyCycle(dcList[1])
        if dcList[2] <= 0:
            pwm3.ChangeDutyCycle(dcList[2])
        sleep(0.01)

except KeyboardInterrupt:
    # Print message when exit
    print(" -> Execution aborted")
    pass

finally:
    # Stop PWMs and release GPIO pins
    pwm1.stop()
    pwm2.stop()
    pwm3.stop()
    GPIO.cleanup()