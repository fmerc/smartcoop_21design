# Test if temperature & humidity sensor is working
# Sensor: AM2320 DTH
# Documentation: https://www.adafruit.com/product/3721
# Tai Kjendal April 2021

import time
import board
import adafruit_am2320

i2c = board.I2C()
am = adafruit_am2320.AM2320(i2c)

while True:
	print("Temperature: ", am.temperature)
	print("Humidity: ", am.relative_humidity)
	time.sleep(2)
