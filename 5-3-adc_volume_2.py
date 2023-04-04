import time
dac = [] # список портов в области DAC
gpio.setmode(gpio.BCM)
leds = [] # список портов в области LEDS

comp = #номер пина из области COMP
troyka = #номер пина тройка-модуля
gpio.setup(dac, gpio.OUT)
gpio.setup(leds, gpio.OUT)
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
    l = [128, 64, 32, 16, 8, 4, 2, 1]
    q = 0
    for x in l:
        compValue = gpio.input(comp)
        if compValue == 1:
            q = q + x
        else:
            q = q
    gpio.output(dac, from10to2(q))
    volume = int((q / 256) * 8)
    l2 = []
    for i in range(7-volume):
        l2.append(0)
        for j in range(volume):
                l2.append(1)
    gpio.output(leds, l2)

try:
    while True:
        adc()

finally:
    gpio.output(dac, gpio.LOW)
    gpio.output(leds, gpio.LOW)
    gpio.cleanup()