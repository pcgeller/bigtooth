from subprocess import call
import os.path
from time import strftime

PATH = '/home/pcgeller/workspace/bigtooth/'

files = {'db':'blue_hydra.db',
        'log':'blue_hydra/blue_hydra.log',
        'rssi':'blue_hydra/blue_hydra_rssi.log'}

storage = {'db':'dbs',
        'log':'logs',
        'rssi':'rssi'}

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

def makefiles():
    for k in files:
        filepath = os.path.join(PATH, files[k])
        call(['touch',filepath])
