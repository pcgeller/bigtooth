#Create a bigtooth device.  Connect over wifi/ssh.
#Make blue hydra, gpsd, database available.
import subprocess

class device:
    def __init__(self):
        self.name='bigtooth'
        self.localaddress='192.168.1.186'
        self.user='pi'
        self.remoteAddress='192.168.42.1'
        self.paths=['/home/pi/bigtooth2/db/*']
        self.localPATH='/home/pcgeller/scratch'
        self.remote=self.user,'@',self.remoteAddress,':',self.paths

    def sync(self):
        remote=self.user,'@',self.remoteAddress,':',self.paths
        #remote='pi@192.168.1.186:/home/pi/bigtooth2/db/*'
        #subprocess.Popen(['scp', '-r',
        #'pi@192.168.1.186:/home/pi/bigtooth2/db',
        #'/home/pcgeller/scratch']).wait()
        subprocess.Popen(['scp', '-r', str(remote), str(localPATH)]).wait()
    def cleanup(self):
        subprocess.Popen['rm', '']
    def resync(self):
        subprocess.Popen(['rsync', str(remote), str(localPath)]).wait()

bt = device()
bt.sync()
import gps3
import subprocess
#Setup gpsd
subprocess.call(['sudo', 'gpsd', '/dev/ttyUSB0', \
    '-F', '/var/run/gpsd.sock'])
#Ensure gpsd is running correction
while True:
    try:
        print('True')
