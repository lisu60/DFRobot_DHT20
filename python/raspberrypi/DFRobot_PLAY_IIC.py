# -*- coding: utf-8 -*
import serial
import time
import smbus
                

class DFRobot_PLAY_IIC(object):


  
  ''' register configuration '''
  I2C_ADDR                = 0x50
  MUSIC = 1         #Music Mode 
  UFDISK = 2        #Slave mode 
 
  SINGLECYCLE = 1   #Repeat one song 
  ALLCYCLE = 2      #Repeat all 
  SINGLE = 3        #Play one song only 
  RANDOM = 4        #Random
  FOLDER = 5        #Repeat all songs in folder 
  ERROR  = 6           
  curFunction = MUSIC
  ''' Conversion data '''
  #txbuf      = [0]
  _addr      =  0x50
  #_mode      =  0
  #   idle =    0
  def __init__(self ,bus,address):
    self.i2cbus = smbus.SMBus(bus)
    self._addr = address
    self.idle =    0

  def begin(self ):
    string,length= self.pack()
    #self.i2cbus.write_byte(self._addr,0xaa)
    time.sleep(0.5)
    self.write_AT_command(string,length)
    if self.read_ack(4) == 'OK\r\n':
      return True
    else:
      return False
  def get_vol(self):
    vol = "  "
    string,length = self.pack("VOL","?")
    self.write_AT_command(string,length)
    ack = self.read_ack(12)
    vol += ack[7]
    if ack[8] != 0x5d:
      vol += ack[8]
    return int(vol)
  def set_vol(self,vol):

   string,length = self.pack("VOL",str(vol))
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False

  def get_play_mode(self):
    mode = "  "
    string,length = self.pack("PLAYMODE","?")
    self.write_AT_command(string,length)
    ack = self.read_ack(13)
    mode = ack[10]
    if ack[11] == '\r' and ack[12] == '\n':
      return int(mode)
    else:
      return self.ERROR
  def switch_function(self,function):
   string,length = self.pack("FUNCTION",str(function))
   self.write_AT_command(string,length)
   self.pauseFlag = 0
   if self.read_ack(4) == "OK\r\n":
    time.sleep(1.5)
    return True
   else:
    return False

  def set_play_mode(self,mode):
   if self.curFunction != self.MUSIC:
     return False
   string,length = self.pack("PLAYMODE",str(mode))
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False

  def set_led(self,om):
   mode = "   "
   if on == True:
     mode = "ON"
   else:
     mode = "OFF"
   string,length = self.pack("LED",mode)
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False
 
  def set_prompt(self,on):
   if on == True:
     mode = "ON"
   else:
     mode = "OFF"
   string,length = self.pack("PROMPT",mode)
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False

  def next(self):
   if self.curFunction != self.MUSIC:
     return False
   string,length = self.pack("PLAY","NEXT")
   self.write_AT_command(string,length)
   pauseFlag = 1
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False

  def last(self):
   if self.curFunction != self.MUSIC:
     return False
   string,length = self.pack("PLAY","LAST")
   self.write_AT_command(string,length)
   pauseFlag = 1
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False
    
  def start(self):
   if self.curFunction != self.MUSIC:
     return False
   pauseFlag = 1
   string,length = self.pack("PLAY","PP")
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False

  def pause(self):
   if self.curFunction != self.MUSIC:
     return False
   pauseFlag = 0
   string,length = self.pack("PLAY","PP")
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False

  def delCurFile(self):
   if self.curFunction != self.MUSIC:
     return False
   string,length = self.pack("DEL")
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False
    
  def play_spec_file(self,name):
   if self.curFunction != self.MUSIC:
     return False
   string,length = self.pack("PLAYFILE",name)
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False

  def play_file_num(self,num):
   if self.curFunction != self.MUSIC:
     return False
   string,length = self.pack("PLAYFILE",str(num))
   self.write_AT_command(string,length)
   print(string)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False
    
  def fast_forward(self,second):
   if self.curFunction != self.MUSIC:
     return False
   cmd = "+" + str(second)
   string,length = self.pack("TIME","cmd")
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False

  def fast_reverse(self,second):
   if self.curFunction != self.MUSIC:
     return False
   cmd = "-" + str(second)
   string,length = self.pack("TIME","cmd")
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False
    
  def set_play_time(self,second):
   if self.curFunction != self.MUSIC:
     return False
   string,length = self.pack("TIME",str(second))
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False
  def get_int(self,string):
    num_len = 0
    num = 0
    
    for i in range(0,len(string)):
      if string[i] != '\r' and string[i+1] != '\n':
        num_len += 1
      else:
        break
    for i in range(0,num_len):
      num = num*10 + ord(string[i]) - ord('0')
    return num


  def get_cur_time(self):
   if self.curFunction != self.MUSIC:
     return False

   string,length = self.pack("QUERY","3")
   self.write_AT_command(string,length)
   cur_time = self.read_ack(6)
   return self.get_int(cur_time)
    
  def enable_AMP(self):
   if self.curFunction != self.MUSIC:
     return False
   string,length = self.pack("AMP","ON")
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False
    
  def disable_AMP(self):
   if self.curFunction != self.MUSIC:
     return False
   string,length = self.pack("AMP","OFF")
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False
    
  def get_total_time(self):
   if self.curFunction != self.MUSIC:
     return False
   string,length = self.pack("QUERY","4")
   self.write_AT_command(string,length)
   total_time = self.read_ack(6)
   return self.get_int(total_time)
    
  def get_cur_file_number(self):
   if self.curFunction != self.MUSIC:
     return False
   string,length = self.pack("QUERY","1")
   self.write_AT_command(string,length)
   cur_number = self.read_ack(6)
   return self.get_int(cur_number)

  def get_total_file(self):
   if self.curFunction != self.MUSIC:
     return False

   string,length = self.pack("QUERY","2")
   self.write_AT_command(string,length)
   total_file = self.read_ack(6)
   return self.get_int(total_file)

  def get_file_name(self):
   if self.curFunction != self.MUSIC:
     return "get file name error"
   string,length = self.pack("QUERY","5")
   self.write_AT_command(string,length)
   name = self.read_ack(0)
   return name 
  def pack(self,cmd = " ",para = " "):
    atCmd = ""
    atCmd += "AT"
    if cmd != " ":
      atCmd += "+"
      atCmd += cmd
    
    if para != " ":
     atCmd += "="
     atCmd += para

    atCmd += "\r\n";
    at_str = atCmd;
    at_length = len(at_str)
    return at_str,at_length
  def write_AT_command(self, data,len1):
    #self.i2cbus = smbus.SMBus(1)
    #self._addr = address
    #list1 = list(data)
    #for i in range(0,len1):
      #list1[i] = ord(list1[i])
    #self.i2cbus.write_i2c_block_data(self._addr,0,list1)
    self.read(24)
    time.sleep(0.1)
    for i in range(0,len1):
      self.i2cbus.write_byte(self._addr ,ord(data[i]))
      #print(ord(data[i]))
    #self.i2cbus.write_i2c_block_data(self._addr,0,[0,0,0])
  
  def read_ack(self,len):
    offset = 0
    data = [0]*108
    ack = ""
    time.sleep(0.1)
    if len == 0:
      data = self.read(108)
      for i in range(0,108):
        ack += chr(data[i])
        offset += 1
        if(ack[offset - 1]) == '\n' and (ack[offset-2]) =='\r':
          break
    else:
      data = self.read(len)
      for i in range(0,len):
        ack += chr(data[i])
        #print(data[i])
        offset += 1
        if(ack[offset - 1]) == '\n' and (ack[offset-2]) =='\r':
          ack += chr(0)
          break
    #print(ack)
    return ack
  def read(self,len):
    #self.i2cbus.write_byte(self._addr,1)
    rslt = [0]*108 
    time.sleep(0.01)
    #rslt = self.i2cbus.read_i2c_block_data(self._addr,0xff,len)
    for i in range(0,len):
       time.sleep(0.01)
       rslt[i] = self.i2cbus.read_byte(self._addr)
    #print(rslt)
    return rslt