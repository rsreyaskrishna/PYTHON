import numpy as np
import pandas as pd

df1 = pd.read_csv('/Users/sruthikrishna/Downloads/custom.txt', sep=',', header=None)
df1.columns = ['id','name','age','loc','salary']

df2=pd.read_csv('/Users/sruthikrishna/Downloads/order.txt', sep=',', header=None)
df2.columns = ['orderid','date','id','amount']

#name,age,loc,date,amount
df3=pd.merge(df1,df2,on='id',how='inner')[['name','age','loc','date','amount']]
print(df3)

#salary above 2000 name,age,loc,date,amount
df4=pd.merge(df1,df2,on='id',how='inner').loc[df1['salary']>2000][['name','age','loc','date','amount']]
print(df4)

#latest date name,age,salary,amount,date
df5=pd.merge(df1,df2,on='id',how='inner').sort_values(by='date',ascending=False)\
       [['name','age','salary','amount','date']].head(1)
print(df5)
