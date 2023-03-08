import RPi.GPIO as gpio
import time
leds = []
gpio.setmode(gpio.BCM)
gpio.setup(leds, gpio.OUT)
while True:
    for i in range(3):
        for j in leds:
            gpio.output(j, 1)
            time.sleep(0.2)
            gpio.output(j, 0)
    gpio.cleanup()