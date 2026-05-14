# Function of the code: Drives the stepper driver via GPIO18. The stepper motor moves CW, switches and moves CCW 200 steps. It does this smoothly using a cosine to define the time the STEP signal is low. 
# Stepper driver used: A4988

import RPi.GPIO as GPIO
from time import sleep
import math

GPIO.setmode(GPIO.BCM)      # Sets BCM pin numbering (GPIOxx), not header numbering
GPIO.setup(18, GPIO.OUT)    # Sets GPIO18 to output = STEP
GPIO.setup(17, GPIO.OUT)    # Sets GPIO17 to output = DIR

LOW_time = 0			# Init LOW_time

min_Vel = 500
max_Vel = 2000
motionProfile_Steps = 1200
sCurve_Steps = motionProfile_Steps/4

min_LOWtime = 1/max_Vel
max_LOWtime = 1/min_Vel

def calcLOW_time(x):
    if x == 0 or x == motionProfile_Steps:
        return max_LOWtime
    if 0 < x <= sCurve_Steps:
        return 1/((max_Vel-min_Vel)*3*(x/sCurve_Steps)**2 - (max_Vel-min_Vel)*2*(x/sCurve_Steps)**3+min_Vel)
    if sCurve_Steps < x <= (motionProfile_Steps-sCurve_Steps):
        return min_LOWtime
    if (motionProfile_Steps-sCurve_Steps) < x < motionProfile_Steps:
        return 1/(-(max_Vel-min_Vel)*3*((x-motionProfile_Steps+sCurve_Steps)/sCurve_Steps)**2 + (max_Vel-min_Vel)*2*((x-motionProfile_Steps+sCurve_Steps)/sCurve_Steps)**3+max_Vel)
    else:
        return None


for i in range(2):
    if i % 2 == 0:
        GPIO.output(17, GPIO.HIGH)  	                # Set DIR to HIGH
    else:
        GPIO.output(17, GPIO.LOW)  	                    # Set DIR to LOW
    for j in range(motionProfile_Steps):                # Sets up a for loop to pulse the driver
        GPIO.output(18, GPIO.HIGH)                      # Writes a HIGH signal (3v3) to GPIO18
        # print("HIGH")                 # Prints the status of pin state
        sleep(min_LOWtime)                    # Sleep 1 ms
        GPIO.output(18, GPIO.LOW)       # Writes a LOW signal (0v) to GPIO18 
        # print("LOW")                  # Prints the status of pin state
        # print(LOW_time)		# = dry run print
        sleep(calcLOW_time(j))                 # Sleep for LOW_time
GPIO.cleanup()                      	# Cleans up GPIO18: releases control over GPIO18
print("Done!")                      	# Print that it is done driving
