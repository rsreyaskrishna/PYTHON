import numpy as np
import pandas as pd
lst=[[101,'vinay','k',27,'python',1000],
     [102,'anu','s',25,'bigdata',1250],
     [103,'arjun','p',28,'python',1500],
     [104,'vipin','d',23,'testing',1750],
     [105,'vijay','f',26,'ds',2000],
     [106,'vishnu','r',23,'ml',2500],
     [107,'appu','u',22,'bigdata',3000]]
df=pd.DataFrame(lst,columns=['id','fname','lname','age','prof','salary'])
print(df)

print(df.shape)     # shape------(7,6)
print(df.dtypes)    # data type ---data type if each rows
print(df.size)      # size--- total  number of elements  ----42
print(df.head())    # first 5 rows
print(df.head(3))   # first 3 rows
print(df.tail(2))   # last 2 rows
