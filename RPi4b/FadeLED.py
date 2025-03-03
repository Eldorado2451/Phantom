"""
Function of the code: This code controls an LED and fades it in and out. LED is connected to GPIO18 -> PWM.

Key takeways: The script runs a pwm.start function, that runs as longs as the script does not quit. after quitting,
the PWM automatically stops, because the Pi releases the GPIOs. The script is kept runnig in the while loop (line 31)
which also includes an update on the Duty Cycle "dc". dc is updated in a different function that changes a, the increment,
and thus "dc". Even reversing the increment at 0 and 100! sleep() is used to define the frequency of increments.
"""

import RPi.GPIO as GPIO         # Import module
from time import sleep          # Import sleep

GPIO.setmode(GPIO.BCM)          # Set GPIO numberbering to BCM (GPIOxx)
PWM_PIN = 18                    # Define PWM pin numbering 
GPIO.setup(PWM_PIN, GPIO.OUT)   # Setup GPIO18 as OUTPUT for PWM

pwm = GPIO.PWM(PWM_PIN, 1000)   # -> Start instance of PWM called pwm, assigning it to GPRIO18 and setting the
                                # PWM frequency to 1kHz
pwm.start(0)                    # Start PWM with 0% Duty Cycle (= OFF)

dc = 0                          # Create a variable to store the value of teh Duty Cycle
a = 0                           # Create a variable for the increment for fading

def update_dc():
    global dc
    global a
    if dc == 0:
        a = 10
    if dc == 100:
        a = -10
    dc = dc + a

try:
    while True:
        update_dc()
        pwm.ChangeDutyCycle(dc)
        sleep(0.2)
except KeyboardInterrupt:
    pass
pwm.stop()
GPIO.cleanup()

