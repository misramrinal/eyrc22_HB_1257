#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include <AccelStepper.h>
#include <Ticker.h>

Ticker blinker;

// Set WiFi credentials
#define WIFI_SSID "Sovit"
#define WIFI_PASS "123123123"
#define UDP_PORT 4210

AccelStepper motor1(1,16,5);//D0 AND D1
AccelStepper motor2(1,4,0);//D2 AND D3
AccelStepper motor3(1,14,12);//D5 AND D6

int i=0;
int s[3];
int v1,v2,v3;

// UDP
WiFiUDP UDP;
char packet[255];
char *msg;
 
void setup() 
{
  
  Serial.begin(115200);
  Serial.println();
 
  // Begin WiFi
  WiFi.begin(WIFI_SSID, WIFI_PASS);
 
  
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(100);

  }
 
  // Connected to WiFi
  

  // Begin listening to UDP port
  UDP.begin(UDP_PORT);

  
  motor1.setMaxSpeed(1000.0);
  motor2.setMaxSpeed(1000.0);
  motor3.setMaxSpeed(1000.0);
  
  blinker.attach_ms(1,motorControl); 
}

void motorControl(void)
{
  motor1.setSpeed(v1);
  motor2.setSpeed(v2);
  motor3.setSpeed(v3);
}

void loop() 
{

  motor1.runSpeed();
  motor2.runSpeed();
  motor3.runSpeed();

  // If packet received...
  int packetSize = UDP.parsePacket();
 
  if (packetSize) 
  {
    int len = UDP.read(packet, 255);
    if (len > 0)
    {
      packet[len] = 0;
    }
    
    msg = strtok(packet,",");

    while(msg!=NULL)
    {

      int x = atoi(msg);
      s[i++]= int(x);
      msg=strtok(NULL,",");
    }

    v1=s[0];
    v2=s[1];
    v3=s[2];
    
    i = 0;

  }

}
