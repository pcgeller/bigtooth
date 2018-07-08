#!/bin/bash
# arg1 = toot path of device files
# default /opt
sudo ifup wlan0
sudo service hostapd status
sh $1/bigtooth/dev/bin/rotate.sh $1
cd $1/data/bh/current
sudo $1/blueHydra/bin/blue_hydra -d &
echo "Blue Hydra started."
cd /
python3 $1/bigtooth/dev/gpsSQlite.py > /home/pi/scratch/python &
echo "GPS logger started."
exit 0
