import numpy as np
import pandas as pd

lst = [[101,'vinay','k',27,'python',1000],
       [102,'anu','s',25,'bigdata',1250],
       [103,'arjun','p',28,'python',1500],
       [104,'vipin','d',23,'testing',1750],
       [105,'vijay','f',26,'ds',2000],
       [106,'vishnu','r',23,'ml',2500],
       [107,'appu','u',22,'python',3000]]

df = pd.DataFrame(lst, columns=['id', 'fname', 'lname', 'age', 'prof', 'salary'])
print(df)
print("*" * 100)

# Describe
print(df.describe())
print("*" * 100)

# Describe including object types
print(df.describe(include=[object]))
print(df.describe(include='all'))

#how to add new column
df['Gender']=['M','M','F','F','M','M','M']
print(df)

#how to rename a column
df1=df.rename(columns={'fname':'first_name'})
print(df1)

