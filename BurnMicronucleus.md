# Burn micronucleus bootloader in 3 steps

[![Platformio](http://cdn.platformio.org/images/platformio-logo.17fdc3bc.png)](http://platformio.org/)
![Digispark_attiny](https://github.com/pedrogoliveira/rubberducky/raw/master/images/digispark_attiny_1.jpg)
![Arduino_logo](https://github.com/pedrogoliveira/rubberducky/raw/master/images/Arduino_Uno_logo.png)


This is a simple howto for burning micronucleus bootloader to attiny85 using Arduino uno, PlatformIO and avrdude.

The Digispark runs the “micronucleus tiny85” bootloader version 1.02, an open source project originally written by [Bluebie](https://github.com/Bluebie).
We are going to use the arduino uno running ArduinoISP program to act as an avr programmer. 

## 1 - Prepare your Arduino uno

In this stage, you are going to upload the ArduinoISP program to your uno board. You can find this PlatfotmIO project [here](https://github.com/pedrogoliveira/rubberducky/tree/master/ArduinoISP). The **main.cpp** file is a copy of ***ArduinoISP.ino*** with a slight modification in order to compile. (lines 162-167).

Connect you arduino to any usb port of your computer and execute the next steps:
```sh
$ git clone https://github.com/pedrogoliveira/rubberducky
$ cd rubberducky/ArduinoISP
$ pio run -e uno -t upload
```
## 2 - Connect Digispark attiny85 to uno board

Connect elements acording to this 3 pictures. 

![Attiny_arduino](https://github.com/pedrogoliveira/rubberducky/raw/master/images/attiny-arduino-ligacao-282x380.jpg)
![Attiny_esquema](https://github.com/pedrogoliveira/rubberducky/raw/master/images/attiny85-esquema_en.jpg)

```sh
Digispark     ATTINY85     UNO
----------------------------------
   5v    <-->  PIN 5  <--> Vcc +5v
  GND    <-->  PIN 4  <--> GND
   P0    <-->  PIN 8  <--> 11
   P1    <-->  PIN 7  <--> 12
   P2    <-->  PIN 6  <--> 13
   P5    <-->  PIN 1  <--> 10
   
```
Don't forget the 10uF capacitor between GND and RESET arduino pins.

![Digispark_attiny_detail](https://github.com/pedrogoliveira/rubberducky/raw/master/images/digispark_attiny_detail.png)

## 3 - Upload micronucleus bootloader

Connect again your arduino uno board to your computer usb port and follow these steps:

```sh
$ wget https://github.com/Bluebie/micronucleus/raw/master/firmware/releases/micronucleus-1.06.hex
$ avrdude -c arduino -b 19200 -P /dev/ttyACM0 -p t85 -U flash:w:micronucleus-1.06.hex -U lfuse:w:0xe1:m -U hfuse:w:0xdd:m -U efuse:w:0xfe:m$ 
```
That's all!
