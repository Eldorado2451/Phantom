import RPi.GPIO as GPIO
import time

# Pin Setup
LED_PIN = 18 
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def flash(duration):
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.2) # Gap between blinks

try:
    print("Starting SOS pattern for ~10 seconds...")
    start_time = time.time()
    
    # Run loop until 10 seconds have passed
    while time.time() - start_time < 10:
        # S: Three dots
        for _ in range(3): flash(0.2)
        time.sleep(0.4) # Gap between letters
        
        # O: Three dashes
        for _ in range(3): flash(0.6)
        time.sleep(0.4) # Gap between letters
        
        # S: Three dots
        for _ in range(3): flash(0.2)
        time.sleep(1.0) # Gap before repeating the word

except KeyboardInterrupt:
    print("\nStopped by user")
finally:
    GPIO.cleanup()
    print("GPIO Cleaned up")
