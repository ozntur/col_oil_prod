# col_oil_prod
Colorado Oil production - downloading data from website using pandas and plotting using matplotlib

Jupyter notebook 'jupyternotebook/one.ipynb' explains all codes and steps. Jupyter notebook can be a little slow in the beginning! Additionally, you can find the necessary code in the folder 'code'. 

Plotting time series using oil production data is significant. Oil production data is usually found in state websites and they are scattered in tables. In this repo Colorado Oil & Gas Conservation Commission, oil production data were used to plot time series.

1 - Shape files were opened using 'geopandas' and API # of producing wells were masked. 

2 - Colorado Oil & Gas Conservation Commission oil production data which was in html (as tables in a website), were obtained using 'pandas'.

3 - Plotted using 'matplotlib'. 

This database was a huge one. I masked producing wells and put a 'break' at some point to show how this code can run. One can edit the code for his/her purpose (for instance plotting oil production that has a mean value of 'X' bbl in last 2 years etc..). 

Please let me know if you are having trouble with the repo OR if you have any advice/suggestions. 



