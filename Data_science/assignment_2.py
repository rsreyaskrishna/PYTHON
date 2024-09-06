import numpy as np
import pandas as pd

df = pd.read_csv('/Users/sruthikrishna/Downloads/movies_cleaned_pandas.csv', sep=',', header=None)

df.columns = ['movieid', 'name', 'year', 'rating', 'duration']
# 1. Find row count
print(df.shape)
# 2. Remove duplicates and find row count
df1 = df.drop_duplicates().shape
print(df1)
# 3. Sort data set by release year in des order
df3= df.sort_values(by='year',ascending=False)
print(df3)
# 4. Find rating mxm 5 movies name,year,rating
df4 = df.sort_values(by='rating', ascending=False)\
          [['name','year','rating']].head(5)
print(df4)

# 5. Find rating minimum 3 movies name,year,rating
df5 = df.sort_values(by='rating')\
          [['name','year','rating']].head(3)
print(df5)
# 6. Find Each year release movie count [count desc order]
df6=df.groupby('year')['year'].count()\
      .sort_values(ascending=False)
print(df6)
# 7. Each rating count [count desc order]
df7=df.groupby('rating')['rating'].count()\
      .sort_values(ascending=False)
print(df7)
# 8. 2008 and rating above 3 [collect]
df8=df.loc[(df['year']==2008)&(df['rating']>3.0)]
print(df8)
# A. row count
df9=df.loc[(df['year']==2008)&(df['rating']>3.0)].groupby('year')['year'].count()\
          .sort_values(ascending=False)
print(df9)
# 9. Find duration mxm 1 movies name,year,rating,duration
df10 = df.sort_values(by='duration', ascending=False)\
          [['name','year','rating','duration']].head(1)
print(df10)
# 10. Find rating minimum 1 movies name,year,rating,duration
df11 = df.sort_values(by='rating')\
          [['name','year','rating']].head(1)
print(df11)

# 11. Rating above 4 and release year above 2005
df12=df.loc[(df['year']>2005)&(df['rating']>4.0)]
print(df12)
# A. Rating mxm movies full data
df13=df.loc[(df['year']>2005)&(df['rating']>4.0)].sort_values(by='rating', ascending=False)\
          .head(1)
print(df13)
# B. Rating mnm movies full data
df14=df.loc[(df['year']>2005)&(df['rating']>4.0)].sort_values(by='rating')\
          .head(1)
print(df14)
# 12. 2008 movies count
df15=df.loc[df['year'] == '2008'].shape
print(df15)
# 13. 1975-2000 movies collect
df16=df.loc[(df['year']>1975)&(df['year']<2000)]
print(df16)
# A. Row count
df17=df.loc[(df['year']>1975)&(df['year']<2000)].shape
print(df17)
# 14. 1975-2000 and rating above 3.5 total row count
df18=df.loc[(df['year']>1975)&(df['year']<2000)&(df['rating']>3.5)].shape
print(df18)
