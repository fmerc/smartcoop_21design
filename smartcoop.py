# Smartcoop system
# Combines GPIO read/write with Blynk app
# Tai Kjendal May 2021

import board
import RPi.GPIO as GPIO
import adafruit_am2320

import  BlynkLib

# Initialize Blynk
BLYNK_AUTH = 'TH65MBuo20kcXEaqykS8d1UdMMzgeiBk'
blynk=BlynkLib.Blynk(BLYNK_AUTH)

# Setup sensor read
i2c = board.I2C()
am = adafruit_am2320.AM2320(i2c)

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

v4 = 0
v5 = 0

# Register handler for virtual pin V4 write event
@blynk.VIRTUAL_WRITE(4)
def write_handler1(value):
	global v4
	v4 = int(value[0])
	print('Virtual Pin V4: {}'.format(v4))

# Register handler for virtual pin V5 write event
@blynk.VIRTUAL_WRITE(5)
def write_handler2(value1):
	global v5
	v5 = int(value1[0])
	print('Virtual Pin V5: {}'.format(v5))

# Register virtual pins
@blynk.VIRTUAL_READ(2)
@blynk.VIRTUAL_READ(3)
def read_handler():
	dth = readSensor()
	blynk.virtual_write(2, "Temp: {:.1f} \xb0F".format(dth.t))
#	print("Temp: {:.1f} \xb0F".format(dth.t))
	blynk.virtual_write(3, "RH: {} %".format(dth.rh))

	temp_low = v4 - 5
	temp_high = v4 + 5
#	print("Setting Temp Range: {0} to {1} \xb0F".format(temp_low, temp_high))

	# Heatmat for temperature
	if dth.t < temp_low:
		GPIO.output(9,GPIO.HIGH)
	elif dth.t > temp_high:
		GPIO.output(9,GPIO.LOW)
	# Ventilation for humidity
	if v5 == 1:
		GPIO.output(11,GPIO.HIGH)
	else:
		GPIO.output(11,GPIO.LOW)


# Get sensor data
class SensorRead:
	def __init__(self):
		self.t = am.temperature * (9/5) + 32
		self.rh = am.relative_humidity

def readSensor():
	return SensorRead()



# Main loop
try:
	print("starting blynk service")
	while True:
		blynk.run()

except KeyboardInterrupt:
	print("\nstopping")

finally:
	GPIO.output(9,GPIO.LOW)
	GPIO.output(11,GPIO.LOW)
