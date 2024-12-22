# Import necessary modules
import serial  # For serial communication with devices like sensors
import time  # Provides functions for time-related operations, such as delays

# Define a class to interface with the PM2.5 sensor
class PM25Sensor:
    def __init__(self, port='/dev/serial0', baudrate=9600, timeout=1):  # Constructor to initialize the sensor
        # Set up a serial connection with the given parameters:
        # `port`: The serial port to use (default is '/dev/serial0' on Raspberry Pi)
        # `baudrate`: Communication speed in bits per second (9600 is a typical value for this sensor)
        # `timeout`: Maximum time to wait for data in seconds (1 second here)
        self.ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)

    # Method to read data from the PM2.5 sensor
    def read_sensor_data(self):
        # Construct a request frame as per the sensor's protocol to request data
        # This frame tells the sensor to send measurement data
        request_frame = b'\x42\x4d\x00\x00\x00\x00\x00\x00\x00\x00'
        
        # Write the request frame to the sensor via the serial connection
        self.ser.write(request_frame)
        
        # Wait for 1 second to allow the sensor to process and respond
        time.sleep(1)
        
        # Read up to 32 bytes of data from the sensor
        data = self.ser.read(32)

        # Check if the data received is valid:
        # - It should be exactly 32 bytes long
        # - The first two bytes should match the sensor's predefined header (0x42 and 0x4D)
        if len(data) == 32 and data[0] == 0x42 and data[1] == 0x4d:
            # Extract PM2.5 and PM10 values from the data frame:
            # The PM2.5 value is a 16-bit number (2 bytes) at positions 10 and 11
            # Multiply the high byte by 256 and add the low byte to reconstruct the value
            pm2_5 = data[10] * 256 + data[11]  # PM2.5 concentration in µg/m³
            
            # Similarly, extract the PM10 value, which is a 16-bit number at positions 12 and 13
            pm10 = data[12] * 256 + data[13]  # PM10 concentration in µg/m³
            
            # Return a formatted string with the PM2.5 and PM10 values
            return f"PM2.5: {pm2_5} µg/m³, PM10: {pm10} µg/m³"
        else:
            # If the data is invalid or the header doesn't match, print an error message
            print("error")
