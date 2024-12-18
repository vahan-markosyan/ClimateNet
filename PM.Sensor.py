import serial
import time

class PM25Sensor:
    def __init__(self, port='/dev/serial0', baudrate=9600, timeout=1):
        self.ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)

    def read_sensor_data(self):
        request_frame = b'\x42\x4d\x00\x00\x00\x00\x00\x00\x00\x00'
        self.ser.write(request_frame)
        time.sleep(1)

        data = self.ser.read(32)

        if len(data) == 32 and data[0] == 0x42 and data[1] == 0x4d:
            pm2_5 = data[10] * 256 + data[11]  # PM2.5
            pm10 = data[12] * 256 + data[13]  # PM10
            return(f"PM2.5: {pm2_5} µg/m³, PM10: {pm10} µg/m³")
        else:
            print("error")
