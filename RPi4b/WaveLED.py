"""
# Function of code
This program is meant to control 3 LEDs in such a way that a wave is achieved from left to right.

# Design method
This program is based on Phantom/RPi4b/FadeLED.py, the first RPi PWM program written by me. Instead of 1 PWM signal, a total of 3 are used in this one. 
The challenge is to change the Duty Cycle of all 3 PWMs in one function instead of just 1. Progressively increasing/decreasing the value of the DutyCycle is
done using the 'update_dc()' function, run every 10ms within the main while loop.

# Wave functionality
The wave functionality works by manipulating the Duty Cycle of the LEDs that follow the 1st LED. By initializing each consecutive Duty Cycle value at -y, -2y etc., 
it takes time for the respective Duty Cycle to reach 0 when progressively increasing. When the Duty Cycle reaches 0, it can be assigned to the 'pwm.ChangeDutyCycle()' 
function. This essentially turns ON the next LED n iteration steps later, creating a phase shift in the Duty Cycle sawtooth-curves of the LEDs.

# Important notes !
- Lists are used to store and organize the values of 'dc' and the iterative value 'a' (dcList & aList)
- A 'range(len(<list>))' loop is used to read the respective values of 'dc' and 'a' and update them
- Since len(dcList) == len(aList), the same "loop variable" 'i' can be used

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

# initializing PWM Duty Cycle and increment values, including negative strat values for LED 2 & 3
dc1 = 0
dc2 = -25
dc3 = -50
a1 = 0
a2 = 0
a3 = 0

# Organizing dc and a values in lists
dcList = [dc1, dc2, dc3]
aList = [a1, a2, a3]

# Upgrading the function of update_dc to check and modify the dc and a lists
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

    # MAIN LOOP
    while True:
        update_dc()
        if dcList[0] >= 0:
            pwm1.ChangeDutyCycle(dcList[0])
        if dcList[1] >= 0:
            pwm2.ChangeDutyCycle(dcList[1])
        if dcList[2] >= 0:
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