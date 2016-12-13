from ingest import *
import numpy as np
from datetime import date, datetime, timedelta
import datetime

data = dbstocsv()
#pkl(data, '/home/pcgeller/workspace/bigtooth/data/alldata.pkl')
#data = unpkl('/home/pcgeller/workspace/bigtooth/data/alldata.pkl')
df = pd.DataFrame(data, columns = header)
print("Data Unpkled")

#Clean up time columns.  Make it a nice dataframe object.
timecols  = ['created_at', 'updated_at']
def cleanDT(df = df, timecols = timecols):
    print("Cleaning datetimegroups.")
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
'firmware','pdate']
def cleanCat(df,catcols = catcols):
    print('Initializing catgorical variables.')
    #df['name'].cat.add_categories('Undetected')
    df['name'].fillna('Undetected', inplace = True)
    for col in catcols:
        df[col] = df[col].astype('category')
    #df['name'].cat.add_categories('Undetected')
    #df['name'].fillna('Undetected', inplace = True)
    #return(df)
    #multi.name.fillna('Undetected', inplace = True)


def cntcol(df, colname):
    count = df.groupby([colname]).size().reset_index().rename(columns={0:'count'})
    count = count.sort_values('count')
    return(count)

#uses UTCF so time is + 4 for EDT and + 5 for EST
def selecthour(df, starthour = 12, endhour = 19, col ='created_at'):
    sub = df[np.logical_and(df[col].dt.hour >= starthour, df[col].dt.hour <= endhour)]
    return(sub)

def selectday(df, startday = 8, endday = 8, col ='created_at'):
    sub = df[np.logical_and(df[col].dt.day >= startday, df[col].dt.day <= endday)]
    return(sub)

def selectmonth(df, startmonth = 11, endmonth = 11, col ='created_at'):
    sub = df[np.logical_and(df[col].dt.month >= startmonth, df[col].dt.month <= endmonth)]
    return(sub)

def selectweekdays(df, startday = 0, endday = 4, col = 'created_at'):
    sub = df[np.logical_and(df[col].dt.weekday >= startday, df[col].dt.weekday <= endday)]
    return(sub)

#def selectminutes(df, startmin = )

#Build address:name dictionary to resolve undected names
def mknamedict(df):
    adict = {'address':'name'}
    for index, row in df.iterrows():
        addy = row['address']
        name = row['name']
        if addy in adict:
            if adict[addy] == "Undetected" and name != 'Undetected':
                adict[addy] = name
                next
            else:
                next
        else:
            adict[addy] = name
    return(adict)

def getelection():
    election = selectday(df)
    election = selecthour(election)
    election = selectmonth(election)
    return(election)

def getbigtooth():
    #Pick out weekdaytrips from my commute
    print('Subsetting to bigtooth data')
    sub = selecthour(df,6,8)
    sub = selectweekdays(sub)
    #cleanCat(sub)
    #create some extra variables.
    #sub['created_at'].dt.strftime('%H:%M')
    #sub['created_at'].dt.strftime('%D').sort_values()
    sub['date'] = pd.DatetimeIndex(sub['created_at'].dt.date)
    sub['pdate'] = sub['created_at'].dt.strftime('%D')
    sub['ptime'] = sub['created_at'].dt.strftime('%H:%M')
    sub['freq'] = sub.groupby('address')['address'].transform('count')
    sub['day'] = sub['created_at'].dt.day
    sub = sub.reset_index(drop=True)
    return(sub)

def getstationarycollection():
    print('Selecting stationary device data')
    sub = selecthour(df, 7, 8)
    sub = select(minutes)
    sub = selectweekdays(sub)

def perdelta(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta

def rmstationarydev(df, sta):
    stationaryaddy = sta['address'].unique()
    addy = df['address'].unique()
    i = 0
    for a in stationaryaddy:
        #print(i)
        #print(a)
        if a in addy:
            df = df[df.address != a]
            #print("Stationary address record: " + a + " dropped from collection.")
            i += 1
        else:
            #Prob should fix unhandled error
            print("XXXXXXX")
            print("Address found in stationary collection does not exist in \
            analysis collection")
            next
    return(df)

#Determine first collection for each day for establishing time
def firsttstamp(df, datecol = 'date', times = 'created_at'):
    dates = df[datecol].unique()
    print(dates)
    dates = list(dates)
    df['firstts'] = pd.NaT
    #df['firstts'] = pd.DatetimeIndex(df['firstts']).tz_localize("US/Eastern")
    df['firstts'] = df['firstts'].dt.tz_localize('US/Eastern')
    #df['firstts'] = df['firstts'].tz_convert('US/Eastern')
    for d in dates:
        sub = df[df[datecol] == d]
        first = sub[times].min()
        #first = first.tz_convert("UTC")
        print(first)
        df.set_value(df[datecol] == d, 'firstts', first)
    epochts = df['firstts']
    df['firstepoch'] = epochts.astype(np.int64) // 10**9
    df['tsincefirst'] = (df.created_at - df.firstts).astype('timedelta64[s]')
    return(df)

'''
datecol = 'date'
times = 'created_at'
d = dates[1]
df['firstts'].dt.tz_localize('UTC')
bt = firsttstamp(df)

bt.ix[bt['tsincefirst'] > 80000,['created_at', 'firstts','tsincefirst','date']]
df.ix[df['tsincefirst'] > 80000,['created_at', 'firstts','tsincefirst','date']]
'''

#GET PROJECT DATA
bt = getbigtooth()

#Make sure columns are cat and add extra categories
cleanCat(bt)
adict = mknamedict(bt)
bt['namegen'] = bt['address'].map(adict)
#bt = firsttstamp(bt)

len(set(adict.keys()))
len(adict.keys())

#df of only frequently observed addresses
multi = bt[bt['freq'] > 4]
multi = multi.sort_values(by='freq')
#multi.name.cat.add_categories('Undetected')


#cntuuid = cntcol(df, 'uuid')
#cntaddress = cntcol(df, 'address')
#cntvendor = cntcol(df, 'vendor')

#Make unique list of uuid
unquuid = df.uuid.unique()
x = unquuid[1]
tdict = {'uuid':x}
df[df['uuid'].str.contains(x)]
#Clean up any null values
df.fillna("MISSING")

#For each uuid select the date created and store it in a dictionary
def mktdict(unquuid = unquuid):
    print("Making tstamp dictionary")
    tdict = {'address':'timecreated'}
    for u in unquuid:
        tstamps = list(df.created_at[df['address'].str.contains(u)].values)
        tdict[u] = tstamps
    return(tdict)

def mktdict2(df):
    print("Making tstamp2 dictionary")
    tdict = {'address':'timecreated'}
    for a in df['address'].unique():
        print(a)
        tstamps = list(df.created_at[df['address'].str.contains(a)].values)
        tdict[a] = tstamps
    return(tdict)

tdict = mktdict2(bt)

tdict['B0:34:95:51:D7:22']

#cntaddress.sort_values('count').tail(1).address.values

#This is my stereo system.
df[df['address'].str.contains('00:08:E0:4C:2F:85')]

#build date range
"""
startdate = bt['created_at'].dt.date.min()
enddate = bt['created_at'].dt.date.max()
for result in perdelta(startdate, enddate, timedelta(days=1)):
    print(result)
    """

#build time range
"""start = bt['created_at'].dt.time.min()
end = bt['created_at'].dt.time.max()
for result in perdelta(start, end, timedelta(minutes=1)):
    print(result)
"""
"""
s = datetime.combine(startdate, start)
e = datetime.combine(enddate, end)
n = 180

starttime = start
endtime = end

def minuterange(startdate, starttime, duration, interval):
    result = []
    i = 0
    print(i)
    s = datetime.combine(startdate, starttime)
    print(s)
    while i <= duration:
        s = s + timedelta(minutes=1)
        print(s.ptime())
        i += 1

#minuterange(startdate,starttime,180)
"""
