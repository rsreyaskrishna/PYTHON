import numpy as np
import pandas as pd
dic1= {'id':[1,2,3,4,5],'fname':['vinay','anu','vipin','nikil','arun'],'lname':['k','p','s','r','t'],
      'age':[34,46,22,22,10]}

dic2={'prof':['python','bigdata','ml','ai','python'],'salary':[1000,1500,2000,2500,3000],
      'id':[3,4,5,6,7],'loc':['tvm','kollam','erklm','kollam','kannur']}
df1=pd.DataFrame(dic1)
df2=pd.DataFrame(dic2)
print(df1)
print(df2)
# inner joining----id matching data from 2 data frame will be combined
# i,e ---->3,4,5
df3=pd.merge(df1,df2,on='id',how='inner')
print(df3)
# to get only required columns
df4=pd.merge(df1,df2,on='id',how='inner')[['fname','lname','age','prof']]
print(df4)
#print details of person with age=22
df5=pd.merge(df1,df2,on='id',how='inner')\
    .loc[df1['age']==22 ][['fname','lname','prof','salary']]
print(df5)

