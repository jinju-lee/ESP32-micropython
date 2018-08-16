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

	$ echo $PATH
	/xtensa-esp32-elf/bin 확인

### 2. Get ESP-IDF  
	
	$ cd ~/esp
	$ git clone --recursive https://github.com/espressif/esp-idf.git
	$ cd ~/esp/esp-idf
	$ git submodule update --init --recursive
	$ export IDF_PATH=~/esp/esp-idf
	$ echo $IDF_PATH
	/esp/esp-idf 확인

### 3. Start a Project
		
	$ cd ~/esp
	$ cp -r $IDF_PATH/examples/get-started/hello_world .
	$ cd ~/esp/hello_world
	$ make menuconfig

![image](https://user-images.githubusercontent.com/35492329/44190301-0efa8980-a161-11e8-9923-cec0161f5b6d.png)
	
Serial flasher config --> Default serial port --> /dev/ttyUSB0

	$ ls -al /dev/ttyUSB*
	crw-rw---- 1 root dialout 188, 0 Aug 15 22:33 /dev/ttyUSB0
	$ id
	uid=1000(pearl) gid=1000(pearl) groups=1000(pearl),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),113(lpadmin),128(sambashare)
	: dialout에 속해있지 않으므로 권한을 준다.
	$ sudo usermod -a -G dialout pearl
	$ sudo reboot 


### 4. Build and Flash
		
	$ make flash
	$ make monitor
	
