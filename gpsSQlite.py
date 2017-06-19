#script to configure and run gpsd server then start
#logging gps data into a postgres database.

import serial
import datetime
import time
import os
import sys
import sqlite3
import subprocess
#import gps3
#import dbconnection
#Setup gpsd
subprocess.call(['sudo', 'gpsd', '/dev/ttyUSB0', \
    '-F', '/var/run/gpsd.sock'])
try:
    ser = serial.Serial("/dev/ttyUSB0")    # baudrate=9600)
except:
    print("Error opening serial port.")
    sys.exit(1)




try:
    conn = sqlite3.connect('/home/pi/bigtooth2/db/GPS/btGPS.sqlite')
    cur = conn.cursor()
except:
    print ("\n_________CONNECTION FAILURE_________\n")

'''
cur.execute('CREATE TABLE gps(\
  n_lat int,\
  w_long int,\
  date_time int,\
  time int,\
  date int,\
  PRIMARY KEY(date_time));')
resp = ""
''''

resp = ''

try:
    while True:
        while (ser.inWaiting() > 0):
            resp = ser.readline()
            resp = str(resp)
            print(resp)
            if '$GPRMC' in resp:
                print(resp)
                data = resp.split(',')
                if data[2] == 'A':
                    dom = data[9][0:2]
                    month = data[9][2:4]
                    year = int(data[9][4:6]) + 2000
                    date = "%d-%s-%s" % (year, month, dom)
                    hour = data[1][0:2]
                    min = data[1][2:4]
                    sec = data[1][4:6]
                    t = "%s:%s:%s-0000" % (hour, min, sec)
                    dateTime = "%s %s" % (date, t)
                    north = data[3]
                    west = data[5]
                    sql = "insert into gps(n_lat, w_long, date_time, time, date) values (%s, %s, '%s', '%s', '%s');" % (north, west, dateTime, t, date)
                    print(sql)
                    cur.execute(sql)
                    print("Rows inserted: %s" % cur.rowcount)
                    conn.commit()
                    time.sleep(0.1)
                    resp = ""
except InternalError as e:
    print(e)
    conn.rollback()
except Exception as e:
    print(sys.exc_info()[0])

finally:
    if conn:
        conn.close()
    ser.close()
