# -*- coding:utf-8 -*-
"""
  *@file play.py
  *@brief Music Playing Example Program 
  *@copyright  Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  *@licence     The MIT License (MIT)
  *@author [fengli](li.feng@dfrobot.com)
  *@version  V1.0
  *@date  2020-12-02
  *@get from https://www.dfrobot.com
  *@https://github.com/DFRobot/DFRobot_PLAY_IIC
"""
import sys
import time
sys.path.append("../..")
from DFRobot_PLAY_IIC import *

IIC_MODE         = 0x01            # default use IIC1
IIC_ADDRESS      = 0x1F           # default i2c device address
'''
   # The first  parameter is to select iic0 or iic1
   # The second parameter is the iic device address
'''
DF1201S = DFRobot_PLAY_IIC(IIC_MODE ,IIC_ADDRESS)
"""
     @brief 初始化函数
"""

DF1201S.begin()

#Set volume to 20
DF1201S.set_vol(21) 
#Get volume
print("VOL: %d"%DF1201S.get_vol())
#Enter music mode
DF1201S.switch_function(DF1201S.MUSIC)
#Wait for the end of the prompt tone 
time.sleep(2)
#Set playback mode to "repeat all"
DF1201S.set_play_mode(DF1201S.ALLCYCLE)
#Get playback mode
print("PlayMode: %d"%DF1201S.get_play_mode())

#Turn on indicator LED (Power-down save)
#DF1201S.set_led(True);
#Turn on the prompt tone (Power-down save) 
#DF1201S.set_prompt(true);
#Enable amplifier chip 
#DF1201S.enable_AMP();
#Disable amplifier chip 
#DF1201S.disable_AMP();

print("Start playing")
#Start playing
DF1201S.start()
time.sleep(3)
print("Pause")
#Pause
DF1201S.pause()
time.sleep(3)
#Play the next song
DF1201S.next()
time.sleep(3)
print("Previous")
#Play the previous song
DF1201S.last()
time.sleep(3)
print("Start playing")
#Fast forward 10S
DF1201S.fast_forward(second = 10)
#Fast Rewind 10S
#DF1201S.fast_reverse(second = 10)
#Start the song from the 10th second 
DF1201S.set_play_time(second = 10)
#Get file number
print("file number:%d"%DF1201S.get_cur_file_number())
#The number of files available to play
print("The number of files available to play:%d"%DF1201S.get_total_file())
#Get the time length the current song has played 
print("The time length the current song has played:%d"%DF1201S.get_cur_time())
#Get the total length of the currently-playing song 
print("The total length of the currently-playing song:%d"%DF1201S.get_total_time())
#Get the name of the playing file 
print("The name of the currently-playing file: %s"%DF1201S.get_file_name())
#Play the file No.1, the numbers are arranged according to the sequence of the files copied into the U-disk 
#DF1201S.play_file_num(num = 1)
#Play the test.mp3 file in test folder 
#DF1201S.play_spec_file("/test/test.mp3")