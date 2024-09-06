import numpy as np
import pandas as pd

df = pd.read_csv('/Users/sruthikrishna/Downloads/customer1.txt', sep=',', header=None)

df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'location']  # to give header tag to columns
print(df)

df1=df[['fname','lname','age','prof']]    # to collect only certain columns in a data frame
print(df1)


# collect fname lname age of first 20 customers
df2=df[['fname','lname','age']].head(20)
print(df2)

# iloc()-----> to collect data from rows inbetween
df3=df.iloc[4]
print(df3)


df4=df.iloc[3:5,2:5]    # row-3,4 column--2,3,4
print(df4)