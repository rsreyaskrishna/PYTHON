import numpy as np
import pandas as pd

df = pd.read_csv('/Users/sruthikrishna/Downloads/Temperature', sep=' ', header=None)
df.columns = ['year','temp']

# max temp on each year
df1=df.groupby('year')['temp'].max()\
     .sort_values(ascending=False)
print(df1)

# min temp on each year
df2=df.groupby('year')['temp'].min()\
     .sort_values(ascending=False)
print(df2)

#total temp on each year------sum()
df3=df.groupby('year')['temp'].sum()\
     .sort_values(ascending=False)
print(df3)

# avg temp on each year------mean()
df4=df.groupby('year')['temp'].mean()\
     .sort_values(ascending=False)
print(df4)