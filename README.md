MicroPython Driver for [GXHT30]

The driver has been tested on 01Studio Columbus board. but It should work on whatever other micropython board, if anyone find problems in other boards, please open an issue and We'll see.

##Motivation
for any 01Studio Board has an DS18B20 & DHT11 driver but not a MicroPython Driver of GXHT30.

##References:
The GXHT30 MicroPython Driver has transplant from SHT3x. So you We'll see datasheet of here.
* [Sensor Datasheet](https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/2_Humidity_Sensors/Sensirion_Humidity_Sensors_SHT3x_Datasheet_digital.pdf)
* [GXHT30 Datasheet](https://github.com/QiaoTuCodes/GXHT30/blob/main/CXCAS-GXHT30.PDF) from sensor manufacturer

##Examples of use:

###How to get the temperature and relative humidity:

The `measure()` method returns a tuple with the temperature in celsius grades and the relative humidity in percentage. 
If the measurement cannot be performed then an exception is raised (`GXHT30Error`)

```python
from gxht30 import GXHT30

sensor = GXHT30()

temperature, humidity = sensor.measure()

print('Temperature:', temperature, 'ºC, RH:', humidity, '%')
```

There is another method, `measure_int()`, that returns 4 integer values, **no floating point operation is done**, designed 
for environments that doesn't support floating point operations, the four values are: 

Temperature (integer part), Temperature (decimal part), RH (integer part), RH (decimal part)

For intance, if the `measure()` method returns `(21.5623, 32.0712)` the `measure_int()` method would return: `(24, 56, 32, 7)` The decimal 
part is limited to 2 decimal digits.

```python
t_int, t_dec, h_int, h_dec = sensor.measure_int()

print('Temperature: %i.%02i °C, RH: %i.%02i %%' % (t_int, t_dec, h_int, h_dec))
```

Both methods allow a `raw` param that when It's `True` returns the sensor measurement as-is, It's a `bytearray(6)` with the format defined in the sensor datasheet document.

```python
raw_measure = sensor.measure(raw=True)

print('Sensor measurement', raw_measure)
```

###Check if shield is connected

```python
from gxht30 import GXHT30

sensor = GXHT30()

print('Is connected:', sensor.is_present())

```

###Read sensor status

Check the [Sensor Datasheet](https://github.com/QiaoTuCodes/GXHT30/blob/main/CXCAS-GXHT30.PDF) for further info about sensor status register
```python
from gxht30 import GXHT30

sensor = GXHT30()

print('Status register:', bin(sensor.status()))
print('Single bit check, HEATER_MASK:', bool(sensor.status() & GXHT30.HEATER_MASK))

#The status register can be cleared with
sensor.clear_status()

```


###Reset the sensor

The driver allows a soft reset of the sensor

```python
from gxht30 import GXHT30

sensor = GXHT30()
sensor.reset()

```



###Error management

When the driver cannot access to the measurement an exception `GXHT30Error` is raised

```python
from gxht30 import GXHT30

sensor = GXHT30()

try:
    t, h = sensor.measure()
except GXHT30Error as ex:
    print('Error:', ex)


```
