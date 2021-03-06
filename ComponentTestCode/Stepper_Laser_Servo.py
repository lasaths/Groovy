from time import sleep
import RPi.GPIO as GPIO

SERV = 1 # Servo
LAS = 23# Laser Pin
DIR = 20   # Direction GPIO Pin (Brown Brown)
STEP = 21  # Step GPIO Pin (Purple Yellow)
SLP = 16   #Sleep GPIO Pin (Grey Green)
#GND (Blue Purple)
#VCC (Green Blue)
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 200   # Steps per Revolution (360 / 1.8)
step_count = SPR
delay = .001
extrudecount = 0;


#Setting up GPIO Outputs
GPIO.setmode(GPIO.BCM)
GPIO.setup(LAS,GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(SLP, GPIO.OUT)
GPIO.setup(SERV,GPIO.OUT)

servo = GPIO.PWM(SERV,50)

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
print("o-On d,f,g - Forward (slow,medium,fast) b - Backward h - Halt s-Stop e-Extrude r-Retract l-Laser Cycle x-Exit")
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
        if extrudecount < 5:
            print("Extrude")
            stepperdrive(400,"CW")
            extrudecount += 1
            x='z'
        else:
            print("Extrude Limit Reached (5)")

    elif x=='r':
        if extrudecount > 0:
            print("Retract")
            stepperdrive(400,"CCW")
            extrudecount -= 1
            x='z'
        else:
            print("Retract Limit Reached (0)")

    elif x=='l':
        print("Laser Cycle")
        lasercycle(2)
        x='z'

    elif x=='f':
        print("Forward Medium")
        servo.start(9)
        x='z'

    elif x=='g':
        print("Forward Fast")
        servo.start(10)
        x='z'

    elif x=='d':
        print("Forward Slow")
        servo.start(8)
        x='z'
        
    elif x=='k':
        print("Halt")
        servo.ChangeDutyCycle(6.85)
        print("Extruding")
        sleep(5) #extruding
        servo.ChangeDutyCycle(8) #move forward
        sleep(2)
        print("Halt")
        servo.ChangeDutyCycle(6.85)
        print("Laser Cycle")
        lasercycle(4)
        print("Forward Slow")
        servo.ChangeDutyCycle(8)
        x='z'

    elif x=='h':
        print("Halt")
        servo.ChangeDutyCycle(6.85)
        x='z'

    elif x=='b':
        print("Backward")
        servo.ChangeDutyCycle(5)
        x='z'
        
    elif x=='v':
        print("Backward Slow")
        servo.ChangeDutyCycle(6)
        x='z'
    
    elif x=='x':
        GPIO.output(SLP, GPIO.LOW) #No Cleanup GPIO as it makes Stepper go undefined and start turning
        GPIO.cleanup()
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
    
