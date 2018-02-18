#!/bin/bash
sudo ifup wlan0
sudo service hostapd status
sh /opt/bigtooth/device/bin/rotate.sh
pushd /home/pi/bigtooth/data
sudo /home/pi/bigtooth/blue_hydra/bin/blue_hydra -d &
popd
python3 /home/pi/bigtooth/device/gpsSQlite.py >/dev/null &
exit 0
