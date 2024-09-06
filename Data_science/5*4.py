import numpy as np
a = np.array([[5,2,3,4],[4,5,6,7],[3,4,5,6],[1,2,3,4],[3,6,7,8]])
print(a)
print("*"*100)
#4*5
b=a.reshape([4,5])
print(b)
print("*"*100)
#2*10
c=a.reshape([2,10])
print(c)

print("*"*100)
#3d
d=a.reshape([1,5,4])
print(d)

print("*"*100)

#1d
e=a.reshape(20)
print(e)

