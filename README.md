# ESP32-micropython
MicroPython on ESP32 boards

## Preparation of development environment
### 1. Set up Toolchain
		
	$ sudo apt-get install gcc git wget make libncurses-dev flex bison gperf python python-serial

	(64-bit Linux)
	$ mkdir -p ~/esp
	$ cd ~/esp
	$ wget https://dl.espressif.com/dl/xtensa-esp32-elf-linux64-1.22.0-80-g6c4433a-5.2.0.tar.gz
	$ sudo tar zxvf xtensa* -C ~/esp

	$ sudo gedit ~/.bashrc
	맨 밑에 export PATH=$HOME/esp/xtensa-esp32-elf/bin:$PATH 추가
	
	터미널 하나 더 켜서
	$ echo $PATH
	/xtensa-esp32-elf/bin 확인

	+++ Install git 
	$ sudo add-apt-repository ppa:git-core/ppa
	$ sudo apt-get update && sudo apt-get dist-upgrade
	$ sudo apt-get install git-core
	$ git version
	
### 2. Get ESP-IDF  

	$ cd ~/esp
	$ git clone --recursive https://github.com/espressif/esp-idf.git
	$ cd ~/esp/esp-idf
	$ git submodule update --init --recursive
	
	$ sudo gedit ~/.bashrc
	맨 밑에 export IDF_PATH=$HOME/esp/esp-idf$IDF_PATH 추가

	$ echo $IDF_PATH
	/esp/esp-idf 확인

### 3. Start a Project
		
	$ cd ~/esp
	$ cp -r $IDF_PATH/examples/get-started/hello_world .
	
	$ ls -al /dev/ttyUSB*
	crw-rw---- 1 root dialout 188, 0 Aug 15 22:33 /dev/ttyUSB0
	$ id
	uid=1000(pearl) gid=1000(pearl) groups=1000(pearl),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),113(lpadmin),128(sambashare)
	: dialout에 속해있지 않으므로 권한을 준다.
	$ sudo usermod -a -G dialout $USER
	$ sudo reboot
	
	$ cd ~/esp/hello_world
	$ make menuconfig

![image](https://user-images.githubusercontent.com/35492329/44190301-0efa8980-a161-11e8-9923-cec0161f5b6d.png)
	
Serial flasher config --> Default serial port --> /dev/ttyUSB0 


### 4. Build and Flash
		
	$ make flash
	$ make monitor
	

## Install MicroPython

### 1. Install MicroPython ( latest version )
[http://micropython.org/download#esp32](http://micropython.org/download#esp32) 
	
	$ wget http://micropython.org/resources/firmware/esp32-20180817-v1.9.4-465-g056e0b629.bin

### 2. Install esptool
	$ sudo apt install python-pip
	$ sudo pip install esptool
	$ ls -al /dev/ttyUSB0
	$ python -m esptool --port /dev/ttyUSB0 flash_id
	$ esptool.py --chip esp32 -p /dev/ttyUSB0 erase_flash
	$ esptool.py --chip esp32 -p /dev/ttyUSB0 write_flash -z 0x1000 esp32-20180817-v1.9.4-465-g056e0b629.bin
	$ sudo apt-get install screen
	$ sudo screen /dev/ttyUSB0 115200

### 3. Install ampy 	
	$ sudo pip install adafruit-ampy
	$ sudo pip install adafruit-ampy --upgrade

### 4. Create a MicroPython module
	$ gedit name.py
	$ ampy -p /dev/tty.SLAB_USBtoUART run name.py

	$ ampy -p /dev/tty.SLAB_USBtoUART put name.py
	$ ampy -p /dev/tty.SLAB_USBtoUART get name.py
	
	>>> import os
	>>> os.listdir()
	['boot.py', 'blink.py']
