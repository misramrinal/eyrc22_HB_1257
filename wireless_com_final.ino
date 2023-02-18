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
int i,k=0;
String s[3];
float v1,v2,v3;

// UDP
WiFiUDP UDP;
char packet[255];
char reply[] = "Packet received!";
 
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
    Serial.print("Packet received: ");
    Serial.println(packet);
    for(i=0;i<255;i++)
    {
//      if(packet[i]==' ')
//      break;
      if(packet[i]==',')
      k++;
      else
      s[k]=s[k]+packet[i];
     
     
    }
    k=0;
    v1=100*(s[0].toFloat());
    v2=100*(s[1].toFloat());
    v3=100*(s[2].toFloat());
    s[0]="";
    s[1]="";
    s[2]="";
    Serial.println(v1);
    Serial.println(v2);
    Serial.println(v3);
   
    motor1.setSpeed(v1);
    motor2.setSpeed(v2);
    motor3.setSpeed(v3);
    //Running the motor
//    motor1.runSpeed();
//    motor2.runSpeed();
//    motor3.runSpeed();
//    

    // Send return packet
    UDP.beginPacket(UDP.remoteIP(), UDP.remotePort());
    UDP.write(reply);
    UDP.endPacket();

  }

}

void motorControl(void)
{
  motor1.runSpeed();
  motor2.runSpeed();
  motor3.runSpeed();
}
