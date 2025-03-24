"""
# Function of the code
This code controls an LED and fades it in and out. LED is connected to GPIO18 -> PWM.

# Key takeways 
The script runs a pwm.start function, that runs as longs as the script does not quit. after quitting,
the PWM automatically stops, because the Pi releases the GPIOs. The script is kept runnig in the while loop (line 31)
which also includes an update on the Duty Cycle "dc". dc is updated in a different function that changes a, the increment,
and thus "dc". Even reversing the increment at 0 and 100! sleep() is used to define the frequency of increments.

# Version updates
v1.1: Added a start value of -200 to test the initial fade delay. Created a conditional statement to check if dc is within the range of 0 and 100.

* This code also teaches something about Exeption handling. See the try, except and finally blocks.
"""

import RPi.GPIO as GPIO             # Import module
from time import sleep              # Import sleep

GPIO.setmode(GPIO.BCM)              # Set GPIO numberbering to BCM (GPIOxx)
PWM_PIN = 18                        # Define PWM pin numbering 
GPIO.setup(PWM_PIN, GPIO.OUT)       # Setup GPIO18 as OUTPUT for PWM

pwm = GPIO.PWM(PWM_PIN, 1000)       # -> Start instance of PWM called pwm, assigning it to GPRIO18 and setting the
                                    # PWM frequency to 1kHz
pwm.start(0)                        # Start PWM with 0% Duty Cycle (= OFF)

dc = -200                           # Create a variable to store the value of the Duty Cycle; Start val is -200 to test initial fade delay
a = 0                               # Create a variable for the increment for fading

def update_dc():                    # -> Defines a function to update the Duty Cycle value "dc" using the iteratino variabbel "a"
    global dc                       # Tells the function that the global variables should be used
    global a
    if dc <= 0:                     # Set increment a when dc <= 0 (0v PWM) -> this line is also true when dc is below 0!
        a = 1
    if dc == 100:                   # Change increment a when dc == 100 (3v3 PWM)
        a = -1
    dc = dc + a                     # Update dc

try:                                        # -> "try:" is a Exception handling block that can be used to RUN code, it executes the test code
                                            # For more info, check: https://youtu.be/NIWwJbo-9_8?si=BVkyXliIl6UjMtwi
    while True:                             # Main while loop that executes the updating the dc and the Duty Cycle of the PWM on GPIO18
        update_dc()                         # Function call
        if dc >= 0 and dc <= 100:           # Check if dc is within the range of 0 and 100, only then do Duty Cycle update
            pwm.ChangeDutyCycle(dc)
        sleep(0.01)
except KeyboardInterrupt:                                   # -> "except" is the exception handling block that CATCHES EXCEPTIONS and executes something after the exception is caught
    print(" -> Execution interrupted by keyboard input.")   # Prints message to user in console
    pass                                                    # -> "pass" silently ignores the exception without taking action

finally:
	pwm.stop()                                              # Stop pwm instance
	GPIO.cleanup()                              	        # Cleans up GPIO18: releases control over GPIO18
