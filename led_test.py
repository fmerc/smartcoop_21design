# Blink 2 LEDs on GPIO 9, 11
# Used for measuring electrical chars of LEDs
# Tai Kjendal May 2021

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

try:
	print("blinking leds D9, D11")
	while True:
		GPIO.output(9,GPIO.HIGH)
		time.sleep(1)
#		input("continue...")

		GPIO.output(11,GPIO.HIGH)
		time.sleep(1)
#		input("continue...")

		GPIO.output(9,GPIO.LOW)
		time.sleep(1)
#		input("continue...")

		GPIO.output(11,GPIO.LOW)
		time.sleep(1)
#		input("continue...")

except KeyboardInterrupt:
	print("stopping")

finally:
	GPIO.output(9,GPIO.LOW)
	GPIO.output(11,GPIO.LOW)
