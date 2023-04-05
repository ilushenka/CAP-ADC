import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = (26, 19, 13, 6, 5, 11, 9, 10)
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    for value in range(256):
        signal = dec2bin(value)
        GPIO.output(dac, signal)
        time.sleep(0.000001)
        compValue = GPIO.input(comp)
        if compValue == 0:
            break
    return value


try:
    while True:
        value = adc()
        V = 3.3/256 * value
        print("номер ", value, "в двоичной записи ", dec2bin(value), "поданное напряжение ", round(V, 5) )

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
                          