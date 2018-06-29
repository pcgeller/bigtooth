import sqlite3 as sql
import yaml

#open both gps and bh database
#compare time stamps and for those that match add the gps dataa
#load into postgres
#result is clean postgres database with bh and gps added together

CONFIG = './'

import os
dir = os.path.dirname(__file__)
filename = os.path.join(dir, '/relative/path/to/file/you/want')

class dbOpener:
    def __init__(self, config=CONFIG):
        with open(CONFIG, 'r') as f:
            config = yaml.load(f)

    def open(local = config['LOCALDB'], dbs = config['DBs']):
        dbs = [db for db in listdir(path) if isfile(join(path, db))]
        completelist = []
        for db in dbs:
            print(db)
            conn = sqlite3.connect(join(path, db))
            c = conn.cursor()
            c.execute('SELECT id, uuid, name, status, address, uap_lap, vendor,\
