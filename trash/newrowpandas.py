## new row
import pandas as pd

data = {'name': ['Somu', 'Kiku', 'Amol', 'Lini'],
	'physics': [68, 74, 77, 78],
	'chemistry': [84, 56, 73, 69],
	'algebra': [78, 88, 82, 87]}

	
#create dataframe
df_marks = pd.DataFrame(data)
print('Original DataFrame\n------------------')
print(df_marks)

new_row = {'name':'Geo', 'physics':87, 'chemistry':92, 'algebra':97}
#append row to the dataframe
df_marks = df_marks.append(new_row, ignore_index=True)

print('\n\nNew row added to DataFrame\n--------------------------')
print(df_marks)