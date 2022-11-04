#FIREFLY
import board
import time
import busio
import neopixel
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility

i2c = busio.I2C(board.SCL1, board.SDA1)
apds = APDS9960(i2c)
apds.enable_color = True
apds.color_integration_time = 37
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)


while True:
    r, g, b, c = apds.color_data

    # wait for color data to be ready
    while not apds.color_data_ready:
        time.sleep(0.005)

    # get the data and print the different channels
    r, g, b, c = apds.color_data
    pixels.fill((r, g, b))在这里写上你的代码 :-)
