import numpy as np
import pandas as pd

dic={'id':101,'fname':'vinay','lmame':'k','age':28,'salary':1000}
ss=pd.Series(dic,index=['lname','fname','age','id','salary'])
print(ss)