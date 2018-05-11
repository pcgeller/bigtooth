#!/bin/bash
today=`date '+%Y_%m_%d__%H_%M'`;

echo $today

bhdbfilename="/home/pi/bigtooth/data/$today.bh.sqlite"
cp /home/pi/bigtooth/blue_hydra/blue_hydra.db $bhdbfilename
rm /home/pi/bigtooth/blue_hydra/blue_hydra.db

gpsdbfilename="/home/pi/bigtooth/data$today.gps.sqlite"
cp /home/pi/bigtooth/data/gps.sqlite $gpsdbfilename
rm /home/pi/bigtooth/data/gps.sqlite

logfilename="/home/pi/bigtooth/data/logs/$today.bhydra.log"
cp /home/pi/bigtooth/blue_hydra/blue_hydra.log $logfilename
rm /home/pi/bigtooth/blue_hydra/blue_hydra.log
