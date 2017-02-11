##Set up the RPi as a WAP.
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

#Install Ubertooth
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

Install Ubertooth tools.
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
