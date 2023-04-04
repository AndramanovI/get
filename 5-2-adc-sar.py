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
    l =[128, 64, 32, 16, 8, 4, 2, 1]
    q = 0
    for x in l:
        compValue = gpio.input(comp)
        if compValue == 1:
            q = q + x
        else: q = q
    gpio.output(dac, from10to2(q))
    voltage = (q / 256) * 3.3
    print(voltage)

try:
    while True:
        adc()

finally:
    gpio.output(dac, gpio.LOW)
    gpio.cleanup()