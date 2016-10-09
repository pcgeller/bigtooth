## Set up PostgreSQL database
Install PostgreSQL
```shell
sudo apt-get install postgresql
```

```shell
sudo -u postgres -i
psql
```

```shell
sudo psql
```
Which opens a psql prompt.  Now create the database.
```sql
CREATE DATABASE bigtooth;
```
Connect to the database.  Similar to mysql use.
```shell
\connect bigtooth
```
Create the devices table.  This is the main table for tracking all of the devices seen.  It's a complete conversion of the sqlite3 database from blue_hydra.
```sql
CREATE TABLE devices (
id SERIAL NOT NULL PRIMARY KEY,
uuid VARCHAR(50),
name VARCHAR(50),
status VARCHAR(50),
address VARCHAR(50),
uap_lap VARCHAR(50),
vendor TEXT,
appearance VARCHAR(50),
company VARCHAR(50),
company_type VARCHAR(50),
lmp_version VARCHAR(50),
manufacturer VARCHAR(50),
firmware VARCHAR(50),
classic_mode BOOLEAN DEFAULT FALSE,
classic_service_uuids TEXT,
classic_channels TEXT,
classic_major_class VARCHAR(50),
classic_minor_class VARCHAR(50),
classic_features TEXT,
classic_features_bitmap TEXT,
le_mode BOOLEAN DEFAULT FALSE,
le_service_uuids TEXT,
le_address_type VARCHAR(50),
le_random_address_type VARCHAR(50),
le_company_data VARCHAR(50),
le_company_uuid VARCHAR(50),
le_proximity_uuid VARCHAR(50),
le_major_num VARCHAR(50),
le_minor_num VARCHAR(50),
le_flags TEXT,
le_rssi TEXT,
le_tx_power TEXT,
le_features TEXT,
le_features_bitmap TEXT,
ibeacon_range VARCHAR(50),
created_at TIMESTAMP WITHOUT TIME ZONE,
updated_at TIMESTAMP WITHOUT TIME ZONE,
last_seen INTEGER);
```
##Establish Permissions
Grant permission to 'regular' non postgres user. Eg; pcgeller.
```sql
ALTER USER postgres password 'pg';
CREATE USER pcgeller createdb createuser password 'pcgeller';
create database pcgeller owner pcgeller;
\q
```
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
