import numpy as np
import pandas as pd

df = pd.read_csv('/Users/sruthikrishna/Downloads/sample4.txt', sep=',', header=None)

df.columns = ['id', 'fname', 'lname', 'age', 'phno', 'location']  # to give header tag to columns
print(df)

#age equal to 21 fname,lname,age,phno
df3=df.loc[df['age']==21] [['fname','lname','age','phno']]   #
print(df3)


#age above 22 fname lname age
df4=df.loc[df['age']>22] [['fname','lname','age']]
print(df4)
#chennai work fname,lname,age,phno
df5=df.loc[df['location']=='Chennai'] [['fname','lname','age','phno']]
print(df5)

#age above 23 and loc chenai fname,lname,age
df6=df.loc[(df['age']>23)&(df['location']=='Chennai')][['fname','lname','age']]
print(df6)