from ingest import *

data = dbstocsv()

df = pd.DataFrame(data, columns = header)
counts = df.groupby(['uuid']).size().reset_index().rename(columns={0:'count'})
unquuid = df.uuid.unique()

x = unquuid[1]
tdict = {'uuid':x}

df[df['uuid'].str.contains(x)]
df.vendor[df['company'].str.contains("G")].values
df['company'].notnull()

#df = pd.read_csv('blue_hydra.db.2016-10-12_H08M10.csv', names=
 #header)

 #Make unique list of uuid
 unquuid = df.uuid.unique()

 #Clean up any null values
 df.fillna("MISSING")

 #For each uuid select the date created and store it in a dictionary
tdict = {'uuid':'timecreated'}
for u in unquuid:
    tstamps = list(df.created_at[df['uuid'].str.contains(u)].values)
    tdict[u] = tstamps
