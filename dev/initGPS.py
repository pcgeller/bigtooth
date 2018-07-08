#gps runner
import gps3

import subprocess
#Setup gpsd
subprocess.call(['sudo', 'gpsd', '/dev/ttyUSB0', '-F', '/var/run/gpsd.sock'])

#Ensure gpsd is running correction
while True:
    try:
        print('True')

# Listen on port 2947 (gpsd) of localhost
session = gps3.gps3("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
def ruexngps():
    while True:
        try:
          report = session.next()
        # Wait for a 'TPV' report and display the current time
        # To see all report data, uncomment the line below
        # print report
            if report['class'] == 'TPV':
                if hasattr(report, 'time'):
                    print report.time
    			if hasattr(report, 'speed'):
    				print report.speed * gps.MPS_TO_KPH
        except KeyError:
        pass
        except KeyboardInterrupt:
        quit()
        except StopIteration:
        session = None
        print "GPSD has terminated"
