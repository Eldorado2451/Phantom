# Function of the code: Drives the stepper driver via GPIO18. The stepper motor moves CW, switches and moves CCW 200 steps. It does this smoothly using a cosine to define the time the STEP signal is low. 
# Stepper driver used: A4988

import RPi.GPIO as GPIO
from time import sleep
import math

GPIO.setmode(GPIO.BCM)      # Sets BCM pin numbering (GPIOxx), not header numbering
GPIO.setup(18, GPIO.OUT)    # Sets GPIO18 to output = STEP
GPIO.setup(17, GPIO.OUT)    # Sets GPIO17 to output = DIR

LOW_time = 0			# Init LOW_time

min_LOWtime = 0.001
max_LOWtime = 0.01
steps = 600
A = (max_LOWtime - min_LOWtime) / 2
offset = (max_LOWtime + min_LOWtime) / 2

for i in range(5):
    if i % 2 == 0:
        GPIO.output(17, GPIO.HIGH)  	# Set DIR to HIGH
    else:
        GPIO.output(17, GPIO.LOW)  	# Set DIR to LOW
    for j in range(steps):                # Sets up a for loop to pulse the driver
        LOW_time = A * math.cos(((2 * math.pi) / steps) * j) + offset # LOW_time is modified by j, ranging from .001 to .01 sec
        GPIO.output(18, GPIO.HIGH)      # Writes a HIGH signal (3v3) to GPIO18
        # print("HIGH")                 # Prints the status of pin state
        sleep(0.001)                    # Sleep 1 ms
        GPIO.output(18, GPIO.LOW)       # Writes a LOW signal (0v) to GPIO18 
        # print("LOW")                  # Prints the status of pin state
        # print(LOW_time)		# = dry run print
        sleep(LOW_time)                 # Sleep for LOW_time
GPIO.cleanup()                      	# Cleans up GPIO18: releases control over GPIO18
print("Done!")                      	# Print that it is done driving
