#script to configure and run gpsd server then start
#logging gps data into a postgres database.

import serial
import datetime
import time
import os
import sys
import psycopg2
import subprocess
#import gps3
#import dbconnection
import sqlite3
#Setup gpsd

subprocess.call(['sudo', 'gpsd', '/dev/ttyUSB0', \
    '-F', '/var/run/gpsd.sock'])
try:
    ser = serial.Serial("/dev/ttyUSB0")    # baudrate=9600)
except:
    print("Error opening serial port.")
    sys.exit(1)



def makeTable(schema=("CREATE TABLE gps(n_lat integer,w_long integer,date_time integer,obs_time integer,obs_date int);"),
        DB="/home/pcgeller/bigtooth2/db/GPS/gps.db"):
# End default args
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(schema)
    conn.close()


try:
    conn = psycopg2.connect(
        host='localhost',
        port="5432",
        database="bigtooth",
        user='bigtooth',
        password='bigtooth')
    cur = conn.cursor()
except:
    print ("\n_________CONNECTION FAILURE_________\n")

resp = ""

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
                    sql = "insert into gps(n_lat, w_long, date_time, obs_time, obs_date) values (%s, %s, '%s', '%s', '%s');" % (north, west, dateTime, t, date)
                    print(sql)
                    cur.execute(sql)
                    print("Rows inserted: %s" % cur.rowcount)
                    conn.commit()
                    time.sleep(0.1)
                    resp = ""

#except InternalError as e:
#    print(e)
#    conn.rollback()
except Exception as e:
    print(sys.exc_info()[0])

finally:
    if conn:
        conn.close()
    ser.close()
