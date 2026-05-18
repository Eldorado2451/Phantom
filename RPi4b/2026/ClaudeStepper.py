import RPi.GPIO as GPIO
import time

# Pin setup
STEP_PIN = 18
DIR_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.output(DIR_PIN, GPIO.HIGH)

# Parameters
TOTAL_TIME = 5.0
ACCEL_TIME = 1.5
DECEL_TIME = 1.5
CRUISE_TIME = TOTAL_TIME - ACCEL_TIME - DECEL_TIME
MAX_SPEED = 800  # steps/sec

def calculate_total_steps():
    """Calculate total steps for the motion profile"""
    accel_steps = 0.5 * MAX_SPEED * ACCEL_TIME
    cruise_steps = MAX_SPEED * CRUISE_TIME
    decel_steps = 0.5 * MAX_SPEED * DECEL_TIME
    return int(accel_steps + cruise_steps + decel_steps)

total_steps = calculate_total_steps()
accel_steps = int(0.5 * MAX_SPEED * ACCEL_TIME)
cruise_steps = int(MAX_SPEED * CRUISE_TIME)

try:
    start_time = time.time()
    
    for step in range(total_steps):
        # Determine phase and speed
        if step < accel_steps:
            # Acceleration
            progress = step / accel_steps
            speed = MAX_SPEED * progress
        elif step < accel_steps + cruise_steps:
            # Cruise
            speed = MAX_SPEED
        else:
            # Deceleration
            steps_in_decel = step - accel_steps - cruise_steps
            decel_total = total_steps - accel_steps - cruise_steps
            progress = 1 - (steps_in_decel / decel_total)
            speed = MAX_SPEED * progress
        
        # Pulse the step pin
        if speed > 10:  # Avoid division by zero
            delay = 1.0 / (2 * speed)
            GPIO.output(STEP_PIN, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(STEP_PIN, GPIO.LOW)
            time.sleep(delay)
    
    print(f"Completed in {time.time() - start_time:.2f} seconds")
    
finally:
    GPIO.cleanup()