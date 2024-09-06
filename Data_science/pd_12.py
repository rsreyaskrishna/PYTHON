import numpy as np
import pandas as pd

df = pd.read_csv('/Users/sruthikrishna/Downloads/customer5.txt', sep=',', header=None)

df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'location', 'salary']  # to give header tag to columns
print(df)

print("*" * 50)
# total  number of missing values
print(df.isna().sum())

print("*" * 50)
#last 20 rows fname,lname,age,prof
df2 = df[['fname', 'lname', 'age', 'prof']].tail(20)
print(df2)

print("*" * 50)
#x
x = df.iloc[:, :-1]
print(x)

print("*" * 50)
#y
y = df.iloc[:, -1]
print(y)

# loc ---> used for collecting data that satisfies the given condition
# df1=df.loc[df['column_name']condition]----->syntax

# collect data of persons with age >40
df3=df.loc[df['age']>40] [['fname','lname','age']]   # collect fname lname age of persons with age>40
print(df3)

#collect details of persons with age <=30 ---fname,lname,age,prof
df4=df.loc[df['age']<=30] [['fname','lname','age','prof']]
print(df4)
# collect fname,lname,age ,prof,salary of person working in india
df5=df.loc[df['location']=='india'] [['fname','lname','age','prof','salary']]
print(df5)


#for passing more than one condition
#df1=df.loc[(df['colname']condition)and(df['colname']condition)]

# age above 40 and working location india
df6=df.loc[(df['age']>40)&(df['location']=='india')]
print(df6)
