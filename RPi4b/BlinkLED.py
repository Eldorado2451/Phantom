# Function of the code: Drives GPIO18 of a RPi 4b from state ON/OFF. Does this 10x

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)      # Sets BCM pin numbering (GPIOxx), not header numbering
GPIO.setup(18, GPIO.OUT)    # Sets GPIO18 to output

for i in range(5):                 # Sets up a for loop
    GPIO.output(18, GPIO.HIGH)      # Writes a HIGH signal (3v3) to GPIO18 
    print("LED is on")              # Prints the status of the LED (for control)
    sleep(1)                        # Sleep 1 sec
    GPIO.output(18, GPIO.LOW)       # Writes a LOW signal (0v) to GPIO18 
    print("LED is off")             # Prints the status of the LED (for control)
    sleep(1)                        # Sleep 1 sec
GPIO.cleanup()                      # --> cleans up GPIO18: releases control over GPIO18
