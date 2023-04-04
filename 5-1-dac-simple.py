import RPi.GPIO as gpio
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10] # список портов в области DAC
gpio.setmode(gpio.BCM)

comp = 4 #номер пина из области COMP
troyka = 17 #номер пина тройка-модуля
gpio.setup(dac, gpio.OUT)
gpio.setup(comp, gpio.IN)
gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)

def from10to2(x):
    x_new = bin(x)
    l = []
    for i in x_new:
        if i != 'b':
            l.append(int(i))
    l.pop(0)

    length = len(l)
    if len(l) < 8:
        length = 8 - len(l)
    for i in range(length):
        l.insert(0, 0)
    return l

def adc():
    for x in range(256):
        gpio.output(dac, from10to2(x))
        time.sleep(0.01)
        compValue = gpio.input(comp)
        if compValue == 0:
            voltage = (x / 256) * 3.3
            print(voltage, from10to2(x))
            break

try:
    while True:
        adc()

finally:
    gpio.output(dac, gpio.LOW)
    gpio.cleanup()