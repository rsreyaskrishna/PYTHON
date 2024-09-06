import numpy as np
import pandas as pd

df = pd.read_csv('/Users/sruthikrishna/Downloads/sample4.txt', sep=',', header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'phno', 'location']
# evaluationg functions
# 1.count()
# 2.max()
# 3.min()
# 4.sum()
# 5.mean()
# first do group operation for every evaluating functions
# count()
df1 = df.groupby('location')['location'].count()
print(df1)
#to sort the values
#df1 = df.groupby('location')['location'].count()\
    #.sort_values()
#to sort in descending order
#df1 = df.groupby('location')['location'].count()\
    #.sort_values(ascending=False)


# max()
