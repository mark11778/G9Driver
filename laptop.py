import serial

# Open serial port
ser = serial.Serial('COM3', 9600, timeout=1)

while True:
    # Read data from the serial port
    data = ser.readline().decode('utf-8').strip()
    if data:
        print(f"Received: {data}")

