import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

dac = (26, 19, 13, 6, 5, 11, 9, 10)

GPIO.setup(dac, GPIO.OUT)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while True:
        num_in = input("Введите число от 0 до 255(для завершение введите q): ")
        if num_in[0] == "q":
            print("Завершение программы")
            break
        if int(num_in) < 0 or int(num_in) > 255:
            print("Значение не входит в требуемый диапазон")
            continue
        num = dec2bin(int(num_in))
        GPIO.output(dac,num)
        V = 3.3/256 * int(num_in)
        print("Примерное напряжение :", V)
except ValueError:
    print("Введено некорректное значение")
    
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
                          