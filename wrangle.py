from ingest import *

data = dbstocsv()
df = pd.DataFrame(data, columns = header)
unquuid = df.uuid.unique()

#Clean up time columns.  Make it a nice dataframe object.
timecols  = ['created_at', 'updated_at']
def datetime(timecols = timecols):
    for col in timecols:
        df[col] = pd.to_datetime(df[col])

times = pd.DatetimeIndex(df.created_at)
grouped = df.groupby([times.hour, times.minute])

nfp = pd.read_csv("NFP.csv", parse_dates=[0], infer_datetime_format=True)
temp = pd.DatetimeIndex(nfp['DateTime'])
nfp['Date'] = temp.date
nfp['Time'] = temp.time
del nfp['DateTime']

print(nfp)

def getdates(col,start,end):
    col = 'created_at'
    start = '2016-10-20'
    end = '2016-10-24'
    mask = (df[col] > start) & (df[col] <= end)
    print(df.loc[mask])

def cntcol(colname):
    count = df.groupby([colname]).size().reset_index().rename(columns={0:'count'})
    count = count.sort_values('count')
    return(count)




cntuuid = cntcol('uuid')
cntaddress = cntcol('address')
cntvendor = cntcol('vendor')


x = unquuid[1]
tdict = {'uuid':x}
df.fillna("MISSING")
df[df['uuid'].str.contains(x)]
#df.vendor[df['company'].str.contains("G")].values
#df['company'].notnull()

#df = pd.read_csv('blue_hydra.db.2016-10-12_H08M10.csv', names=
 #header)

#Make unique list of uuid
unquuid = df.uuid.unique()

#Clean up any null values

#For each uuid select the date created and store it in a dictionary
tdict = {'uuid':'timecreated'}
for u in unquuid:
    tstamps = list(df.created_at[df['address'].str.contains(u)].values)
    tdict[u] = tstamps

freq = cntaddress.sort_values('count')


cntaddress.sort_values('count').tail(1).address.values
#Has
df[df['address'].str.contains('00:08:E0:4C:2F:85')]
