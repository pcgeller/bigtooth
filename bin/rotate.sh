#!/bin/bash
today=`date '+%Y_%m_%d__%H_%M'`;

echo $today

bhdbfilename="/home/pi/bigtooth2/db/$today.bh.sqlite"
cp /home/pi/bigtooth/blue_hydra/blue_hydra.db $bhdbfilename
rm /home/pi/bigtooth/blue_hydra/blue_hydra.db

gpsdbfilename="/home/pi/bigtooth2/db/GPS/$today.gps.sqlite"
cp /home/pi/bigtooth2/db/GPS/gps.sqlite $gpsdbfilename
rm /home/pi/bigtooth2/db/GPS/gps.sqlite

logfilename="/home/pi/bigtooth2/logs/$today.bhydra.log"
cp /home/pi/bigtooth/blue_hydra/blue_hydra.log $logfilename
rm /home/pi/bigtooth/blue_hydra/blue_hydra.log
