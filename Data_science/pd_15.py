import numpy as np
import pandas as pd
df = pd.read_csv('/Users/sruthikrishna/Downloads/sample4.txt', sep=',', header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'phno', 'location']  # to give header tag to columns


#1. age max 2, employee fname lname age phno
df1=df.sort_values(by='age', ascending=False)\
      [['fname', 'lname', 'age', 'phno']] \
      .head(2)
print(df1)

#2.age minimum 1 employee fname lname age
df2=df.sort_values(by='age')\
      [['fname', 'lname', 'age']]\
      .head(2)
print(df2)


#chennai work age max 1 employee fname lname age phno
df3=df.loc[df['location'] == 'Chennai']\
       .sort_values('age', ascending=False)\
       [['fname', 'lname', 'age', 'phno']].head(1)
print(df3)