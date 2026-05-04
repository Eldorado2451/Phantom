import RPi.GPIO as GPIO
import time
import math

# Pin Setup
LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Initialize PWM at 100Hz (smooth enough for the eye)
pwm = GPIO.PWM(LED_PIN, 100)
pwm.start(0)

try:
    print("Breathing LED started... Press Ctrl+C to stop.")
    while True:
        # Use a sine wave to create a smooth pulse
        for i in range(0, 180):
            # Convert degrees to radians for math.sin
            # sin(0)=0, sin(90)=1 (max brightness), sin(180)=0
            duty_cycle = math.sin(math.radians(i)) * 100
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.02) # Speed of the breath

except KeyboardInterrupt:
    print("\nStopping...")
finally:
    pwm.stop()
    GPIO.cleanup()
    print("GPIO Cleaned up")
