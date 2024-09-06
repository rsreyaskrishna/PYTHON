import numpy as np
import pandas as pd

df = pd.read_csv('/Users/sruthikrishna/Downloads/customer1.txt', sep=',', header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'location']
#print(df)
print(df.isna().sum())  # print the missing values
df1 = df.fillna('india')  # fill the missing the values with india
# 1. find row count
print(df1.shape)
# 2.remove duplicate rows and find total row count
df2 = df1.drop_duplicates().shape
print(df2)
# 3. Age maximum 10 fname,lname,prof,loc
df3 = df.sort_values(by='age', ascending=False)[['fname', 'lname', 'prof', 'location']].head(10)
print(df3)
# 4. Age minimum 5 employees fname,lname,prof,loc
df4 = df.sort_values(by='age')[['fname', 'lname', 'prof', 'location']].head(5)
print(df4)
# 5. Each location count [count desc order]
df5 = df.groupby('location')['location'].count().sort_values(ascending=False)
print(df5)
# 6. Full data
df6 = df.loc[df['location'] == 'australia']
print(df6)
# 7. Each age group count [age desc order]
df7 = df.groupby('age')['age'].count().sort_values(ascending=False)
print(df7)
# 8. Each profession count [count desc order]
df8 = df1.groupby('prof')['prof'].count().sort_values(ascending=False)
print(df8)
# 9. India work
# A. Row count
df9 = df1.loc[df1['location'] == 'india'].shape
print(df9)
# B. Each profession count [count desc order]
df10 = df1.loc[df1['location'] == 'india'].groupby('prof')['prof'].count()\
          .sort_values(ascending=False)
print(df10)
# C. Age mxm 3 employees fname,lname,age,prof
df11 = df1.loc[df1['location'] == 'india'].sort_values(by='age', ascending=False)\
          [['fname', 'lname', 'age', 'prof']].head(3)
print(df11)
# D. Age minimum 3 employees fname,lname,age,prof
df12=df1.loc[df1['location'] == 'india'].sort_values(by='age')\
          [['fname', 'lname', 'age', 'prof']].head(3)
print(df12)
# E. age above 40 full data
df13=df1.loc[(df1['location']== 'india')&(df1['age']>40)]
print(df13)
# F. age range 30 to 40 [profession count]
df14 = df1.loc[(df1['location'] == 'india') & (df1['age'].between(30, 40))]\
            .groupby('prof')['prof'].count()
print(df14)
# 10. us work
# A. Row count
df15=df1.loc[df1['location'] == 'us'].shape
print(df15)
# B. Each age group count
df16=df1.loc[df1['location'] == 'us'].groupby('age')['age'].count()
print(df16)
# C. Each profession count [count desc]
df17 = df1.loc[df1['location'] == 'us'].groupby('prof')['prof'].count()\
          .sort_values(ascending=False)
print(df17)
# D. Civil engineer dept and age above 30
df18= df1.loc[(df1['location'] == 'us') & (df1['prof'] == 'Civil engineer') & (df1['age'] > 30)]
print(df18)
