import time
import board
import adafruit_ltr390

class LTR390:
    def __init__(self):
        self.i2c = board.I2C()  # uses board.SCL and board.SDA
        self.ltr = adafruit_ltr390.LTR390(self.i2c, 0x53)

    def read_ltr_data(self):
        return self.ltr.uvi, self.ltr.light


