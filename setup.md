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
```

####RUN!
```shell
./bin/blue_hydra
```
