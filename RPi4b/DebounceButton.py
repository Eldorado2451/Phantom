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
# Import modules
import RPi.GPIO as GPIO
import time

# Setup constants
BUTTON_PIN = 17         # GPIO17
DEBOUNCE_TIME = 0.2     # 200ms

# Configure GPIO, setup internal pull-up resitor
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# init last time button was pressed
last_press_time = 0     

# Using try, except, finally block
try:
    while True:                                                 # MAIN LOOP
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:                  # When GPIO voltage is pushed LOW (=GND) by button (i.e. is pressed)
            current_time = time.time()                          # Mark time when voltage is pushed LOW, this can happen multiple time when switch is bouncing!
            if current_time - last_press_time > DEBOUNCE_TIME:  # If time since last pushed Low > 200ms.. (i.e. when last bounce has happend, and signal is stable LOW)
                print("    > ON")                               # Execute action
                last_press_time = current_time                  # Update last pressed time, esentialy saying: mark last time GPIO signal was stable LOW
        else:
            print("OFF <   ")
        time.sleep(0.01)

# Print message when exit
except KeyboardInterrupt:
    print(" -> Execution aborted")

# Release GPIO pins
finally:
    GPIO.cleanup()