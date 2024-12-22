# Import necessary modules
import time  # For time-related functions like delays
import board  # For accessing board-related I2C pins
import adafruit_ltr390  # For interfacing with the LTR390 UV and light sensor

# Define a class to interface with the LTR390 sensor
class LTR390:
    def __init__(self):  # Constructor to initialize the sensor
        # Set up the I2C interface using the board's SCL and SDA pins
        self.i2c = board.I2C()
        # Initialize the LTR390 sensor on the I2C bus, assuming address 0x53
        self.ltr = adafruit_ltr390.LTR390(self.i2c, 0x53)

    # Method to read data from the LTR390 sensor
    def read_ltr_data(self):
        # Returns a tuple containing UV Index (UVI) and ambient light intensity (light level)
        return self.ltr.uvi, self.ltr.light

# Create an instance of the LTR390 class
sensor = LTR390()

# Call the `read_ltr_data` method to retrieve sensor data
# and print the UV Index and light level readings
print(sensor.read_ltr_data())



