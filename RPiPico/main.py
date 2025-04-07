"""
Not sure if this works yet...
"""

from machine import Pin
from time import sleep

led = Pin(19, Pin.OUT)

try:
    while True:
        led.toggle()
        sleep(0.5)

except KeyboardInterrupt:
    print(" -> execution aborted")

finally:
    machine.reset()