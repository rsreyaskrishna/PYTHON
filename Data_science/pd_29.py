import numpy as np
import pandas as pd

# Load the data
df = pd.read_csv('/Users/sruthikrishna/Downloads/heart.csv', sep=',')
print(df)
print(df.isna().sum())
x=df['Sex'].mode()[0]
df['Sex'].fillna(x,inplace=True)
print(df)