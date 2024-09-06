import numpy as np
import pandas as pd

df = pd.read_csv('/Users/sruthikrishna/Downloads/customer5.txt', sep=',', header=None)

df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'location', 'salary']
# each prof count
df1=df.groupby('prof')['prof'].count().sort_values(ascending=False)
print(df1)

# each prof max salary
df2=df.groupby('prof')['salary'].max()\
     .sort_values(ascending=False)
print(df2)
# each prof min salary
df3=df.groupby('prof')['salary'].min()\
     .sort_values(ascending=False)
print(df3)
#  each loc max age
df4=df.groupby('location')['age'].max()\
     .sort_values(ascending=False)
print(df4)
# each prof total salary
df5=df.groupby('prof')['salary'].sum()\
     .sort_values(ascending=False)
print(df5)