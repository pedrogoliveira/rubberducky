# Burn micronucleus bootloader

[![Platformio](http://cdn.platformio.org/images/platformio-logo.17fdc3bc.png)](http://platformio.org/)
![Digispark_attiny](https://github.com/pedrogoliveira/rubberducky/raw/master/images/digispark_attiny_1.jpg)
![Arduino_logo](https://github.com/pedrogoliveira/rubberducky/raw/master/images/Arduino_Uno_logo.png)


This is a simple howto for burning micronucleus bootloader to attiny85 using Arduino uno, PlatformIO and avrdude.

The Digispark runs the “micronucleus tiny85” bootloader version 1.02, an open source project originally written by [Bluebie](https://github.com/Bluebie).
We are going to use the arduino uno running ArduinoISP program to act as an avr programmer. 

## Preparing Arduino uno

In this stage, you are going to upload the ArduinoISP program to your uno board. You can find this PlatfotmIO project [here](https://github.com/pedrogoliveira/rubberducky/tree/master/ArduinoISP). The **main.cpp** file is a copy of ***ArduinoISP.ino*** with a slight modification in order to compile. (lines 162-167).

Connect you arduino to any usb port of your computer and execute the next steps:
```sh
$ git clone https://github.com/pedrogoliveira/rubberducky
$ cd rubberducky/ArduinoISP
$ pio run -e uno -t upload
```
## Connecting Digispark attiny85 to uno board

Connect elements acording to this 3 pictures. 

![Attiny_arduino](https://github.com/pedrogoliveira/rubberducky/raw/master/images/attiny-arduino-ligacao-282x380.jpg)
![Attiny_esquema](https://github.com/pedrogoliveira/rubberducky/raw/master/images/attiny85-esquema_en.jpg)
![Digispark_attiny_detail](https://github.com/pedrogoliveira/rubberducky/raw/master/images/digispark_attiny_detail.png)
