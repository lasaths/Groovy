from time import sleep
import RPi.GPIO as GPIO

SERV = 6 # Servo
LAS = 26 # Laser Pin
DIR = 20   # Direction GPIO Pin
STEP = 21  # Step GPIO Pin
SLP = 16   #Sleep GPIO Pin
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 200   # Steps per Revolution (360 / 1.8)
step_count = SPR
delay = .001


#Setting up GPIO Outputs
GPIO.setmode(GPIO.BCM)
GPIO.setup(LAS,GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(SLP, GPIO.OUT)
GPIO.setup(SERV,GPIO.OUT)

servo = GPIO.PWN(SERV,50)

def stepperdrive(count,direction):
    if direction == "CW":
        GPIO.output(DIR, CW)
    if direction == "CCW":
        GPIO.output(DIR, CCW)
    for x in range(count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
        if (x == count):
            print(x)

def lasercycle(time):
    GPIO.output(LAS,GPIO.HIGH)
    sleep(time)
    GPIO.output(LAS,GPIO.LOW)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("o-On f - Forward h - Halt s-Stop e-Extrude r-Retract l-Laser Cycle x-Exit")
print("\n")

GPIO.output(SLP, GPIO.LOW) # Turn off Stepper to Start
   
while(1):

    x = input()
    
    if x=='o':
        print("On")
        GPIO.output(SLP, GPIO.HIGH) #Turn on Stepper
        x='z'

    elif x=='s':
        print("Stop")
        GPIO.output(SLP, GPIO.LOW) #Turn Off Stepper
        x='z'

    elif x=='e':
        print("Extrude")
        stepperdrive(800,"CW")
        x='z'

    elif x=='r':
        print("Retract")
        stepperdrive(800,"CCW")
        x='z'

    elif x=='l':
        print("Laser Cycle")
        lasercycle(2000)
        x='z'

    elif x=='f':
        print("Forward")
        servo.start(2.5)
        p.ChangeDutyCycle(7.5)
        x='z'

    elif x=='h':
        print("Halt")
        servo.start(2.5)
        p.ChangeDutyCycle(7.5)
        x='z'
    
    elif x=='x':
        GPIO.output(SLP, GPIO.LOW) #No Cleanup GPIO as it makes Stepper go undefined and start turning
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
    