import serial
import time

# Open serial port
ser = serial.Serial('/dev/ttyAMA10', 9600, timeout=1)

time.sleep(2)  # Wait for the connection to establish

while True:
    # Send data
    print("sending data")
    ser.write(b'Hello from Raspberry Pi\n')
    time.sleep(1)  # Delay between sends
