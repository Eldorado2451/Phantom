import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)      #Sets BCM pin numbering (GPIOxx), not header numbering
GPIO.setup(18, GPIO.OUT)    #Sets GPIO18 to output

for i in range(5):
    GPIO.output(18, GPIO.HIGH)
    sleep(1)
    GPIO.output(18, GPIO.LOW)
    sleep(1)
