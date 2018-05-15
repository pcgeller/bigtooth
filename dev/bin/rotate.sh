#!/bin/bash
today=`date '+%Y_%m_%d__%H_%M'`;

echo $today
#arg $1 is passed by the calling function startup.sh
#default /opt

bhdbfilename="$1/data/bh/$today.bh.sqlite"
cp $1/data/bh/current/blue_hydra.db $bhdbfilename
rm $1/data/bh/current/blue_hydra.db

gpsdbfilename="$1/data/gps/$today.gps.sqlite"
cp $1/data/gps/current/gps.sqlite $gpsdbfilename
rm $1/data/gps/current/gps.sqlite
