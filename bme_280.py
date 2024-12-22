# Importing necessary libraries and modules
import board  # Provides access to the I2C interface and other board-related hardware functions
import time  # Provides time-related functions, such as delays
from adafruit_bme280 import basic as adafruit_bme280  # Imports the Adafruit library for the BME280 sensor in basic mode

# Define a class to manage interactions with the BME280 sensor
class BME280:
    def __init__(self):  # Constructor method called when an instance of the class is created
        # Initialize the I2C interface using the I2C pins on the board
        self.i2c = board.I2C()
        # Create an instance of the BME280 sensor object using the I2C interface
        # The address `0x76` is the default I2C address for the BME280 sensor
        self.bme280 = adafruit_bme280.Adafruit_BME280_I2C(self.i2c, 0x76)

    # Method to read data from the BME280 sensor
    def read_bme_data(self):
        # Returns a tuple containing temperature (in Celsius), 
        # relative humidity (in %), and pressure (in hPa)
        return self.bme280.temperature, self.bme280.relative_humidity, self.bme280.pressure

# Create an instance of the BME280 class
sensor = BME280()

# Call the `read_bme_data` method to retrieve sensor data
# and print the temperature, humidity, and pressure readings
print(sensor.read_bme_data())



