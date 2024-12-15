import board
import time
from adafruit_bme280 import basic as adafruit_bme280

class BME280:
    def __init__(self):
        self.i2c = board.I2C()
        self.bme280 = adafruit_bme280.Adafruit_BME280_I2C(self.i2c, 0x76)

    def read_bme_data(self):
        return self.bme280.temperature, self.bme280.relative_humidity, self.bme280.pressure


