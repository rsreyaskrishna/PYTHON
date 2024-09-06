import numpy as np
import pandas as pd

df1 = pd.read_csv('/Users/sruthikrishna/Documents/student', sep=',', header=None)
df1.columns = ['name','id']

df2=pd.read_csv('/Users/sruthikrishna/Documents/results', sep=',', header=None)
df2.columns = ['id','out']

# pass name,rollno,result

df3 = pd.merge(df1, df2, on='id', how='inner').loc[df2['out'] == 'pass', ['name', 'id', 'out']]
print(df3)