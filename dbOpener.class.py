import sqlite3 as sql

class dbOpener:
    def __init__(self, config):
        with open(config, 'r') as f:
            config = yaml.load(f)
            keys, values = zip(*config.items())

    def dbQueue(config, remote = TRUE):
        if remote = TRUE:
            DBPATH = config['REMOTEDB']


    def open(config, remote=TRUE):
        conn = sql.connect(config[''])
