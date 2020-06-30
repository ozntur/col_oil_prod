import geopandas as gpd
import pandas as pd

ds = gpd.read_file('data/WELLS_SHP/Wells.shp')
print('asd')
#print('done')
print(ds.API[ds.Facil_Stat == 'PR'])
#print('done')
d = {}

for x in (ds.API[ds.Facil_Stat =='PR']):
    a = ds.API_County.loc[ds.API == x].item()
    b = ds.API_Seq.loc[ds.API == x].item()
    print('x = ' + x + ' a = ' + a + ' b =' + b)
    website = 'https://cogcc.state.co.us/production/?&apiCounty='+a+'&apiSequence='+b+'&APIWB=00&Year=All'
    print(website)
    dfs = pd.read_html(website)
    dfs[1]['First of Month'] = pd.to_datetime(dfs[1]['First of Month'])

    data = {
    'Time' : dfs[1]['First of Month'] ,
    'Oilprod' : dfs[1]['Oil Produced']
    }
    d[x] = pd.DataFrame(data)
    if b == '08294':
        break

print('finished')

for m in list(d):
    plt.plot(d[m]['Time'], d[m]['Oilprod'], label = m)

#plt.legend()
plt.xlabel('Date')
plt.ylabel('Oil Produced')
plt.show()




    
