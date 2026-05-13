# Function of the code: Drives GPIO18 of a RPi 4b from state ON/OFF. Pulses 50x
# Stepper driver used: A4988

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)      # Sets BCM pin numbering (GPIOxx), not header numbering
GPIO.setup(18, GPIO.OUT)    # Sets GPIO18 to output = STEP
GPIO.setup(17, GPIO.OUT)    # Sets GPIO18 to output = DIR

GPIO.output(17, GPIO.HIGH)  # Set DIR to HIGH

for i in range(50):                 # Sets up a for loop
    GPIO.output(18, GPIO.HIGH)      # Writes a HIGH signal (3v3) to GPIO18
    print("HIGH")                   # Prints the status of pin state
    sleep(0.1)                      # Sleep 100 ms
    GPIO.output(18, GPIO.LOW)       # Writes a LOW signal (0v) to GPIO18 
    print("LOW")                    # Prints the status of pin state
    sleep(0.1)                      # Sleep 100 ms
GPIO.cleanup()                      # --> cleans up GPIO18: releases control over GPIO18
print("Done!")                      # Print that it is done
