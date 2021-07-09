# DFRobot_DHT20
DHT20 配有一个全新设计的 ASIC专用芯片、一个经过改进的MEMS半导体电容式湿度传感元件 <br>
和一个标准的片上温度传感元件，其性能已经大大提升甚至超出了前一代传感器的可靠性水平 <br>
新一代温湿度传感器，经过改进使其在恶劣环境下的性能更稳定。每一个传感器都经过严格的 <br>
校准和测试。由于对传感器做了改良和微型化改进，因此它的性价比更高。<br>

![正反面svg效果图](https://github.com/cdjq/DFRobot_LIS2DW12/raw/master/resources/images/SEN0245svg4.png)

## 产品链接（链接到英文商城）
    SKU：产品名称
## Table of Contents

* [Summary](#summary)
* [Installation](#installation)
* [Methods](#methods)
* [Compatibility](#compatibility)
* [History](#history)
* [Credits](#credits)

## Summary

Provide an RaspberryPi library to get Humidity and Temperature by reading data from dht20.
## Installation

Download the DFRobot_DHT20 file to the Raspberry Pi file directory, then run the following command line to use this sensor:

## Methods
```python
  '''
    @brief init function
    @return Return 0 if initialization succeeds, otherwise return non-zero and error code.
   '''
  def begin(self ):

  '''
    @brief 获取环境温度,单位为摄氏度(°C)
    @return 环境温度,量程为(-40°C ~ 80°C)
  '''
  def get_temperature(self):
     
  '''
    @brief 获取相对湿度,单位为%RH. 
    @return 相对湿度, 量程为(1-100%)
  '''
  def get_humidity(self):
```

## Compatibility

MCU                | Work Well    | Work Wrong   | Untested    | Remarks
------------------ | :----------: | :----------: | :---------: | -----
Raspberry Pi              |      √         |            |             | 


## History

- Date 2021-7-2
- Version V0.1


## Credits

Written by fengli(li.feng@dfrobot.com), 2021.7.2 (Welcome to our [website](https://www.dfrobot.com/))





