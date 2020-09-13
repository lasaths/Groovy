import RPi.GPIO as GPIO
import time
SERV = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERV, GPIO.OUT)
p = GPIO.PWM(SERV, 50)
p.start(7.5)
while True:
        x = input();
        if x=='x':
            GPIO.cleanup
            break
        else:
                p.ChangeDutyCycle(int(x))
                print("Speed is " + x)
                time.sleep(2)
