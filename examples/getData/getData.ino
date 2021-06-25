/*!
 *@file getData.ino
 *@brief 读取环境温度和相对湿度,并打印到串口
 *@copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
 *@licence     The MIT License (MIT)
 *@author [fengli](li.feng@dfrobot.com)
 *@version  V1.0
 *@date  2021-6-24
 *@get from https://www.dfrobot.com
 *@https://github.com/DFRobot/DFRobot_DHT20
*/

#include <DFRobot_DHT20.h>
/*!
 * @brief Construct the function
 * @param pWire IC bus pointer object and construction device, can both pass or not pass parameters, Wire in default.
 * @param address Chip IIC address, 0x38 in default.
 */
DFRobot_DHT20 dht20;
void setup(){

  Serial.begin(115200);
  //传感器初始化
  while(dht20.begin()){
    Serial.println("传感器初始化失败");
    delay(1000);
  }
}

void loop(){

 Serial.print("temperature:"); Serial.print(dht20.getTemperature());Serial.print("C");
 Serial.print("  humidity:"); Serial.print(dht20.getHumidity()*100);Serial.println(" %RH");

 delay(1000);

}