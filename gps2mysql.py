import serial
import time
import datetime
import os
import sys
import MySQLdb as mdb

try:
   serial = serial.Serial("/dev/ttyAMA0", baudrate=9600)
   time.sleep(1)
   con = mdb.connect('localhost', 'YourDBUser', 'YourDBPasswd', 'YourDB');
   cur = con.cursor()

except:
   print("Error opening serial port.")
   sys.exit(1)

resp = ""

try:
   while True:
       while (serial.inWaiting() > 0):
           resp += serial.read()
           if "\r\n" in resp:
               if "$GPRMC" in resp:
                   data = resp.split(',')
                       if data[2] == 'A':
                           dom = data[9][0:2]
                           month = data[9][2:4]
                           year = int(data[9][4:6]) + 2000
                           date = "%d-%s-%s" % (year, month, dom)
                           hour = data[1][0:2]
                           min = data[1][2:4]
                           sec = data[1][4:6]
                           t = "%s:%s:%s" % (hour, min, sec)
                           dateTime = "%s %s" % (date, t)
                           north = data[3]
                           west = data[5]
                           sql = "insert into gps(n_lat, w_long, date_time) values(%s, %s, %s)" % (north, west, t)
                           print sql
                           cur.execute(sql)
                           print "Rows inserted: %s" % cur.rowcount
                           con.commit()
                           time.sleep(0.5)
                           resp = ""
except:
   print sys.exc_info()[0]

finally:
   if con:
       con.close()
   serial.close()
