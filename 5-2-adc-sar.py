import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = (26, 19, 13, 6, 5, 11, 9, 10)[::-1]
comp = 4
troyka = 17
num = [0] * 8

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
def bin2dec(num):
    sum = 0
    for i in range(8):
        sum *= 2
        sum += num[i]
    return sum

def adc():
    num = [0] * 8
    for i in reversed(range(8)):
        num[i] = 1
        GPIO.output(dac, num)
        time.sleep(0.001)
        compValue = GPIO.input(comp)
        if compValue == 0:
            num[i] = 0
        #print(num, i)
    value = bin2dec(num[::-1])      
    #print(num)
    return value


try:
    while True:   
        value = adc()
        V = 3.3/256 * value
        print("номер ", "value", "в двоичной записи ", dec2bin(value), "поданное напряжение ", round(V, 5) )

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
                          