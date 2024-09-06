import numpy as np
import pandas as pd
ss=pd.Series([4,1,8,9,2,3,6,7,8,20,11,13,14,17,60])
print(ss)

#order
print(ss.shape)
#data type
print(ss.dtype)
#total number of elements
print(ss.size)

#head=====>print first 5 elements
print(ss.head())

print(ss.head(3))  #to print first 3 elements
#tail()====>print last 5 values
print(ss.tail())
print(ss.tail(4))   #to print last 4 values