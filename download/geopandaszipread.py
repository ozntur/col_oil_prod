import geopandas as gpd

#url = 'https://cogcc.state.co.us/documents/data/downloads/gis/WELLS_SHP.ZIP'
file_path = '/Users/ozanturkes/coding/GitHub/prod_data/data/WELLS_SHP/Wells.shp'

ds = gpd.read_file(file_path)

print(ds.columns.values)

print('done')

print(ds[ds.Facil_Stat == 'PR'])

print('done')

ds.plot()