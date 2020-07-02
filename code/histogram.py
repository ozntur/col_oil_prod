import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import glob
import datetime

## read multiple csv file in a folder
data_folder = '/Users/ozanturkes/OneDrive - Auburn University/901_Kisisel/col-data/07-01-2020'

# glob.glob('data*.csv') - returns List[str]
# pd.read_csv(f) - returns pd.DataFrame()
# for f in glob.glob() - returns a List[DataFrames]
# pd.concat() - returns one pd.DataFrame()

print('Started reading csv files\n')
df = pd.concat([pd.read_csv(f) for f in glob.glob('data/col-data/07-01-2020/*.csv')], ignore_index = False)

df['First of Month'] = pd.to_datetime(df['First of Month'])

print('\n Data ready')
fnumb = df['Formation'][(df['First of Month'] > '2018-4-1')].value_counts().values
#form = df[df['Formation'].value_counts() < 50000 & df['First of Month'].loc[2018-04-01:2020-04-01]].value_counts().index.values
form = df['Formation'][(df['First of Month'] > '2018-4-1')].value_counts().index.values


#objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
objects = form
#y_pos = np.arange(len(objects))
y_pos = len(fnumb)
#performance = [10,8,6,4,2,1]
performance = fnumb

plt.bar(y_pos, performance, align='center', alpha=0.5)

plt.xticks(y_pos, objects)

plt.ylabel('Usage')
plt.title('Programming language usage')

plt.show()






