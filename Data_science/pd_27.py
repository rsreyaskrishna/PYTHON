import numpy as np
import pandas as pd

# Load the data
df = pd.read_csv('/Users/sruthikrishna/Downloads/missing_data.csv', sep=',')
#df.columns = ['Duration','Date','Pulse','Maxpulse','Calories']
#print(df)

print(df.isna().sum())  # to find the missing valves
# filling with mean
x=df['Calories'].mean()
#x=df['Calories'].median()/x=df['Calories'].mode()[0]
df['Calories'].fillna(x,inplace=True)
#print(df)

y=df['Date'].mode()[0]
df['Date'].fillna(x,inplace=True)
print(df)