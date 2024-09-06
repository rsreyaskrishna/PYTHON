import numpy as np
import pandas as pd
lst=[[101,'vinay','k',27,'python',1000],
     [102,'anu','s',25,'bigdata',1250],
     [103,'arjun','p',28,'python',1500],
     [103,'arjun','p',28,'python',1500],
     [104,'vipin','d',23,'testing',1750],
     [105,'vijay','f',26,'ds',2000],
     [106,'vishnu','r',23,'ml',2500],
     [107,'appu','u',22,'bigdata',3000]]
df=pd.DataFrame(lst,columns=['id','fname','lname','age','prof','salary'])
print(df)

# to remove duplicate rows
df1=df.drop_duplicates()
print(df1)

#to remove unwanted columns----drop()
df2=df.drop(['lname'],axis=1)   #remove column lname
print(df2)

#df2=df.drop(['lname','prof'],axis=1)   ----->to remove multiple coloumns