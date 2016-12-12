import sqlite3
import csv
import pickle
from subprocess import call
from os import listdir
from os.path import isfile, join
import pandas as pd



DBPATH = '/home/pcgeller/workspace/bigtooth/dbs'
DATAPATHS = ['dbs','logs']
PROJECT = '/home/pcgeller/bigtooth'
def fetchdbs(LOCAL, \
        remote = 'pi@192.168.1.186', \
        REMOTE = '/home/pi/bigtooth/', \
        DATAPATHS = DATAPATHS):
    for PATH in DATAPATHS:
        call(['scp', '-r', remote + ':' + join(REMOTE,PATH), LOCAL ])

header = ['id','uuid','name','status','address','uap_lap',\
'vendor','appearance','company', 'company_type','lmp_version','manufacturer',\
'firmware','ibeacon_range','created_at','updated_at','last_seen']
dbs = [db for db in listdir(DBPATH) if isfile(join(DBPATH, db))]

def pkl(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data,f,pickle.HIGHEST_PROTOCOL)

def unpkl(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return(data)

def dbstocsv(path=DBPATH, header = False, mkfiles = False):
    #DBPATH = './bigtooth/dbs'
    dbs = [db for db in listdir(DBPATH) if isfile(join(DBPATH, db))]
    completelist = []
    for db in dbs:
        print(db)
        conn = sqlite3.connect(join(DBPATH, db))
        c = conn.cursor()
        c.execute('SELECT id, uuid, name, status, address, uap_lap, vendor,\
        appearance, company, company_type, lmp_version, manufacturer, firmware,\
        ibeacon_range, created_at, updated_at, last_seen from blue_hydra_devices;')

        completelist.extend(c.fetchall())
        print(len(completelist))
        if mkfiles == True:
            savepath = join(PROJECT, 'csv', db + '.csv')
            with open(savepath, 'w') as f:
                writer = csv.writer(f)
                if header == True:
                    writer.writerow(['id','uuid','name','status','address','uap_lap',\
                    'vendor','appearance','company','company','company_type','lmp_version','manufacturer',\
                    'firmware','ibeacon_range','created_at','updated_at','last_seen'])
                writer.writerows(c)
        c.close()
        conn.close()
    return(completelist)
#### YAR HERE BE sqlite3 commands
'''
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
'''
#df = pd.read_csv('blue_hydra.db.2016-10-12_H08M10.csv', names=
 #header)
