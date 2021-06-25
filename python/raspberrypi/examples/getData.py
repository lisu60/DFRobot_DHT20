# -*- coding:utf-8 -*-
"""
  *@file getData.ino
  *@brief 读取环境温度和相对湿度,并打印到串口
  *@copyright  Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  *@licence     The MIT License (MIT)
  *@author [fengli](li.feng@dfrobot.com)
  *@version  V1.0
  *@date  2020-12-02
  *@get from https://www.dfrobot.com
  *@https://github.com/DFRobot/DFRobot_DHT20
"""
import sys
import time
sys.path.append("../")
from DFRobot_DHT20 import *

IIC_MODE         = 0x01            # default use IIC1
IIC_ADDRESS      = 0x38           # default i2c device address
'''
   # The first  parameter is to select iic0 or iic1
   # The second parameter is the iic device address
'''
dht20 = DFRobot_DHT20(IIC_MODE ,IIC_ADDRESS)
"""
     @brief 初始化函数
"""

dht20.begin()

while True:
  #读取环境温度和相对湿度,并打印到终端 
  print("temperature::%f C"%dht20.get_temperature())
  print("humidity::%f RH"%dht20.get_humidity())
  time.sleep(1)