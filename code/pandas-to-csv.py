# DOWNLOAD SHP FILE DATA --> READ WELLS
# USE API'S TO PULL OIL/GAS PRODUCTION ETC. DATA --> DOWNLOAD THE DATA AS CSV -- PANDAS --> CSV

import geopandas as gpd
import pandas as pd
import datetime
print('Reading Wells.shp\n')

file_path = 'https://cogcc.state.co.us/documents/data/downloads/gis/WELLS_SHP.ZIP'

ds = gpd.read_file(file_path)

print('Wells.shp - successful\n')

size_numb = len(ds.index) # number of wells

print('starting time: ' + str(datetime.datetime.now()) + '\n')

#group = ds.API
#group = ds.API[ds.Facil_Stat =='PR']
#group1 = len(ds.index)
for row in ds.itertuples():
    
    print('# of wells left: ' + str(size_numb))
    size_numb = size_numb - 1
    
    website = 'https://cogcc.state.co.us/production/?&apiCounty='+row.API_County+'&apiSequence='+row.API_Seq+'&APIWB=00&Year=All'

    try:
        asd = pd.read_html(website)
        dfs = asd[1]
        if (dfs['API County'][2] == int(row.API_County) and dfs['API Sequence'][2] == int(row.API_Seq)):
            print('esitlik saglandi')
        else:
            print('IF ERROR API: ' + row.API)
            print(dfs['API County'][2]) 
            print(row.API_County) 
            print(dfs['API Sequence'][2]) 
            print(row.API_Seq)
            continue
        print('try worked')
    except Exception as exp:
        print('except worked exception: ' + str(exp) + ' API: ' + row.API)
        continue
    else:
        print('x = ' + row.API + ' a = ' + row.API_County + ' b = ' + row.API_Seq)
        print(website)
        dfs['First of Month'] = pd.to_datetime(dfs['First of Month'])
        dfs.to_csv(row.API + '.csv')
        print('else worked')

print('End time:  ' + str(datetime.datetime.now()))