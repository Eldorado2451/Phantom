"""
# Function of code
This program lets the user control a state using a physical button on a breadboard. The states function as follows:
- State is 'ON' when button is pressed
- State is 'OFF' when button is released

# Author
Eldorado
"""

# Import modules
import RPi.GPIO as GPIO
from time import sleep

# Configure GPIO
GPIO.setmode(GPIO.BCM)
BUTTON_PIN = 17
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)           # Set GPIO17 to input and use the internal pull-up resitor to keep the signal HIGH.
                                                                    # When the button is pressed (=Active) the signal is pulled to GND ()=LOW) making
                                                                    # the logic Acative Low.

# Use try/except blocks to run code and exit if ctrl+c is pressed
try:
    # MAIN LOOP
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:                      # GPIO.input reads signal voltage level, when pulled to GND, input == GPIO.LOW
            print("    > ON")
        else:
            print("OFF <   ")
        sleep(0.2)

except KeyboardInterrupt:
    # Print message when exit
    print(" -> Execution aborted")

finally:
    # Release GPIO pins
    GPIO.cleanup()