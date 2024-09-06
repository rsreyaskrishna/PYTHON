import numpy as np
import pandas as pd

# Load the data
df = pd.read_csv('/Users/sruthikrishna/Downloads/missing_data.csv', sep=',')
#df.columns = ['Duration','Date','Pulse','Maxpulse','Calories']
#print(df)

print(df.isna().sum())  # to find the missing valves

#dropna()
# df.dropna(inplace=True,ignore_index=True)
# print(df)

df.dropna(subset=['Date'],inplace=True,ignore_index=True)   # to drop missing values oand row checking only date column
print(df)

#wrong data
df.loc[7,'Duration']=45


# above 400 wrong data # check column calorie remove wrong data above 400
x=df['Calories'].mean()
for i in df.index:
    if df.loc[i,'Calories']> 400:
        df.loc[i,'Calories']=x
print(df)