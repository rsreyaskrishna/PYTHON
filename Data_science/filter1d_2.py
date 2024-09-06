import numpy as np    #collect divisible by 5 from array of 1 to 50
a=np.arange(1,51)
print(a)
b=a%5==0
c=a[b]
d=c.reshape(2,5)
print(d)