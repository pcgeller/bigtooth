#!/bin/bash
today=`date '+%Y_%m_%d__%H'`;
dbfilename="/home/pi/bigtooth2/db/$today.sqlite.db"
echo $dbfilename;
cp /home/pi/bigtooth/blue_hydra/blue_hydra.db $dbfilename

logfilename="/home/pi/bigtooth2/logs/$today.bhydra.log"
echo $logfilename;
cp /home/pi/bigtooth/blue_hydra/blue_hydra.log $logfilename
