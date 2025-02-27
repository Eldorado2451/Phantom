import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)      #Sets BCM pin numbering (GPIOxx), not header numbering
GPIO.setup(18, GPIO.OUT)    #Sets GPIO18 to output

for i in range(5):
    GPIO.output(18, GPIO.HIGH)
    print("LED is on")
    sleep(1)
    GPIO.output(18, GPIO.LOW)
    print("LED is off")
    sleep(1)
