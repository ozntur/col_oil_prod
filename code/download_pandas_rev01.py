###### read shp file with geopandas ######

import geopandas as gpd
print('reading shp file data')
print()
my_df = gpd.read_file('data/WELLS_SHP/Wells.shp')

print('data is ready, printing shp file data')
print()
print(my_df[my_df.Facil_Stat == 'PR'])

a = '001'     ##county number
b = '05299'   ## well number

###### read them by using pandas #####
import pandas as pd

website = 'https://cogcc.state.co.us/production/?&apiCounty='+a+'&apiSequence='+b+'&APIWB=00&Year=All'
print(website)

dfs = pd.read_html(website)
print()
print('printing data from web')
print()
dfs[1]['First of Month'] = pd.to_datetime(dfs[1]['First of Month'])
print(dfs[1])

#create graphs
import matplotlib.pyplot as plt

#N = 50
#x = pd.to_datetime(dfs['First of Month'])
x = dfs[1]['First of Month']
y = dfs[1]['Oil Produced']
z = dfs[1]['Water Volume']
d = dfs[1]['Gas Produced']
#colors = np.random.rand(N)
#area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

#plt.scatter(x, y, s=area, c=colors, alpha=0.5)

#plt.plot(x, y, alpha=0.5, label = 'Oil Produced')
#plt.plot(x,z, alpha = 0.5, label = 'Water Volume')

line_a, =plt.plot(x, y, label = 'Oil Produced')
#line_b, =plt.plot(x, z, label = 'Water Volume')
line_c, = plt.plot(x, d, label = 'Gas Produced')
plt.xlabel('Date')
#plt.ylabel('Oil Produced')
plt.legend()
plt.show()



