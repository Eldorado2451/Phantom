"""
Sends a UART message every 1 sec
"""

from machine import UART, Pin
import time

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

while True:
    uart.write('Hello from Pico!\r\n')     # \r\n is used to do (Carriage return + Line Feed) CR + LF over serial
    time.sleep(1)