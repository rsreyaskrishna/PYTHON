import numpy as np
a=np.array([5,8,1,10,15,40,43,21,17,13,12,13,1,10,1])
b=np.where(a==1)
print(b)
c=np.where(a%2==0)
print(c)   #gives index of even number