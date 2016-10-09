#!/bin/bash
today=`date '+%Y_%m_%d__%H'`;
dbfilename="/home/pcgeller/bigtooth/db/$today.sqlite.db"
echo $dbfilename;
cp /home/pcgeller/bigtooth/blue_hydra/blue_hydra.db $dbfilename

logfilename="/home/pcgeller/bigtooth/logs/$today.bhydra.log"
echo $logfilename;
cp /home/pcgeller/bigtooth/blue_hydra/blue_hydra.log $logfilename
