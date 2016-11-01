from subprocess import call
from os import listdir
from os.path import isfile, join
import sqlite3

"""
Save the database.  Load the database.
```shell
pg_dump bigtooth > bigtooth.pg
pg_dump -d bigtooth -f bigtooth.pg
\copy devices FROM '/home/pcgeller/bigtooth/sqlitedb.csv' DELIMITER ',' CSV;
```

##sqlite to CSV
```shell
sqlite3 /home/pcgeller/bigtooth/blue_hydra/blue_hydra.db
.mode csv
.out /home/pcgeller/bigtooth/sqlitedb.csv
select * from blue_hydra_devices;
.quit
```
"""

BPATH = '/home/pcgeller/workspace/bigtooth'

DBPATH = '/dbs/project'
collectionfiles = listdir('/home/pcgeller/workspace/bigtooth/dbs/project')

#Kludgy and fragile.  Rewrite to sqlite py module.
# for f in collectionfiles:
#     filepath = join(DBPATH, f)
#     outpath = join(DBPATH, 'csvdump', (f + '.csv'))
#     print('f:' + f)
#     print('filepath:' + filepath)
#     call(['sqlite3', filepath, 'csv'])
#     call(['.mode csv'])
#     call(['.out', outpath])
#     call(['select * from blue_hydra_devices;'])
#     call(['.quit'])
#

#PostGres isn't needed.
'''
Connect to each sqlite db and look for unique UUID.
Append to dictionary keys if it's new.
If it's been seen before append to dicionary value
'''
for f in collectionfiles:
     con = sqlite3.connect()
