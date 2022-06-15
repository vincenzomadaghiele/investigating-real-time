import oscP5.*;
import netP5.*;

OscP5 osc;
NetAddress remoteLocation;

int sensor1 = 0;
int sensorValue1 = 0;
int sensor2 = 0;
int sensorValue2 = 0;
int sensor3 = 0;
int sensorValue3 = 0;
int sensor4 = 0;
int sensorValue4 = 0;
int sensor5 = 0;
int sensorValue5 = 0;
int sensor6 = 0;
int sensorValue6 = 0;

void setup()
{
  size(600, 400);
  background(0);
  noStroke();
  textSize(12);
  osc = new OscP5(this, 5010);
}

void draw()
{
  fill(sensor1, 20, 50, 100);
  rect(0,0,200,200);
  fill(sensor2, 20, 50, 100);
  rect(200,0,200,200);
  fill(sensor3, 20, 50, 100);
  rect(400,0,200,200);
  fill(sensor4, 20, 50, 100);
  rect(0,200,200,200);
  fill(sensor5, 20, 50, 100);
  rect(200,200,200,200);
  fill(sensor6, 20, 50, 100);
  rect(400,200,200,200);

  fill(200, 200, 200);
  text(sensorValue1, 10, 30); 
  fill(200, 200, 200);
  text(sensorValue2, 210, 30); 
  fill(200, 200, 200);
  text(sensorValue3, 410, 30); 
  fill(200, 200, 200);
  text(sensorValue4, 10, 230); 
  fill(200, 200, 200);
  text(sensorValue5, 210, 230); 
  fill(200, 200, 200);
  text(sensorValue6, 410, 230); 
}

void oscEvent(OscMessage message)
{
  println("message received "+message.addrPattern());
  if(message.checkAddrPattern("/sensor/7"))
  {
    println(message.get(0).intValue());
    sensorValue1 = message.get(0).intValue();
    sensor1 = int(map(sensorValue1, 5000, 0, 0, 200));
  }
  if(message.checkAddrPattern("/sensor/11"))
  {
    println(message.get(0).intValue());
    sensorValue2 = message.get(0).intValue();
    sensor2 = int(map(sensorValue2, 5000, 0, 0, 200));
  }
  if(message.checkAddrPattern("/sensor/13"))
  {
    println(message.get(0).intValue());
    sensorValue3 = message.get(0).intValue();
    sensor3 = int(map(sensorValue3, 5000, 0, 0, 200));
  }
  if(message.checkAddrPattern("/sensor/15"))
  {
    println(message.get(0).intValue());
    sensorValue4 = message.get(0).intValue();
    sensor4 = int(map(sensorValue4, 5000, 0, 0, 200));
  }
  if(message.checkAddrPattern("/sensor/16"))
  {
    println(message.get(0).intValue());
    sensorValue5 = message.get(0).intValue();
    sensor5 = int(map(sensorValue5, 5000, 0, 0, 200));
  }
  if(message.checkAddrPattern("/sensor/18"))
  {
    println(message.get(0).intValue());
    sensorValue6 = message.get(0).intValue();
    sensor6 = int(map(sensorValue6, 5000, 0, 0, 200));
  }

}
