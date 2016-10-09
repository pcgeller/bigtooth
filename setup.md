### Install Ubertooth
sudo apt-get install cmake libusb-1.0-0-dev make gcc g++ libbluetooth-dev \
pkg-config libpcap-dev python-numpy python-pyside python-qt4

##libbtbb
Bluetooth base band library

wget https://github.com/greatscottgadgets/libbtbb/archive/2015-10-R1.tar.gz -O libbtbb-2015-10-R1.tar.gz
tar xf libbtbb-2015-10-R1.tar.gz
cd libbtbb-2015-10-R1
mkdir build
cd build
cmake ..
make
sudo make install

##Ubertooth tools
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

## Wireshark
```shell
sudo apt-get install wireshark wireshark-dev libwireshark-dev cmake
cd libbtbb-2015-10-R1/wireshark/plugins/btbb
mkdir build
cd build
cmake -DCMAKE_INSTALL_LIBDIR=/usr/lib/x86_64-linux-gnu/wireshark/libwireshark3/plugins ..
make
sudo make install
```

##Wireshark with BT BR/EDR
```shell
sudo apt-get install wireshark wireshark-dev libwireshark-dev cmake
cd libbtbb-2015-10-R1/wireshark/plugins/btbredr
mkdir build
cd build
cmake -DCMAKE_INSTALL_LIBDIR=/usr/lib/x86_64-linux-gnu/wireshark/libwireshark3/plugins ..
make
sudo make install
```
## Blue Hydra
Install dependencies.
```shell
sudo apt-get install bluez  python-bluez python-dbus libsqlite3-dev
```
#Ruby
bh is written in ruby.  naturally you need to have ruby installed.
```shell
sudo apt-get install ruby ruby-dev
```
Get the package dependences for bh.  This takes awhile.
```shell
sudo gem install bundle --no-ri --no-rdoc
sudo gem install rake -v '11.2.2' --no-ri --no-rdoc
sudo gem install addressable -v '2.4.0'--no-ri --no-rdoc
sudo gem install coderay -v '1.1.1' --no-ri --no-rdoc
sudo gem install do_sqlite3 -v '0.10.17' --no-ri --no-rdoc
sudo gem install dm-sqlite-adapter -v '1.2.0' --no-ri --no-rdoc

bundle install
```

##Install git
Need to clone the code from github repos.  
```shell
sudo apt-get install git
```

Get blue_hydra hostcode.
```
sudo git clone https://github.com/pwnieexpress/blue_hydra
cd ./blue_hydra
bundle install
```
Interesting feature of Ruby.  Ruby packages install into a project folder.

##Your Bluetooth device
Make sure it's running.  Check first.
modprobe -v btusb
```shell
service --status-all
sudo service bluetooth start
sudo apt-get install bluez-dev bluez-tools
```
List bluetooth devices:
hcitool dev
sudo /etc/init.d/bluetooth start
/etc/init.d/bluetooth status

https://learn.adafruit.com/install-bluez-on-the-raspberry-pi/installation
####RUN!
```shell
./bin/blue_hydra
```

##Troubleshooting
If you get an error similar to :
```shell
Unable to read the mac address from hci0
```
then your system can't find your bluetooth device.  Some helpful commands:

**modprobe btusb**: ensure the btusb drive kernel module is loaded.
**lsusb**: list all connected usb devices.  
**hciconfig**: change the status of the bluetooth device

be sure to check help with something similar to -h or --help.

#####ARGH

Bluez5 (installed from pacman on Debian) is packaged differently than previous versions - bluez-utils is no longer a seperate package.  It's rolled up with the bluez package.  Blue_hydra can't detect this and looks like bluez4 is a requirement.  Blue_hydra only works with bluez4.  Trying to force install of bluez version 4 on debian jessie (rpi3).  

```shell
sudo nano /etc/apt/sources.list
```
Comment out all lines.  Add:
```shell
deb http://ftp.us.debian.org/debian wheezy main contrib non-free
sudo apt-get update
```
Ran into problems with encryption certs.  Thanks for the service MIT.
```shell
gpg --keyserver pgpkeys.mit.edu --recv-key 8B48AD6246925553 7638D0442B90D010 6FB2A1C265FFB764
gpg -a --export 8B48AD6246925553 | sudo apt-key add -
gpg -a --export 7638D0442B90D010 | sudo apt-key add -
gpg -a --export 6FB2A1C265FFB764 | sudo apt-key add -
sudo apt-get update
```

Just use the older package.
```shell
apt-cache showpkg bluez
sudo apt-get install bluez='4.99-2'
sudo apt-mark hold bluez
sudo apt-get install bluetooth='4.99-2'
sudo apt-mark hold bluetooth
sudo apt-get install bluez-utils='4.99-2'
sudo apt-mark hold bluez-utils
sudo apt-get install bluez-cups='4.99-2'
sudo apt-mark hold bluez-cups
```

###Alternative fix - use an older version of debian - wheezy

Install bluez4
```shell
wget http://www.kernel.org/pub/linux/bluetooth/bluez-4.101.tar.xz
tar xvf bluez-4.101.tar.xz
cd bluez-4.101
sudo apt-get update
sudo apt-get install -y libusb-dev libdbus-1-dev libglib2.0-dev libudev-dev libical-dev libreadline-dev
./configure
make
sudo make install
```
