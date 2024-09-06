# converting an External file to dataframe
import numpy as np
import pandas as pd

df = pd.read_csv('/Users/sruthikrishna/Downloads/customer1.txt', sep=',', header=None)

df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'location']  # to give header tag to columns
print(df)

print(df.dtypes)  # print data types of each column

print(df.isna().sum())  # calculate total number of missing values corresponding to each column

# filling the missing values----> fillna()
df1=df.fillna('nothing')     # fill every missing value with the word nothing
print(df1.isna().sum())     # now there will not be any missing value as every missing value is fillled with nothing
