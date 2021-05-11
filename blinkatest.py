import board
import digitalio
import busio

#Try creating digital input
pin = digitalio.DigitalInOut(board.D4)
print("Digital IO ok")

#Try creating I2C device
i2c = busio.I2C(board.SCL, board.SDA)
print("I2C ok")

#Try creating SPI device
spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
print("SPI ok")

print("done")
