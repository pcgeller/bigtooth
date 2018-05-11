#Ensure the device is running bigtooth.
#It ensures three things happen:
#1. All neccessary programs are started.
#  - hostapd
#  - wifi access point
#  - postgres
#  - blue_hydra
#  - gpsd
# 2. Track data.
#  - log rotatation
#  -
# 3. Serve data.
#  - The postgres database is queryable to a remote user.
import subprocess
import os.path
from time import strftime

class bigtoothSetup:
    def __init__(self):
        self.name = 'bigtooth Device'
        self.SCRIPTS = '/home/bigtooth2/scripts'
    def boot():
        subprocess.call(os.path.join(self.SCRIPTS,'startup.sh'))

class fileMover:
    #Move the blue hydra database and logs each time the rPi boots.
    def __init__(self):
        self.PATH = '/home/pcgeller/workspace/bigtooth/'
        self.FILES = {'db':'blue_hydra.db',
            'log':'blue_hydra/blue_hydra.log',
            'rssi':'blue_hydra/blue_hydra_rssi.log'}
        self.STORAGE = {'db':'dbs',
            'log':'logs',
            'rssi':'rssi'}
    def moveFiles():
        for k in files:
            filepath = os.path.join(PATH, files[k])
            storagepath = os.path.join(PATH, storage[k],\
            ''.join(['blue_hydra','.',k,'.',strftime("%Y-%m-%d_H%HM%M")]))
            if os.path.isfile(filepath) == True:
                print(files[k] + ':File exists, moving.')
                call(['mv', filepath, storagepath])
                print("File moved to" + storagepath)
                #Should add some exception handling.
            else:
                print(filepath,':Does not exist.')
                next
                
    def makefiles(): # for testing
        for k in files:
            filepath = os.path.join(PATH, files[k])
            call(['touch',filepath])
