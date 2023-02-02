#include <AccelStepper.h>
#include <TimerOne.h>

AccelStepper motor1(1,6,8);
AccelStepper motor2(1,10,12);
AccelStepper motor3(1,7,9);
long t;
void motorControl(void)
{
  double velx=0,vely=0,omega=0,velMotor1,velMotor2,velMotor3;
  int rad=350;
  t=micros();
  velx=(-rad)*sin(t);
  vely=(rad)*cos(t);
  omega=0;
  //Inverse Kinematics equation
  velMotor1= (0.33*velx)-(0.58*vely)+(0.33*omega);
  velMotor2=(0.33*velx)+(0.58*vely)+(0.33*omega);
  velMotor3=(-0.67*velx)+(0.33*omega);

  motor1.setSpeed(velMotor1);
  motor2.setSpeed(velMotor2);
  motor3.setSpeed(velMotor3);

 //Setting up motor speed
 motor1.setMaxSpeed(1000.0);
 motor2.setMaxSpeed(1000.0);
 motor3.setMaxSpeed(1000.0);
  
  
  
  
}

void setup() {
  Timer1.initialize(1000000);
  Timer1.attachInterrupt(motorControl);
  motor1.setMaxSpeed(1000);
  motor2.setMaxSpeed(1000);
  motor3.setMaxSpeed(1000);
  
  

}

void loop() {
  motor1.runSpeed();
  motor2.runSpeed();
  motor3.runSpeed();

}
