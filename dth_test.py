import time
import board
import adafruit_am2320

i2c = board.I2C()
am = adafruit_am2320.AM2320(i2c)

while True:
	print("Temperature: ", am.temperature)
	print("Humidity: ", am.relative_humidity)
	time.sleep(2)
