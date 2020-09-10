import RPi.GPIO as GPIO
import time
SERV = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERV, GPIO.OUT)
p = GPIO.PWM(SERV, 50)
p.start(7.5)
try:
        while True:
                p.ChangeDutyCycle(7.5)
                time.sleep(1)
                p.ChangeDutyCycle(12.5)
                time.sleep(1)
                p.ChangeDutyCycle(2.5)
                time.sleep(1)

except KeyboardInterrupt:
        GPIO.cleanup()