import numpy as np
import pandas as pd
df = pd.read_csv('/Users/sruthikrishna/Downloads/customer1.txt', sep=',', header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'location']
#1.age above 50 fname,lname,age,prof,loc
df1=df.loc[df['age']>50] [['fname','lname','age','prof','location']]
print(df1)
# 2.age rane 25 to 40 fname lname age prof
df2=df.loc[df['age'>25]&df['age'<40]] [['fname','lname','age']]
print(df2)
# 3.india work fname,lname,age prof
df3=df.loc[df['location']=='india'] [['fname','lname','age','prof']]
print(df3)
# 4.age max 5 employees fname,lname,age prof
df4=df.sort_values(by='age', ascending=False)\
      [['fname', 'lname', 'age', 'prof']] \
      .head(5)
print(df4)
# 5.age  min 3 employee fname lname age prof
df5=df.sort_values(by='age')\
      [['fname', 'lname', 'age', 'prof']] \
      .head(3)
print(df5)
# 6.india work,age minimum 3 employee fname lname age
df6=df.loc[df['location'] == 'india']\
       .sort_values(by='age')\
       [['fname', 'lname', 'age']].head(3)
print(df6)
# 7.india and prof doctor fname lname age prof
df7 = df.loc[(df['location'] == 'india') & (df['prof'] == 'doctor')]\
         [['fname', 'lname', 'age', 'prof']]
print(df7)

# 8.pilot prof age min 1 employee fname lname age
df8=df.loc[df['prof'] == 'pilot']\
       .sort_values(by='age')\
       [['fname', 'lname', 'age']]
print(df8)

# 9.doctor prof age max 1 employee full data
df9=df.loc[df['prof'] == 'doctor']\
       .sort_values(by='age',ascending=False)\
       [['fname', 'lname', 'age']].head(3)
print(df9)