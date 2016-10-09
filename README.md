# bigtooth

bigtooth is a project that taps into the unseen world around us.  Bluetooth signals are only one of the many signal types that are 
(almost) constantly permiating the space around us.  This project takes a small slice of that space - 20 days of data collected over the
same geographic route (a road) during roughly the same time period.  The goal is to see how often the same unique individuals are seen 
along the route (and possibly how long they travel together).  

The project consists of a Raspberry Pi 3 loaded with blue_hydra.  It uses a SENA UD100 as the bluetooth adapter, the rpi3 onboard wifi,
an Ubertooth dongle (not required), and the scripts in this repository.  The scripts convert the blue_hydra sqlite3 output into
a PostgreSQL db.  They then perform analysis on the db to determine if a device has been seen before.  It does this by creating a python
dictionary that stores the device observation timestamps.
