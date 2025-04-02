"""
# Function of code
This program lets the user control a state using a physical button on a breadboard. The states function as follows:
- State is 'ON' when button is pressed
- State is 'OFF' when button is released

# Button functionality

# Author
Eldorado
"""

import RPi.GPIO as GPIO
from time import sleep

BUTTON_PIN = 17
State = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)       # Set GPIO17 to input and use the internal pull-up resitor to

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            print("    > ON")
        else:
            print("OFF <   ")
        sleep(0,2)

except KeyboardInterrupt:
    print("-> Execution aborted")

finally:
    GPIO.cleanup()