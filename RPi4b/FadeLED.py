"""
Function of the code: This code controls an LED and fades it in and out. LED is connected to GPIO18 -> PWM.
"""

import RPi.GPIO as GPIO  

GPIO.setmode(GPIO.BCM)  
PWM_PIN = 18  
GPIO.setup(PWM_PIN, GPIO.OUT)  

pwm = GPIO.PWM(PWM_PIN, 1000)  # 1 kHz frequency  
pwm.start(50)  # Start PWM with 50% duty cycle  

input("Press Enter to exit...")  # Keeps the script running  

pwm.stop()  
GPIO.cleanup()