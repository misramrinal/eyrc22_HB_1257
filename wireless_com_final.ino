#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include <AccelStepper.h>
#include <Ticker.h>
Ticker blinker;
 
// Set WiFi credentials
#define WIFI_SSID "Mrinal"
#define WIFI_PASS "mrinal1729"
#define UDP_PORT 4210
AccelStepper motor1(1,26,25);//D0 AND D1
AccelStepper motor2(1,14,12);//D2 AND D3
AccelStepper motor3(1,13,16);//D5 AND D6
int i,k=0;
int s[3];
int v1,v2,v3;

// UDP
WiFiUDP UDP;
char packet[255];
char *msg;
 
void setup() {
  // Setup serial port
  Serial.begin(115200);
  Serial.println();
 
  // Begin WiFi
  WiFi.begin(WIFI_SSID, WIFI_PASS);
 
  // Connecting to WiFi...
  Serial.print("Connecting to ");
  Serial.print(WIFI_SSID);
  // Loop continuously while WiFi is not connected
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(100);
    Serial.print(".");
  }
 
  // Connected to WiFi
  Serial.println();
  Serial.print("Connected! IP address: ");
  Serial.println(WiFi.localIP());

  // Begin listening to UDP port
  UDP.begin(UDP_PORT);
  Serial.print("Listening on UDP port ");
  Serial.println(UDP_PORT);
  motor1.setMaxSpeed(1000.0);
  motor2.setMaxSpeed(1000.0);
  motor3.setMaxSpeed(1000.0);
  blinker.attach_ms(1,motorControl);
 
}

void loop() {

  // If packet received...
  int packetSize = UDP.parsePacket();
  if (packetSize) {
    Serial.print("Received packet! Size: ");
    Serial.println(packetSize);
    int len = UDP.read(packet, 255);
    if (len > 0)
    {
      packet[len] = '\0';
    }
//    Serial.print("Packet received: ");
//    Serial.println(packet);
//    for(i=0;i<255;i++)
//    {
////      if(packet[i]==' ')
////      break;
//      if(packet[i]==',')
//      k++;
//      else
//      s[k]=s[k]+packet[i];
//    }


msg = strtok(packet,",");
int i =0;
while(msg!=NULL)
{
  s[i]=atoi(msg);
  msg=strtok(NULL,",");
  i++;
}






    k=0;
    v1=s[0];
    v2=s[1];
    v3=s[2];
    
    
//    Serial.println(v1);
//    Serial.println(v2);
//    Serial.println(v3);
//    delay(150);
   
    motor1.setSpeed(v1);
    motor2.setSpeed(v2);
    motor3.setSpeed(v3);
    //Running the motor
//    motor1.runSpeed();
//    motor2.runSpeed();
//    motor3.runSpeed();
//    

    // Send return packet
//    UDP.beginPacket(UDP.remoteIP(), UDP.remotePort());
//    UDP.write(reply);
//    UDP.endPacket();

  }

}

void motorControl(void)
{
  motor1.runSpeed();
  motor2.runSpeed();
  motor3.runSpeed();
}
