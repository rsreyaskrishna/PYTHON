#2d 4*4 matrix sorting

import numpy as np
a=np.array([[2,6,3,8],[7,4,7,4],[1,8,3,7],[4,9,3,7]])
print(a)
b=np.sort(a)
print(b)

c=np.sort(a,axis=0)
print(c)