import sqlite3
import csv
import pickle
import yaml
from subprocess import call
from os import listdir
from os.path import isfile, join

piconf = {'name':'device',
            'rmtAddress':'pi@192.168.1.186'}

sql3conf = {'name':'sqlite3',
            'LOCALDB':'/home/pcgeller/btData',
            'REMOTEDB':'/home/pi/bigtooth2/db/'
            'DATAPATHS':['dbs','logs'],
            'PROJECT':'/home/pcgeller/bigtooth',
            'deviceconf':piconf,
            'header':['id','uuid','name','status','address','uap_lap','vendor','appearance','company', 'company_type','lmp_version', \
                'manufacturer','firmware','ibeacon_range','created_at','updated_at','last_seen']}
pgconf = {'name':'pg',
            'LOCALDB':'/home/pcgeller/btData',
            'DATAPATHS':['dbs','logs'],
            'PROJECT':'/home/pcgeller/bigtooth',
            'device':piconf,
            'header':['id','uuid','name','status','address','uap_lap','vendor','appearance','company', 'company_type','lmp_version', \
                'manufacturer','firmware','ibeacon_range','created_at','updated_at','last_seen']}

class ingestor:
    def __init__(self,config,db):
        with open(config, 'r') as f:
            config = yaml.load(f)
            keys, values = zip(*config.items())


        self.dbs = [db for db in listdir(conf['LOCALDB']) if isfile(join(conf['LOCALDB'], db))]


    def fetchdbs(self, conf):
        for PATH in DATAPATHS:
            call(['scp', '-r', remote + ':' + join(REMOTE,PATH), LOCAL ])


    def pkl(data, filename):
        with open(filename, 'wb') as f:
            pickle.dump(data,f,pickle.HIGHEST_PROTOCOL)
        print("Data pkled")
        return(data)

    def unpkl(filename):
        with open(filename, 'rb') as f:
            data = pickle.load(f)
        print("Data Unpkled")
        return(data)

    def dbstocsv(path=DBPATH, header = False, mkfiles = False):
        #DBPATH = './bigtooth/dbs'
        dbs = [db for db in listdir(path) if isfile(join(path, db))]
        completelist = []
        for db in dbs:
            print(db)
            conn = sqlite3.connect(join(path, db))
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
