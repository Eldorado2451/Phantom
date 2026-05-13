# Function of the code: Drives the stepper driver via GPIO18. The stepper motor moves CW, switches and moves CCW 200 steps.
# Stepper driver used: A4988

import RPi.GPIO as GPIO
from time import sleep
import math

GPIO.setmode(GPIO.BCM)      # Sets BCM pin numbering (GPIOxx), not header numbering
GPIO.setup(18, GPIO.OUT)    # Sets GPIO18 to output = STEP
GPIO.setup(17, GPIO.OUT)    # Sets GPIO18 to output = DIR

LOW_time = 0

for i in range(5):
    if i % 2 == 0:
        GPIO.output(17, GPIO.HIGH)  # Set DIR to HIGH
    else:
        GPIO.output(17, GPIO.LOW)  # Set DIR to LOW
    for j in range(200):                # Sets up a for loop
        LOW_time = 0.2495 * math.cos(((2*math.pi)/2)*j) + 0.2505
        GPIO.output(18, GPIO.HIGH)      # Writes a HIGH signal (3v3) to GPIO18
        # print("HIGH")                   # Prints the status of pin state
        sleep(0.001)                    # Sleep 1 ms
        GPIO.output(18, GPIO.LOW)       # Writes a LOW signal (0v) to GPIO18 
        # print("LOW")                    # Prints the status of pin state
        print(LOW_time)
        sleep(LOW_time)                    # Sleep 1 ms
GPIO.cleanup()                      # --> cleans up GPIO18: releases control over GPIO18
print("Done!")                      # Print that it is done
