#!/bin/bash
sudo ifup wlan0
sudo service hostapd status
pushd /home/pi/bigtooth2/i
sudo /home/pi/bigtooth/blue_hydra/bin/blue_hydra -d & 	
popd
python3 /home/pi/bigtooth2/gpsPG.py >/dev/null &
sh /home/pi/bigtooth2/bin/rotate.sh
exit 0
