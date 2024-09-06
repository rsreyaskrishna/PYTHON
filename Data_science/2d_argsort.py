import numpy as np
a=np.array([[4,1,9,0],[1,3,4,7],[3,0,8,5],[8,1,2,3]])
print(a)
print("-"*50)
b=np.argsort(a)    #rowwise arg sort
print(b)

print("-"*50)
c=np.argsort(a,axis=0)
print(c)

#arg max-index of highesht element
#arg min-index of lowest element
d=np.argmax(a)
print(d)
e=np.argmin(a)
print(d)


f=np.argmax(a,axis=0)
print(f)

g=np.argmax(a,axis=1)
print(g)

h=np.argmin(a,axis=0)
print(h)

i=np.argmin(a,axis=1)
print(i)
