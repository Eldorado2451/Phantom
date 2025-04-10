"""
Blinks 5 times and stops.
"""

from machine import Pin
from time import sleep

led = Pin(19, Pin.OUT)

try:
    for i in range(10):
        led.toggle()
        sleep(0.5)
except:
    pass
finally:
    print("Done blinking!")