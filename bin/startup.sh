#!/bin/bash
sudo ifup wlan0
sudo service hostapd status
sh /home/pi/bigtooth2/bin/rotate.sh
pushd /home/pi/bigtooth2/db/
sudo /home/pi/bigtooth/blue_hydra/bin/blue_hydra -d &
popd
python3 /home/pi/bigtooth2/gpsSQlite.py >/dev/null &
exit 0
