import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)

p = GPIO.PWM(2, 100)

try:
    p.start(0)
    while True:
        num = float(input("Введите коэффициент заполнения: "))
        p.ChangeDutyCycle(num)
        print("Предполагаемое напряжение", 3.3 * num/100)

except ValueError:
    p.stop()

finally:
    GPIO.cleanup()

