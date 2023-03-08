import RPi.GPIO as gpio
import time
dac = []
number = []
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
gpio.output(dac, number)
time.sleep(15)
gpio.output(dac, 0)