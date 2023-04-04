import RPi.GPIO as gpio
import time
dac = [] # список портов в области DAC
gpio.setmode(gpio.BCM)

comp = #номер пина из области COMP
troyka = #номер пина тройка-модуля
gpio.setup(dac, gpio.OUT)
gpio.setup(comp, gpio.IN)
gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)

def from10to2(x):
    x_new = bin(x)
    l = []
    for i in x_new:
        l.append(i)
    l.pop(0)
    l.pop(0)
    return l

def adc():
    for i in range(256):
        gpio.output(dac, from10to2(x))
        time.sleep(0.01)
        compValue = gpio.input(comp)
        if compValue == 0:
            voltage = (x / 256) * 3.3
            print(voltage)
            break

try:
    while True:
        adc()

finally:
    gpio.output(dac, gpio.LOW)
    gpio.cleanup()