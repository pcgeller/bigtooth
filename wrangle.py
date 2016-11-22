from ingest import *
import numpy as np

data = dbstocsv()
df = pd.DataFrame(data, columns = header)

#Clean up time columns.  Make it a nice dataframe object.
timecols  = ['created_at', 'updated_at']
def cleanDT(timecols = timecols):
    for col in timecols:
        time = pd.DatetimeIndex(df[col])
        time = time.tz_localize('UTC')
        time = time.tz_convert('US/Eastern')
        df[col] = time
        df['epoch_' + col] = time.astype(np.int64) // 10**9

cleanDT()
df['duration'] = abs(df['epoch_created_at'] - df['last_seen'])

catcols = ['uuid','name','status','address','uap_lap',\
'vendor','appearance','company', 'company_type','lmp_version','manufacturer',\
'firmware']
def cleanCat(df,catcols = catcols):
    for col in catcols:
        df[col] = df[col].astype('category')

def cntcol(df, colname):
    count = df.groupby([colname]).size().reset_index().rename(columns={0:'count'})
    count = count.sort_values('count')
    return(count)

cntuuid = cntcol(df, 'uuid')
cntaddress = cntcol(df, 'address')
cntvendor = cntcol(df, 'vendor')



#Make unique list of uuid
unquuid = df.uuid.unique()
x = unquuid[1]
tdict = {'uuid':x}
df[df['uuid'].str.contains(x)]
#Clean up any null values
df.fillna("MISSING")

#For each uuid select the date created and store it in a dictionary
tdict = {'address':'timecreated'}
for u in unquuid:
    tstamps = list(df.created_at[df['address'].str.contains(u)].values)
    tdict[u] = tstamps

cntaddress.sort_values('count').tail(1).address.values

#This is my stereo system.
df[df['address'].str.contains('00:08:E0:4C:2F:85')]
