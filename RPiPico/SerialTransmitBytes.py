"""
Sends a byte per second.

-> Works, but needs a terminal to interpret the byte!
"""

from machine import UART, Pin
import time

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

try:
    while True:
        uart.write(bytes([0xAC]))     # \r\n is used to do (Carriage return + Line Feed) CR + LF over serial
        time.sleep(1)

except KeyboardInterrupt:
    print("-> Pico execution aborted")