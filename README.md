# Digispark Rubber Ducky with PlatformIO

[![N|Solid](http://cdn.platformio.org/images/platformio-logo.17fdc3bc.png)](http://platformio.org/)
![Digispark_attiny](https://github.com/pedrogoliveira/rubberducky/raw/master/images/digispark_attiny_1.jpg)
![ducky](https://github.com/pedrogoliveira/rubberducky/raw/master/images/rubberducky_s.png)

## Howto for lazy people

If you have already installed platformio, have an original digispark module or any clone with micronucleus bootloader and you are as lazy as i am, this litle howto is made for you.

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

If you want to know a litle more, continue reading ...

## Installing PlatformIO
Follow install procedure at http://docs.platformio.org/en/stable/installation.html

### Testing Platformio Installation

Before using our platformio installation to program some devices, we may test some usefull commands. This will make us fill more confortable for futures steps.

***PlatformIO help screeen and version***
```sh
$ platformio --help
```
output:
```sh
Options:
  --version          Show the version and exit.
  -f, --force        Force to accept any confirmation prompts.
  -c, --caller TEXT  Caller ID (service).
  -h, --help         Show this message and exit.

Commands:
  boards    Pre-configured Embedded Boards
  ci        Continuous Integration
  device    Monitor device or list existing
  init      Initialize PlatformIO project or update existing
  lib       Library Manager
  platform  Platform Manager
  run       Process project environments
  settings  Manage PlatformIO settings
  test      Unit Testing
  update    Update installed Platforms, Packages and Libraries
  upgrade   Upgrade PlatformIO to the latest version
```
***PlatformIO version***
```sh
$ platformio --version
```
Output:
```sh
PlatformIO, version 3.0.1
```
***Listing installed platforms***
```sh
$ platformio platforms list
```
or simply (pio = platformio)
```sh
$ pio platforms list
```
Output:
```sh
atmelavr ~ Atmel AVR
====================
Atmel AVR 8- and 32-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industrys most code-efficient architecture for C and assembly programming.

Home: http://platformio.org/platforms/atmelavr
Packages: framework-arduinoavr, tool-micronucleus, toolchain-atmelavr, tool-avrdude, tool-scons
Version: 1.1.0
```
***Show details about installed platform***
```sh
$ pio platforms show atmelavr
```
Output:
```sh
atmelavr ~ Atmel AVR
====================
Atmel AVR 8- and 32-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industrys most code-efficient architecture for C and assembly programming.

Version: 1.1.0
Home: http://platformio.org/platforms/atmelavr
License: Apache-2.0
Frameworks: simba, arduino

Package tool-micronucleus
-------------------------
Type: uploader
Requirements: ~1.200.0
Installed: Yes
Description: Micronucleus
Url: https://github.com/micronucleus/micronucleus
Version: 1.200.0

Package framework-simba
-----------------------
Type: framework
Requirements: >=7.0.0
Installed: No (optional)

Package framework-arduinoavr
----------------------------
Type: framework
Requirements: ~1.10608.0
Installed: Yes
Description: Arduino Wiring-based Framework (AVR Core, 1.6)
Url: http://arduino.cc/en/Reference/HomePage
Version: 1.10608.2

Package tool-avrdude
--------------------
Type: uploader
Requirements: ~1.60001.0
Installed: Yes
Description: AVRDUDE
Url: http://www.nongnu.org/avrdude/
Version: 1.60001.1

Package tool-scons
------------------
Requirements: >=2.3.0,<2.6.0
Installed: Yes
Description: SCons software construction tool
Url: http://www.scons.org
Version: 2.4.1

Package toolchain-atmelavr
--------------------------
Type: toolchain
Requirements: ~1.40801.0
Installed: Yes
Description: avr-gcc
Url: https://gcc.gnu.org/wiki/avr-gcc
Version: 1.40801.0
```
*** Listing PlatformIO Installed Boards
```sh
$ pio boards
```
This command will output ***all*** boards available eich is a long list. However you can be more specific ...
```sh
$ pio boards uno
```
Output:
```sh
Platform: atmelavr
--------------------------------------------------------------------------------
ID                    MCU            Frequency  Flash   RAM    Name
--------------------------------------------------------------------------------
uno                   ATMEGA328P     16Mhz     31kB    2kB    Arduino Uno

Platform: espressif8266
--------------------------------------------------------------------------------
ID                    MCU            Frequency  Flash   RAM    Name
--------------------------------------------------------------------------------
espduino              ESP8266        80Mhz     4096kB  80kB   ESPDuino (ESP-13 Module)

Platform: microchippic32
--------------------------------------------------------------------------------
ID                    MCU            Frequency  Flash   RAM    Name
--------------------------------------------------------------------------------
chipkit_uc32          32MX340F512H   80Mhz     508kB   32kB   Digilent chipKIT uC32
chipkit_wf32          32MX695F512L   80Mhz     508kB   128kB  Digilent chipKIT WF32
uno_pic32             32MX320F128H   80Mhz     124kB   16kB   Digilent chipKIT UNO32
```
Another example for digispark attiny
```sh
$ pio boards digispark
```
Output:
```sh
Platform: atmelavr
--------------------------------------------------------------------------------
ID                    MCU            Frequency  Flash   RAM    Name
--------------------------------------------------------------------------------
digispark-pro         ATTINY167      16Mhz     14kB    512B   Digistump Digispark Pro (Default 16 MHz)
digispark-pro32       ATTINY167      16Mhz     14kB    512B   Digistump Digispark Pro (16 MHz) (32 byte buffer)
digispark-pro64       ATTINY167      16Mhz     14kB    512B   Digistump Digispark Pro (16 MHz) (64 byte buffer)
digispark-tiny        ATTINY85       16Mhz     5kB     512B   Digistump Digispark (Default - 16 MHz)
```

### Creating a new project
To begin with a new project, all you have to do is create a new empty folder and initialize the project for the board or boards that you plan to use.
You can start with several boards from the begining or you just start with one board and add other boards whenever you want.

##### Starting with arduino uno board
In my example, I'll just begin with arduino uno, make some tests and after that, with attiny digispark board.
![uno](https://github.com/pedrogoliveira/rubberducky/raw/master/images/uno_3.jpg)

***Initialize blink_led project***
```sh
$ mkdir blink_led && cd blink_led
$ pio init --board uno
```
Output:
```sh
The current working directory /home/pedro/Documents/iot/PlatformIO/blink_led will be used for project.
You can specify another project directory via
`platformio init -d %PATH_TO_THE_PROJECT_DIR%` command.

The next files/directories have been created in /home/pedro/Documents/iot/PlatformIO/blink_led
platformio.ini - Project Configuration File
src - Put your source files here
lib - Put here project specific (private) libraries

Project has been successfully initialized!
Useful commands:
`platformio run` - process/build project from the current directory
`platformio run --target upload` or `platformio run -t upload` - upload firmware to embedded board
`platformio run --target clean` - clean project (remove compiled files)
`platformio run --help` - additional information
```
At this point, we ended with two additional folders and a conficuration file.
Folder ***lib*** used for project libraries (see readme.txt).
folder ***src*** is the place to put our main.cpp file.
file ***platformio.ini*** is the config file. (be curiouse and take a look at this file)

***blink_led sketch***

In this example, we will make the classic program that blinks a led and we will change the frquency and pattern (delay used when led is on and off). The arduino uno board as a led built in connected to pin 13. Using vim, I created a file named **main.cpp** in **src** folder.
main.cpp:
```cpp
/**
 * Blink
 *
 * Turns on an LED on for one second,
 * then off for one second, repeatedly.
 */
#include "Arduino.h"

#define TESTPIN 13
#define INTERVAL 100

void setup()
{
  // initialize LED digital pin as an output.
  //pinMode(LED_BUILTIN, OUTPUT);
  pinMode(TESTPIN, OUTPUT);
}

void loop()
{
  // turn the LED on (HIGH is the voltage level)
  //digitalWrite(LED_BUILTIN, HIGH);
  digitalWrite(TESTPIN, HIGH);

  // wait for a second
  delay(INTERVAL);

  // turn the LED off by making the voltage LOW
  //digitalWrite(LED_BUILTIN, LOW);
  digitalWrite(TESTPIN, LOW);

   // wait for a second
  delay(INTERVAL);
}
```

***Compiling blink_led project***

For building the project, we must use the platormio run command. This command uses the init definitions to do the work. In the project base folder (the parent folder of src), if we run platformio run, the framework will builf ALL the environments defined in platformio.ini. Environments where defined with previous command platformio init. If we want to build only one environment, we must run platformio run -e <environment_name>.

```sh
$ pio run
```

Output:
```sh
[Sat Nov 12 18:27:06 2016] Processing uno (platform: atmelavr, board: uno, framework: arduino)
--------------------------------------------------------------------------------
Verbose mode can be enabled via `-v, --verbose` option
Collected 25 compatible libraries
Looking for dependencies...
Project does not have dependencies
Archiving .pioenvs/uno/libFrameworkArduinoVariant.a
Compiling .pioenvs/uno/src/main.o
Indexing .pioenvs/uno/libFrameworkArduinoVariant.a
Compiling .pioenvs/uno/FrameworkArduino/CDC.o
Compiling .pioenvs/uno/FrameworkArduino/HardwareSerial.o
Compiling .pioenvs/uno/FrameworkArduino/HardwareSerial0.o
Compiling .pioenvs/uno/FrameworkArduino/HardwareSerial1.o
Compiling .pioenvs/uno/FrameworkArduino/HardwareSerial2.o
Compiling .pioenvs/uno/FrameworkArduino/HardwareSerial3.o
Compiling .pioenvs/uno/FrameworkArduino/IPAddress.o
Compiling .pioenvs/uno/FrameworkArduino/PluggableUSB.o
Compiling .pioenvs/uno/FrameworkArduino/Print.o
Compiling .pioenvs/uno/FrameworkArduino/Stream.o
Compiling .pioenvs/uno/FrameworkArduino/Tone.o
Compiling .pioenvs/uno/FrameworkArduino/USBCore.o
Compiling .pioenvs/uno/FrameworkArduino/WInterrupts.o
Compiling .pioenvs/uno/FrameworkArduino/WMath.o
Compiling .pioenvs/uno/FrameworkArduino/WString.o
Compiling .pioenvs/uno/FrameworkArduino/_wiring_pulse.o
Compiling .pioenvs/uno/FrameworkArduino/abi.o
Compiling .pioenvs/uno/FrameworkArduino/hooks.o
Compiling .pioenvs/uno/FrameworkArduino/main.o
Compiling .pioenvs/uno/FrameworkArduino/new.o
Compiling .pioenvs/uno/FrameworkArduino/wiring.o
Compiling .pioenvs/uno/FrameworkArduino/wiring_analog.o
Compiling .pioenvs/uno/FrameworkArduino/wiring_digital.o
Compiling .pioenvs/uno/FrameworkArduino/wiring_pulse.o
Compiling .pioenvs/uno/FrameworkArduino/wiring_shift.o
Archiving .pioenvs/uno/libFrameworkArduino.a
Indexing .pioenvs/uno/libFrameworkArduino.a
Linking .pioenvs/uno/firmware.elf
Building .pioenvs/uno/firmware.hex
Calculating size .pioenvs/uno/firmware.elf
AVR Memory Usage
----------------
Device: atmega328p

Program:    1034 bytes (3.2% Full)
(.text + .data + .bootloader)

Data:          9 bytes (0.4% Full)
(.data + .bss + .noinit)


========================= [SUCCESS] Took 4.21 seconds =========================
```

As we can see, the framework did all the work. The compilation process used all the arduino libs and reported all we need about the final firmware.elf (memory usage for program alocation (flash or eprom and ram used for data). Next step is uploading to arduino board.

***Uploading firmware***

Arduino boards have a special program resident in atmega eprom (bootloader) used to upload. The process of uploading, use the usb connection and for this reason, make sure your linux user belongs to dialout group, otherwise, you will not be able to upload firmware (see: https://fedorahosted.org/fldigi/wiki/Documentation/HOWTO/Serial_Port_Setup).  

Now is time to connect the arduino uno to a free usb port, and run platformio run --target upload

```sh
$ pio run --target upload
```
Output:
```sh
[Sat Nov 12 18:47:11 2016] Processing uno (platform: atmelavr, board: uno, framework: arduino)
--------------------------------------------------------------------------------
Verbose mode can be enabled via `-v, --verbose` option
Collected 25 compatible libraries
Looking for dependencies...
Project does not have dependencies
Looking for upload port...

Warning! Please install `99-platformio-udev.rules` and check that your board's PID and VID are listed in the rules.
https://raw.githubusercontent.com/platformio/platformio/develop/scripts/99-platformio-udev.rules
Auto-detected: /dev/ttyACM0
Uploading .pioenvs/uno/firmware.hex

avrdude: AVR device initialized and ready to accept instructions

Reading | ################################################## | 100% 0.00s

avrdude: Device signature = 0x1e950f
avrdude: reading input file ".pioenvs/uno/firmware.hex"
avrdude: writing flash (1034 bytes):

Writing | ################################################## | 100% 0.20s

avrdude: 1034 bytes of flash written
avrdude: verifying flash memory against .pioenvs/uno/firmware.hex:
avrdude: load data flash data from input file .pioenvs/uno/firmware.hex:
avrdude: input file .pioenvs/uno/firmware.hex contains 1034 bytes
avrdude: reading on-chip flash data:

Reading | ################################################## | 100% 0.16s

avrdude: verifying ...
avrdude: 1034 bytes of flash verified

avrdude: safemode: Fuses OK (E:00, H:00, L:00)

avrdude done.  Thank you.

========================= [SUCCESS] Took 2.37 seconds =========================
```
***Note (Fedora 24 users):*** If you get errors with avrdude, probably you must fix an issue related with libncurses. Avrdude installed with PlatformIO relies on a different version of libncurses. To fix this issue, execute this steps after you finish creating your first project (running platformio init for the first time). 

```sh
$ dnf install avrdude-6.1-5.fc24.x86_64
```
then
```sh
$ mv ~/.platformio/packages/tool-avrdude/avrdude ~/.platformio/packages/tool-avrdude/avrdude.bck
$ ln -s /usr/bin/avrdude ~/.platformio/packages/tool-avrdude/avrdude
```
and / or
```sh
$ mv ~/.platformio/packages/toolchain-atmelavr/bin/avrdude ~/.platformio/packages/toolchain-atmelavr/bin/avrdude.bck
$ ln -s /usr/bin/avrdude ~/.platformio/packages/toolchain-atmelavr/bin/avrdude
```
 
***Back to PlatformIO***

As we can see, PlatformIO autodetects the uno board usb port in use.
We can check it usin the following:
```sh
$ pio device list
```
Output:
```sh
/dev/ttyACM0
------------
Hardware ID: USB VID:PID=2341:0043 SER=75232303135351213031 LOCATION=8-2
Description: ttyACM0
```
***Making changes***

After making any change, we must repeat all the process of compiling and uploading, however, we can make all this in one simple step.
```sh
$ pio run -e uno --target upload
```
output:
```sh
[Sat Nov 12 19:04:00 2016] Processing uno (platform: atmelavr, board: uno, framework: arduino)
--------------------------------------------------------------------------------
Verbose mode can be enabled via `-v, --verbose` option
Collected 25 compatible libraries
Looking for dependencies...
Project does not have dependencies
Compiling .pioenvs/uno/src/main.o
Linking .pioenvs/uno/firmware.elf
Checking program size .pioenvs/uno/firmware.elf
text	   data	    bss	    dec	    hex	filename
1034	      0	      9	   1043	    413	.pioenvs/uno/firmware.elf
Building .pioenvs/uno/firmware.hex
Looking for upload port...

Warning! Please install `99-platformio-udev.rules` and check that your board's PID and VID are listed in the rules.
https://raw.githubusercontent.com/platformio/platformio/develop/scripts/99-platformio-udev.rules
Auto-detected: /dev/ttyACM0
Uploading .pioenvs/uno/firmware.hex

avrdude: AVR device initialized and ready to accept instructions

Reading | ################################################## | 100% 0.00s

avrdude: Device signature = 0x1e950f
avrdude: reading input file ".pioenvs/uno/firmware.hex"
avrdude: writing flash (1034 bytes):

Writing | ################################################## | 100% 0.20s

avrdude: 1034 bytes of flash written
avrdude: verifying flash memory against .pioenvs/uno/firmware.hex:
avrdude: load data flash data from input file .pioenvs/uno/firmware.hex:
avrdude: input file .pioenvs/uno/firmware.hex contains 1034 bytes
avrdude: reading on-chip flash data:

Reading | ################################################## | 100% 0.16s

avrdude: verifying ...
avrdude: 1034 bytes of flash verified

avrdude: safemode: Fuses OK (E:00, H:00, L:00)

avrdude done.  Thank you.

========================= [SUCCESS] Took 2.43 seconds =========================
```

### Adding Digispark
![Digispark_attiny_detail](https://github.com/pedrogoliveira/rubberducky/raw/master/images/digispark_attiny_detail.png)

Before we begin with digispark, remember that if we bought any clone of digispark, we must ensure that it has micronucleus bootloader installed. If not, read my adventure [burning micronucleus in a digispark clone with arduino as a ISP](https://github.com/pedrogoliveira/rubberducky/blob/master/BurnMicronucleus.md).

***Note:*** Ubuntu, Fedora and other Linux distibutions use udev to manage device files when USB devices are added and removed. By default, udev will create a device with read-only permission which will not allow to you download code. You must place the udev rules below into a file named /etc/udev/rules.d/49-micronucleus.rules

```sh
# UDEV Rules for Micronucleus boards including the Digispark.
# This file must be placed at:
#
# /etc/udev/rules.d/49-micronucleus.rules    (preferred location)
#   or
# /lib/udev/rules.d/49-micronucleus.rules    (req'd on some broken systems)
#
# After this file is copied, physically unplug and reconnect the board.
#
SUBSYSTEMS=="usb", ATTRS{idVendor}=="16d0", ATTRS{idProduct}=="0753", MODE:="0666"
KERNEL=="ttyACM*", ATTRS{idVendor}=="16d0", ATTRS{idProduct}=="0753", MODE:="0666", ENV{ID_MM_DEVICE_IGNORE}="1"
#
# If you share your linux system with other users, or just don't like the
# idea of write permission for everybody, you can replace MODE:="0666" with
# OWNER:="yourusername" to create the device owned by you, or with
# GROUP:="somegroupname" and mange access using standard unix groups.
```
after saving this file,

```sh
$ sudo udevadm control --reload-rules
```

Returning to our pio project,
```sh
pio init --board digispark-tiny
```
Output:
```sh
...

platformio.ini - Project Configuration File
src - Put your source files here
lib - Put here project specific (private) libraries

Project has been successfully initialized!
Useful commands:
`platformio run` - process/build project from the current directory
`platformio run --target upload` or `platformio run -t upload` - upload firmware to embedded board
`platformio run --target clean` - clean project (remove compiled files)
`platformio run --help` - additional information
```

Program must be changed because digispark board don't have pin 13.
Digispark have a ltest led connected to P1 so I changed const TESTPIN to 1.

```cpp
/**
 * Blink
 *
 * Turns on an LED on for one second,
 * then off for one second, repeatedly.
 */
#include "Arduino.h"

#define TESTPIN 1
#define INTERVAL 1000

void setup()
{
  // initialize LED digital pin as an output.
  //pinMode(LED_BUILTIN, OUTPUT);
  pinMode(TESTPIN, OUTPUT);
}

void loop()
{
  // turn the LED on (HIGH is the voltage level)
  //digitalWrite(LED_BUILTIN, HIGH);
  digitalWrite(TESTPIN, HIGH);

  // wait for a second
  delay(INTERVAL);

  // turn the LED off by making the voltage LOW
  //digitalWrite(LED_BUILTIN, LOW);
  digitalWrite(TESTPIN, LOW);

   // wait for a second
  delay(INTERVAL);
}
```
Compiling and uploading to digispark .  
```sh
pio run -e digispark-tiny -t upload
```
output ((Remember that you may have to unplug and plug again your device):
```sh
[Sun Nov 13 23:25:07 2016] Processing digispark-tiny (platform: atmelavr, board: digispark-tiny, framework: arduino)
--------------------------------------------------------------------------------
Verbose mode can be enabled via `-v, --verbose` option
Collected 41 compatible libraries
Looking for dependencies...
Project does not have dependencies
Looking for upload port...
Please unplug/plug device ...
Uploading .pioenvs/digispark-tiny/firmware.hex
> Please plug in the device ...
> Press CTRL+C to terminate the program.
> Device is found!
connecting: 40% complete
> Device has firmware version 1.6
> Available space for user applications: 6012 bytes
> Suggested sleep time between sending pages: 8ms
> Whole page count: 94  page size: 64
> Erase function sleep duration: 752ms
parsing: 60% complete
> Erasing the memory ...
erasing: 80% complete
> Starting to upload ...
writing: 100% complete
>> Micronucleus done. Thank you!
========================= [SUCCESS] Took 1.99 seconds =========================
```

## ... to be continued ..


