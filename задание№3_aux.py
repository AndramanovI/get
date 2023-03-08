import RPi.GPIO as gpio
import time
leds = []
aux = []
gpio.setmode(gpio.BCM)
gpio.setup(leds, gpio.OUT)
gpio.setup(leds, gpio.IN)
while True:
    counter = 0
    while counter <= len(leds) - 1:
        gpio.output(leds[counter], gpio.input(aux[counter]))
        counter += 1