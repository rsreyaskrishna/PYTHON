import numpy as np
import pandas as pd

df = pd.read_csv('/Users/sruthikrishna/Downloads/customer1.txt', sep=',', header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'location']
#max()
df1=df.groupby('prof')['age'].max()     # max age of person in each profession
print(df1)

df2=df.groupby('location')['age'].max().sort_values(ascending=False)  # max age of person in each location-descending order
print(df2)