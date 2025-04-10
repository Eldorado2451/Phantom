import serial

ser = serial.Serial('/dev/serial0', baudrate=9600, timeout=1)

print ("Listening on UART0 at 9600 baud...")

try:
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8', errors='ignore').strip()
            if data:
                print(f"Received: {data}")
except KeyboardInterrupt:
    print("Exiting.")
finally:
    ser.close()