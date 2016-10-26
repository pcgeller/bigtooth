import sqlite3
import csv
from subprocess import call
from os import listdir
from os.path import isfile, join

DBPATH = './bigtooth/dbs'
DATAPATHS = ['dbs','logs']
def fetchdbs(remote = 'pi@192.168.1.186', \
REMOTE = '/home/pi/bigtooth/', \
LOCAL = '/home/pcgeller/bigtooth/',\
DATAPATHS = DATAPATHS):
    for PATH in DATAPATHS:
        call(['scp', '-r', remote + ':' + join(REMOTE,PATH), LOCAL ])


def joindbs(path=DBPATH, header = False):
    DBPATH = './bigtooth/dbs'
    dbs = [db for db in listdir(DBPATH) if isfile(join(DBPATH, db))]
    for db in dbs:
        conn = sqlite3.connect(db)
        c = conn.cursor()
        c.execute('SELECT id, uuid, name, status, address, uap_lap, vendor,\
        appearance, company, company_type, lmp_version, manufacturer, firmware,\
        ibeacon_range, created_at, updated_at, last_seen from blue_hydra_devices;')
        with open(db + '.csv','w') as f:
            writer = csv.writer(f)
            if header == True:
                writer.writerow(['id','uuid','name','status','address','uap_lap',
                'vendor','appearance','company','company','company_type','lmp_version','manufacturer'\
                'firmware','ibeacon_range','created_at','updated_at','last_seen'])
            writer.writerows(c)
        c.close()
        conn.close()




#### YAR HERE BE sqlite3 commands
.headers on
.mode csv
.output data.csv

SELECT id,
uuid,
name,
status,
address,
uap_lap,
vendor,
appearance,
company,
company_type,
lmp_version,
manufacturer,
firmware,
ibeacon_range,
created_at,
updated_at,
last_seen from blue_hydra_devices;
