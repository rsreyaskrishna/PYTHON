# 2d 4*5 slicing

import numpy as np
a=np.array([[2,3,4,7,8],[7,4,7,2,4],[2,3,8,5,4],[6,4,8,5,3]])
print(a)

print("-"*50)
# 2dimensional slicing
# print(s[row,column])
print(a[1:4,:3])  #row=1,2,3   column=0,1,2

print("-"*50)

print(a[:3,1:4])    #  row=0,1,2  column=1,2,3
print("-"*50)
print(a[1::2,1::2])  # row=1,3  column=1,3