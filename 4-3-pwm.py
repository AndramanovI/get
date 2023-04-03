import RPi.GPIO as gpio
led = # номер светодиода из области LEDS
ptn = #номер выхода для ШИМ-сигнала(выбрать необходимый)
gpio.setmode(gpio.BCM)
gpio.setup(pin, gpio.OUT)
gpio.setup(led, gpio.OUT)

try:
    frequency = float(input('Введите частоту сигнала: '))
    pwm = gpio.PWM(pin,frequency)
    p.start(0)
    print('Предполагаемое напряжение: 3.3 В')
    while True:
        duty_cycle = float(input('Введите коэффициент заполнения в процентах: '))
        pwm.start(duty_cycle)
        print('Предполагаемое напряжение: ', (duty_cycle/100)*3.3, ' В')
finally:
    pwm.stop()
    gpio.output(pin, gpio.LOW)
    gpio.output(led, gpio.LOW)
    gpio.cleanup()