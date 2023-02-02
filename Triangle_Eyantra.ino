
// Triangle
const int dirPin1 =8;//4C //8
const int stepPin1 = 6;//4A //6
const int dirPin2 =7;//4B //8
const int stepPin2 = 9;//2B //6
const int dirPin3=10;//2A //8
const int stepPin3 = 12;//1B //6
//According to kinematics equation 2 is x and downward(between 1 and 2) is negative y
//jis taraf wire (in stepper motor) hai wo HIGH hai

const int stepsPerRevolution =200;
long int t1,t2,t3,t4;

void setup()
{   
  pinMode(stepPin1, OUTPUT);
  pinMode(dirPin1, OUTPUT);
  pinMode(stepPin2, OUTPUT);
  pinMode(dirPin2, OUTPUT);
  pinMode(stepPin3, OUTPUT);
  pinMode(dirPin3, OUTPUT);
  
  
}
void loop()
{
  t1=millis();
  while(millis()-t1<3000)
  {
    forward();
  }

  t2=millis();
  while(millis()-t2<3000)
  {
    backward();
  }
  t3=millis();
  while(millis()-t3<3000)
  {
    backward1();
  }

  
}
void forward()
{
  digitalWrite(dirPin1, LOW);
  digitalWrite(dirPin3, HIGH);
  
  for(int x = 0; x < stepsPerRevolution; x++)
  {
    digitalWrite(stepPin1, HIGH);
    delayMicroseconds(2500);
    digitalWrite(stepPin1, LOW);
    digitalWrite(stepPin3, HIGH);
    delayMicroseconds(2500);
//    digitalWrite(stepPin3, HIGH);
    
    
    digitalWrite(stepPin3, LOW);
//    digitalWrite(stepPin3, LOW);
    
    
  }
}
void backward()
{
  digitalWrite(dirPin1, HIGH);
  digitalWrite(dirPin2, LOW);
  
  for(int x = 0; x < stepsPerRevolution; x++)
  {
    digitalWrite(stepPin1, HIGH);
    digitalWrite(stepPin2, HIGH);
    delayMicroseconds(2500);
    digitalWrite(stepPin1, LOW);
    digitalWrite(stepPin2, LOW);
    delayMicroseconds(2500);

   
    

    
  }
}
void backward1()
{
  digitalWrite(dirPin3, LOW);
  digitalWrite(dirPin2, HIGH);
  
  for(int x = 0; x < stepsPerRevolution; x++)
  {
    digitalWrite(stepPin3, HIGH);
    digitalWrite(stepPin2, HIGH);
    delayMicroseconds(2500);
    digitalWrite(stepPin3, LOW);
    digitalWrite(stepPin2, LOW);
    delayMicroseconds(2500);
  }
}
