#2Dimension 4*4 matrix

import numpy as np
a=np.array([[3,6,4,9],[2,3,7,5],[3,9,4,6],[1,5,9,7]])     # 2d 4*4 matrix
print(a)
b=np.sum(a)   #sum
print(b)
# to print row / column sum

# axis = 0
# axis = 1
c=np.sum(a,axis=0)   # gives sum of row
print(c)

d=np.sum(a,axis=1)  # gives sum of column
print(d)

#max of 2D matrix

e=np.max(a)
print(e)

# to get row wise max
f=np.max(a,axis=1)
print(f)

#to get column wise max
g=np.max(a,axis=0)
print(g)

# to get row wise min
h=np.min(a,axis=1)
print(h)
#to get coloumnwise min
i=np.min(a,axis=0)
print(i)

