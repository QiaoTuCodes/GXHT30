import utime
from gxht30 import GXHT30, GXHT30Error

sensor = GXHT30()

# if sensor.is_present():
#     try:
#         temperature, humidity = sensor.measure()
#         print('GXHT30: Temperature:', temperature, 'ºC, RH:', humidity, '%')
#     except SHT30Error as e:
#         print('Error reading GXHT30 sensor:', e)
# else:
#     print('GXHT30 sensor is not connected')

while True:
    utime.sleep_ms(1000)
    temperature, humidity = sensor.measure()
    print('GXHT30: Temperature:', temperature, 'ºC, RH:', humidity, '%')