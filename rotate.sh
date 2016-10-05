#!/bin/bash
today=`date '+%Y_%m_%d__%H'`;
dbfilename="/home/pcgeller/bigtooth/db/$today.pgsql.csv"
echo $dbfilename;

logfilename="home/pcgeller/bigtooth/logs/$today.bhydra.log"
echo $logfilename;
