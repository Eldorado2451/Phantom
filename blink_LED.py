from time import sleep

def led_on():
    print("LED is ON")  # Simulating LED being ON

def led_off():
    print("LED is OFF")  # Simulating LED being OFF

while True:
    led_on()
    sleep(1)
    led_off()
    sleep(1)