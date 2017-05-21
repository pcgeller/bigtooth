wget https://github.com/greatscottgadgets/libbtbb/archive/2017-03-R2.tar.gz -O libbtbb-2017-03-R2.tar.gz
tar xf libbtbb-2017-03-R2.tar.gz
cd libbtbb-2017-03-R2
mkdir build
cd build
cmake ..
make
sudo make install
