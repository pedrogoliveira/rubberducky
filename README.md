# Digispark Rubber Ducky with PlatformIO

[![N|Solid](http://cdn.platformio.org/images/platformio-logo.17fdc3bc.png)](http://platformio.org/)
![Digispark_attiny](https://github.com/pedrogoliveira/rubberducky/raw/master/images/digispark_attiny_1.jpg)
![ducky](https://github.com/pedrogoliveira/rubberducky/raw/master/images/rubberducky_s.png)

## Howto for lazy people

If you have already installed platformio, have an original digispark module or any clone with micronucleus bootloader and you are as lazy as i am, this little how-to is made for you. If your attiny does't have micronucleus, take a look [here](https://github.com/pedrogoliveira/rubberducky/blob/master/BurnMicronucleus.md).

1. Create a new folder and copy ***Digiducky.py*** and make it executable
2. Init the project with platformio
3. Create your rubber ducky payload
4. run ***Digiducky.py*** with option ***-k PT*** to emulate a portuguese keyboard
5. Compile and upload with platformio

***Example using a linux box***

```sh
$ mkdir mySimpleDuck && cd mySimpleDuck
$ wget https://github.com/pedrogoliveira/rubberducky/raw/master/Digiducky.py && chmod +x Digiducky.py
$ pio init --board digispark-tiny
$ wget https://github.com/pedrogoliveira/rubberducky/raw/master/payload.txt
$ ./Digiducky.py -i payload.txt -o src/main.cpp -k PT
$ pio run -e digispark-tiny -t upload
```
every time you need to change your payload, just run 2 last steps.

That's It. Enjoy!

If you want to know a little more, continue reading [here](https://github.com/pedrogoliveira/rubberducky/blob/master/DigiduckyPIO.md)...



