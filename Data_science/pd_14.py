# sorting
import numpy as np
import pandas as pd

df = pd.read_csv('/Users/sruthikrishna/Downloads/sample4.txt', sep=',', header=None)

df.columns = ['id', 'fname', 'lname', 'age', 'phno', 'location']  # to give header tag to columns
print(df)

# sorting
df1=df.sort_values(by='age')    # sorting in ascending order
print(df1)

#sorting descending
df2=df.sort_values(by='age',ascending=False)
print(df2)

df3=df.sort_values(by='lname')     # sorting with alphabetical values
print(df3)
