#!/bin/bash
sudo ifup wlan0
sudo service hostapd restart
sudo service udhcpd start
sudo /home/pi/bigTooth/blue_hydra/bin/blue_hydra

exit 0
