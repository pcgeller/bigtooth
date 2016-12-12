from wrangle import *
import seaborn as sns
sns.set(rc={'figure.facecolor':'lightgray'})
import matplotlib.pyplot as plt

pd.set_option('display.width', pd.util.terminal.get_terminal_size()[0])
pd.set_option('display.max_columns', None)


#def barplot(count):
    #plot = sns.barplot(x = count.columns[0], y = count.columns[1], data = count)
    #plot.set_xticklabels(rotation = 45)
    #return(plot)

#Try a hexplot
sns.set(style='ticks')
x = df['created_at'].dt.day
y = df['created_at'].dt.hour
g = sns.jointplot(x,y, kind='hex')



#Show overall distribution of vendor and address
g = sns.barplot(x=bt.vendor.value_counts().index, y=bt.vendor.value_counts(), order=bt.vendor.value_counts().index)
g = sns.barplot(x=bt.address.value_counts().index, y=bt.address.value_counts())
g = sns.barplot(x=bt.address.value_counts().index, y=bt.address.value_counts(), order=bt.address.value_counts().index[::-1])
g.get_xaxis().set_visible(False)
g.set_title("Number of Days a Device as Seen")
g.set_ylabel('Count of Address')

#build heatmap for uap_lap over each day
hm = pd.pivot_table(bt,index='uap_lap',values='uap_lap', \
columns=bt['created_at'].dt.day,aggfunc=len)
g = sns.heatmap(hm, fmt='g')

pd.pivot_table(bt,index='uap_lap',values='name',columns=bt['created_at'].dt.day,aggfunc=len)
hm = pd.pivot_table(bt,index=['uap_lap'],values='uuid',columns='day',\
aggfunc=lambda x: len(x.dropna().unique()))
g = sns.heatmap(hm, fmt='g')

g.set_xticklabels(g.get_xticklabels(),rotation = 90)
g.set_yticklabels(g.get_yticklabels(),rotation=0)

#Violin plot of times by day
g = sns.violinplot(x=bt['date'], y = bt['tsincefirst'])

#heatmap of when a device is observed over ptime
multi = bt[bt['freq'] > 5]
multi.vendor.cat.remove_unused_categories()
multi.address.cat.remove_unused_categories()
multi = multi.sort_values(by='freq')
multi.name.fillna('Undetected', inplace = True)

hm = pd.pivot_table(multi, index=[multi.address.cat.remove_unused_categories()], values='uuid',\
    columns='pdate', aggfunc = len)

hm = pd.pivot_table(multi, index='namegen', values='uuid',\
    columns='pdate', aggfunc = len)

'''Using the name column in the code below can cause double counting of
unique addresses.  This happens because an address can be recorded with
a name and without one.  If sniffing captures a device both ways then
both will be counted as unique device.  The vendor column doesn't have the
same problem.
'''
hm = pd.pivot_table(multi, index = 'pdate', values = 'uuid', \
    columns = ['address', 'vendor'], aggfunc = len)

hm.size
hm.shape

sns.set_context('talk')
plt.figure(figsize=(8,6))
ax = plt.axes()
g = sns.heatmap(hm, fmt='g', cmap='RdBu_r', cbar=False, \
    linewidths = 1, linecolor = 'gray', vmin=0, vmax=1, \
    square=True)
g = sns.heatmap(hm, fmt='g', cmap='RdBu_r', cbar=False, vmin=0, vmax=1)
g.set_title('Observation of Devices Over Time (freq > 5)')
g.set_yticklabels(g.get_yticklabels(),rotation=0)
g.set_xticklabels(g.get_xticklabels(),rotation = 90)

#dot plot of vendors
sns.stripplot(x='vendor', y='strtime', data=bt, jitter = True)

sns.stripplot(x='pdate', y='ptime', data = bt, jitter = True)

sns.violinplot(x='pdate', y='ptime', data = bt)

ax = sns.stripplot(x=bt['created_at'])
ax = sns.stripplot(x=bt['pdate'], y = bt['created_at'].dt.time)

#build dict of counts
counts = dict()
for i in bt['vendor']:
    counts[i] = counts.get(i,0)+1

#How to subset by masking
start_date = '20161108'
end_date = '20161110'
maskdate = (df['created_at'] > start_date) & (df['created_at'] <= end_date)
masktime = (df['created_at'].dt.hour > 15)
maskdate = (df['created_at'].dt.month == 11)
sub = df.loc[mask]

sns.factorplot(x =test['vendor'], y=pd.to_datetime(test.ptime, format='%H:%M'), data=test, type = 'violin')


#It took forever to figure this out.  This is the syntax to access parts of a
#datetime object.
#df['created_at'].dt.hour
#df['created_at'].dt.day
