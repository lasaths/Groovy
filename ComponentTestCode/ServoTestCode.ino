#include <Servo.h> 

Servo myservo;

void setup() 
{ 
  myservo.attach(9);
  myservo.write(150);  // set servo to mid-point (150 Fast)
} 

void loop() {} 