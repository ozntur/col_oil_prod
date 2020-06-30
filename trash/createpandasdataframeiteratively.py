### Create pandas dataframe iteratively ###
import pandas as pd

my_df = []
for i in range(0,10):
    d = {
        'val0' : 1,  # some formula for obtaining values
        'val1' : 2.5,
        'val2' : 1.8
    }
    my_df.append(d)

my_df = pd.DataFrame(my_df)

print(my_df)
