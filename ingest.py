from subprocess import call
from os import listdir
from os.path import isfile, join
import sqlite3

DBS = '/home/pcgeller/workspace/bigtooth/dbs/project'

def cmdDB(self, command):
    self.cursor.execute(command)
    self.connector.commit()

#Merge databases in a folder into a big database
def mergeDB(DBS = DBS):
    dbs = listdir(DBS)
    for db in dbs:
        conn = sqlite3.connect(db)
        c = conn.cursor()
        cmd = 'attach "{0}" as project'.format(db)

        cur.execute(cmd)
        conn.close()


#Open each database from a store-based collection.  (named storename)
#Create a python pickle for each dataset.  (one per store)

conn = sqlite3.connect(':memory:')
cur = conn.cursor()
cur.execute('CREATE TABLE test (id INTEGER)')
cur.execute('INSERT INTO test VALUES (2)')
conn.commit()

cur.execute('SELECT * FROM test')
results = cur.fetchall()
print(results)
conn.close()
