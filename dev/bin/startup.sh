#!/bin/bash
# arg1 = toot path of device files
# default /opt
sudo ifup wlan0
sudo service hostapd status
sh $1/bigtooth/dev/bin/rotate.sh $1
pushd $1/data/bh/current
sudo $1/blueHydra/bin/blue_hydra -d &
popd
python3 $1/bigtooth/dev/gpsSQlite.py >/dev/null &
exit 0
