#include <AccelStepper.h>
#include <TimerOne.h>
 AccelStepper motor1(1, 6, 8);
AccelStepper motor2(1, 10, 12);
AccelStepper motor3(1, 7, 9);
long t = 0;



void setup() {
  Timer1.initialize(1000000);
  Timer1.attachInterrupt(motorControl);
  motor1.setMaxSpeed(1000.0);
  motor2.setMaxSpeed(1000.0);
  motor3.setMaxSpeed(1000.0);
}

void loop() {
  motor1.runSpeed();
  motor2.runSpeed();
  motor3.runSpeed();
}
void motorControl(void)
{
  t=t+1;
  double velx, vely,omega,velMotor1,velMotor2,velMotor3;
  if (t <= 3) {
      velx = 0;
      vely = 400;
      omega = 0;
      delay(1000);
    }
    else if (t > 3 && t <= 6) {
      velx = 0;
      vely = -400;
      omega= 0;
      delay(1000);
  
    }
    else if (t > 6 && t <= 9)
    {
      velx = -400;
      vely = 0;
      omega= 0;
      delay(1000);
  
    }
    else if (t > 9 && t <= 12)
    {
      velx= 400;
      vely= 0;
      omega= 0;
      delay(1000);
  
    }
    else {
      velx= 0;
      vely= 0;
      omega = 0;   
  }
   velMotor1 = (0.33 * velx) + (-0.58 * vely) + (0.33 *omega);
   velMotor2 = (0.33 *velx) + (0.58 *vely) + (0.33 *omega);
   velMotor3 = (-0.67*velx) + (0.33*omega);
    
  motor1.setSpeed(velMotor1);
  motor2.setSpeed(velMotor2);
  motor3.setSpeed(velMotor3);
}
