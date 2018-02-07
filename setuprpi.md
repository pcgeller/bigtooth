
# bigtooth

bigtooth streams bluetooth device metadata into storage.  

bigtooth captures bluetooth related data on individual devices.  Many of these devices can be attributed to an individual.   This gives you data to do things like pattern of life analysis.  This intelligence technique teaches


## Update dependencies
Installs bluez, the bluetooth driver package for linux.  Also contains `hcitools` and `hciconfig` which are amazing low-level commands to bluetooth.
```shell
ls
```

## Install gpsd
Gets the GPS going.  Pulling data from space. :) **Code to store this data in a db comes later.**

Find the GPS over USB.
```shell
ls /dev/ttyUSB*
sudo lsusb #Prolific PL2303
sudo cat /dev/ttyUSB0
```

Install gpsd and set the input for gpsd to the GPS connection.  In this case the USB port.  Run.
```shell
sudo apt-get install gpsd gpsd-clients python-gps
sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock
cgps
```

## Set up the RPi as a WAP.
This is very incomplete.  The rPi works as a wireless access point (WAP) but I didn't document the proces.
Make sure AP is listed as a a supported interface mode.
```shell
iw list
```
Get access point daemon.
```shell
sudo apt-get install hostapd
```
Edit the /etc/network/interfaces to set static IP.  It should look like:
```shell
iface wlan0 inet static
address 10.0.0.1
netmask 255.255.255.0
```

# Bluetooth
Commands to install and setup BlueHydra and Ubertooth.  

## Install BlueHydra
```shell
sudo apt-get install bluetooth libbluetooth-dev
```

## Install Ubertooth
Install OS packages.
```shell
sudo apt-get update
sudo apt-get install cmake libusb-1.0-0-dev make gcc g++ libbluetooth-dev \
pkg-config libpcap-dev python-numpy python-pyside python-qt4
```
Install Bluetooth baseband library(libbtbb) that is used to decode packets.
```shell
wget https://github.com/greatscottgadgets/libbtbb/archive/2015-10-R1.tar.gz -O libbtbb-2015-10-R1.tar.gz
tar xf libbtbb-2015-10-R1.tar.gz
cd libbtbb-2015-10-R1
mkdir build
cd build
cmake ..
make
sudo make install
```

## Install Ubertooth tools.
```shell
wget https://github.com/greatscottgadgets/ubertooth/releases/download/2015-10-R1/ubertooth-2015-10-R1.tar.xz -O ubertooth-2015-10-R1.tar.xz
tar xf ubertooth-2015-10-R1.tar.xz
cd ubertooth-2015-10-R1/host
mkdir build
cd build
cmake ..
make
sudo make install
```

Switch to the $UBERTOOTH/host folder and return.  It's ok if the build dir exists.
```shell
mkdir build
cd build/
cmake ..
sudo make
sudo make install
```

**You make need to run `sudo ldconfig` so that the OS knows about the install**

Now you can run commands such as:
```shell
ubertooth-rx #sniff lower address part or LAP
ubertooth-util -v #get version -V is more verbose
ubertooth-scan #-s for hci
```

Blue hydra should also automatically pick up ubertooth now.  

# Setup ubuntu and python to run bigtooth

## Ubuntu dependencies
```shell
sudo apt-get update
sudo apt-get install bluetooth libbluetooth-dev python3-pip ipython
```

## Setup and run virtual Environment
```shell
pip3 install virtualenv
virtualenv bigtooth #Creates virtual Environment
source bigtooth/bin/activate #activates env
```

## python dependencies
```shell
pip3 install setuptools --upgrade
pip3 install numpy #takes about 45 mins
pip3 install scikit-learn
pip3 install pandas
pip3 install pybluez
pip3 install gpsd-py3
```
