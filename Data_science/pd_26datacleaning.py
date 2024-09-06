import numpy as np
import pandas as pd

# Load the data
df = pd.read_csv('/Users/sruthikrishna/Downloads/missing_data.csv', sep=',')
#df.columns = ['Duration','Date','Pulse','Maxpulse','Calories']
print(df)

print(df.isna().sum())  # to find the missing valves
#18   22   28

# df1=df.fillna('300')
# print(df1)              #  fill missing values with 300

# fill calorie column missing value with 280
df['Calories'].fillna(280,inplace=True)
print(df)
# fill column date with 02/07/2024
df['Date'].fillna('02/07/2024',inplace=True)
print(df)