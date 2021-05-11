# Sample IO test
# Creates a digital I/O, I2C, and SPI interface to make sure interfaces work
# Tai Kjendal, April 2021

import board
import digitalio
import busio

# Digital input
pin = digitalio.DigitalInOut(board.D4)
print("Digital IO ok")

# I2C device
i2c = busio.I2C(board.SCL, board.SDA)
print("I2C ok")

# SPI device
spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
print("SPI ok")

print("done")
