from wrangle import *
import seaborn as sns

sns.barplot(x='address', y='count', data = freq)

def barplot(count):
    plot = sns.barplot(x = count.columns[0], y = count.columns[1], data = count)
    return(plot)
