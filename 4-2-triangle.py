import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = (26, 19, 13, 6, 5, 11, 9, 10)

GPIO.setup(dac, GPIO.OUT)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    hl = float(input("Введите период:"))/512
    while True:
        for i in range(255):
            GPIO.output(dac, dec2bin(i))
            time.sleep(hl)
        for i in reversed(range(255)):
            GPIO.output(dac, dec2bin(i))
            time.sleep(hl)
    
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    
                          
