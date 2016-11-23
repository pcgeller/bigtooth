from wrangle import *
import seaborn as sns
import matplotlib.pyplot as plt

def barplot(count):
    plot = sns.barplot(x = count.columns[0], y = count.columns[1], data = count)
    #plot.set_xticklabels(rotation = 45)
    return(plot)

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

def getelection():
    election = selectday(df)
    election = selecthour(election)
    election = selectmonth(election)
    return(election)

def getbigtooth():
    #Pick out weekdaytrips from my commute
    sub = selecthour(df,6,8)
    sub = selectweekdays(sub)
    #cleanCat(sub)
    return(sub)

#It took forever to figure this out.
df['created_at'].dt.hour
df['created_at'].dt.day

barplot(cntcol(df, 'address'))

sns.set(style='ticks')
x = df['created_at'].dt.day
y = df['created_at'].dt.hour

sns.jointplot(x,y, kind='hex')

#sns.factorplot(x=df['created_at'].dt.day, y = )

start_date = '20161108'
end_date = '20161110'
maskdate = (df['created_at'] > start_date) & (df['created_at'] <= end_date)
masktime = (df['created_at'].dt.hour > 15)
maskdate = (df['created_at'].dt.month == 11)
sub = df.loc[mask]

bt = getbigtooth()
g = sns.barplot(x=df.vendor.value_counts().index, y=df.vendor.value_counts())
g = sns.barplot(x=bt.address.value_counts().index, y=bt.address.value_counts())

#Count of unique UAPs
plot = sns.barplot(x='address', y='count', data = cntaddress)
plot.set_xticklabels(rotation=90)

hm = pd.pivot_table(bt,index='uap_lap',values='uap_lap', \
columns=bt['created_at'].dt.day,aggfunc=len)

g = sns.heatmap(hm, fmt='g')

pd.pivot_table(bt,index='uap_lap',values='name',columns=bt['created_at'].dt.day,aggfunc=len)

#build heatmap for uap_lap over each day
bt['day'] = bt['created_at'].dt.day
hm = pd.pivot_table(bt,index=['uap_lap'],values='uuid',columns='day',\
aggfunc=lambda x: len(x.dropna().unique()))
g = sns.heatmap(hm, fmt='g')

g.set_xticklabels(g.get_xticklabels(),rotation = 90)
g.set_yticklabels(g.get_yticklabels(),rotation=0)

bt['freq'] = bt.groupby('address')['address'].transform('count')
multi = bt[bt['freq'] > 2]
hm = pd.pivot_table(multi, index=['address','name','vendor'], values='uuid',\
    columns='date', aggfunc = len)
g = sns.heatmap(hm, fmt='g', cmap='RdBu_r')

sns.stripplot(x='vendor', y='strtime', data=bt, jitter = True)
bt['created_at'].dt.strftime('%H:%M')

bt['created_at'].dt.strftime('%D').sort_values()

bt['date'] = bt['created_at'].dt.strftime('%D')
