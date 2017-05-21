#Create a bigtooth device.  Connect over wifi/ssh.
#Make blue hydra, gpsd, database available.

class device:
    def __init__(self):
        self.name='bigtooth'
        self.loacalddress='192.168.1.186'
        self.user='pi'
        self.remoteAddress='192.168.42.1'
    def connect(hostname):
        ssh = subprocess.Popen(["ssh", "%s" % remote],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
                       result = ssh.stdout.readlines()
                       if result == []:
                           error = ssh.stderr.readlines()
                           print >>sys.stderr, "ERROR: %s" % error
                       else:
                           print result


import subprocess
NAME='bigtooth'
remote='192.168.42.1'
warg=['ssh','pi@192.168.42.1']
subprocess.Popen(['ssh', 'pi@%h' % remote])
subprocess.Popen(warg,
    stdin = subprocess.PIPE,
    stdout= subprocess.PIPE,
    )

import gps3
import subprocess
#Setup gpsd
subprocess.call(['sudo', 'gpsd', '/dev/ttyUSB0', \
    '-F', '/var/run/gpsd.sock'])
#Ensure gpsd is running correction
while True:
    try:
        print('True')
