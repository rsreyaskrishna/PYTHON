import numpy as np
a=np.array([[4,5,6,4],[4,7,2,6],[3,7,5,7],[3,6,7,9]])
b=np.array([[3,1,2,3],[2,5,8,9],[3,5,7,9],[2,3,5,6]])

c=np.concatenate((a,b))
print(c)

print("-"*50)
d=np.concatenate((a,b),axis=1)
print(d)