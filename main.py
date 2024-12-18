from bme280Sensor import BME280Sensor
from ltr390Sensor import LTR390Sensor
from PMSensor import PM25Sensor

bme = BME280Sensor()
MP = PM25Sensor()
ltr = LTR390Sensor()

print(bme.get_data())
print(ltr.read_uv_and_light())
print(MP.read_sensor_data())
