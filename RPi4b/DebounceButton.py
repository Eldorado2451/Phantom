"""
# Function of code
This program lets the user control a state using a physical button on a breadboard. The states function as follows:
- State is 'ON' when button is pressed
- State is 'OFF' when button is released

Additionaly this program shows how to debounce a button inside a loop. It is not the best way to tackle debouncing,
due to the fact that the debouncing is handled in the loop, and no other process is done. This code is just for educational purposes.

Was to handle the button in a better way is to use event tiggers or callbacks.

# Author
Eldorado
"""

import RPi.GPIO as GPIO
import time

BUTTON_PIN = 17         # GPIO17
DEBOUNCE_TIME = 0.2     # 200ms

GPIO.setmode(BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

last_press_time = 0

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            current_time = time.time()
            if current_time - last_press_time > DEBOUNCE_TIME:
                print("    > ON")
                last_press_time = current_time
        else:
            print("OFF <   ")
        time.sleep(0.01)

except KeyboardInterrupt:
    print(" -> Execution aborted")

finally:
    GPIO.cleanup()