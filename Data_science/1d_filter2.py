import numpy as np    #collect even numbers from array of 1 to 50
a=np.arange(1,51)
print(a)
b=a%2==0
c=a[b]
print(c)