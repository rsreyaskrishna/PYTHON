import numpy as np
a = np.array([[5,2,3],[4,5,6],[3,4,5]])
print(a)
print("*"*100)
#3d
b=a.reshape([1,3,3])
print(b)
print("*"*100)
#1d
c=a.reshape(9)  # c=a.flatten()
print(c)