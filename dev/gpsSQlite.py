#script to configure and run gpsd server then start
#logging gps data into a postgres database.

import serial
import datetime
import time
import os
import sys
import sqlite3
import subprocess

sys.path.insert(0,'/home/pi/bigtooth/dev/statusLights')
import statusLightClass as sl

serialPort = "/dev/ttyUSB0"
gpsDatabase = "/opt/data/gps/current/gps.sqlite"
databaseSchema = "CREATE TABLE gps(n_lat integer,w_long integer,\
        date_time integer,obs_time integer,obs_date int);"

def startGps():
    subprocess.call(['sudo', 'gpsd', '/dev/ttyUSB0', \
        '-F', '/var/run/gpsd.sock'])
    try:
        ser = serial.Serial("/dev/ttyUSB0")
    except:
        print("Error opening serial port.")
        sys.exit(1)
    finally:
        ser.close()

def makeTable(schema=("CREATE TABLE gps(n_lat integer,w_long integer,\
        date_time integer,obs_time integer,obs_date int);"),
        DB=gpsDatabase):
    for i in range(0,10): #set number of retrys
        try:
            conn = sqlite3.connect(DB)
            c = conn.cursor()
            c.execute(schema)
        except sqlite3.OperationalError as e:
            print("SQLITE3 ERROR:" + str(e))
            os.remove(DB)
            print("Database removed, retrying")
        finally:
            conn.close()

def logGps():
    try:
        conn = sqlite3.connect('/opt/data/gps/current/gps.sqlite')
        cur = conn.cursor()
    except:
        print ("\nError opening database connection.\n")
        sys.exit(1)
    try:
        ser = serial.Serial("/dev/ttyUSB0")
    except:
        print("Error opening serial port.")
        sys.exit(1)
    #init empty response
    light = sl.statusLight("bigtooth", 26)
    light2 = sl.statusLight("serialWait", 21)
    response = ''
    try:
        while True:
            while (ser.inWaiting() > 0):
                response = ser.readline()
                response = str(response)
                light2.turnOn()
                print(response)
                light2.turnOff()
                if '$GPRMC' in response:
                    print(response)
                    data = response.split(',')
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
                        light.turnOn()
                        print("Rows inserted: %s" % cur.rowcount)
                        conn.commit()
                        light.turnOff()
                        time.sleep(0.3)
                        response = ""
    except Exception as e:
        print(sys.exc_info()[0])
    finally:
        if conn:
            conn.close()
        ser.close()

if __name__ == '__main__':
    startGps()
    makeTable()
    logGps()
