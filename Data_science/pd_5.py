import numpy as np
import pandas as pd
a=pd.Series([1,4,5,6,7,10,3,5,6])
b=pd.Series([2,4,6,7,8,3,5,12,3])
#append====>join
c=a._append(b,ignore_index=True)
print(c)

#add
d=a.add(b)
print(d)
# substract
e=a.subtract(b)
print(e)
# multiply
f=a.multiply(b)
print(f)
# divide
g=a.divide(b)
print(g)