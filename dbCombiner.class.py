import sqlite3 as sql
import yaml
import psycopg2

#open both gps and bh database
#compare time stamps and for those that match add the gps dataa
#load into postgres
#result is clean postgres database with bh and gps added togethe

import os
dir = os.path.dirname(__file__)
filename = os.path.join(dir, '/relative/path/to/file/you/want')

class dbOpener:
    def __init__(self, config):
        self.listOfSignals = []
        self.listOfDatabases = []
        with open(config, 'r') as f:
            config = yaml.load(f)
        for signal in config['signals']:
            self.listOfSignals.append(signal)
            listdir(signal['path'])


    def open(local = config['LOCALDB'], dbs = config['DBs']):

        completelist = []
        for db in dbs:
            print(db)
            conn = sqlite3.connect(join(path, db))
            c = conn.cursor()
            c.execute('SELECT id, uuid, name, status, address, uap_lap, vendor,
            appearance, company, company_type, lmp_version, manufacturer, firmware,
            ibeacon_range, created_at, updated_at, last_seen from blue_hydra_devices;')


if __name__ == '__main__':
    ingestConfig = '/home/pcgeller/bigtooth/conf/ingestConfig.yml'
    zipper = dbOpener(ingestConfig)
