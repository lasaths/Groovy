from time import sleep
import RPi.GPIO as GPIO

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
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(SLP, GPIO.OUT)

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

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("o-On s-Stop e-Extrude r-Retract x-Exit")
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
    
    elif x=='x':
        GPIO.output(SLP, GPIO.LOW) #No Cleanup GPIO as it makes Stepper go undefined and start turning
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
    
