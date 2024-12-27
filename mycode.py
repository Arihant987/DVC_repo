import pandas as pd
import os

data={
    'name':['Tom','Jerry','Mickey'],
    'age':[20,21,22],
    'city':['New York','Los Angeles','Orlando']
}
df=pd.DataFrame(data)

# add new row 
new_row={
    'name':'gf',
    'age':19,
    'city':'San Francisco'
}
df.loc[len(df.index)]=new_row 




data_dir='data'
os.makedirs(data_dir,exist_ok=True)

file_path=os.path.join(data_dir,'sample_data.csv')
df.to_csv(file_path,index=False)

print(f"csv file saved to {file_path}")