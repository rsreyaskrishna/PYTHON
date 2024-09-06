import numpy as np
a=np.array([41,42,43,44,45,46,47,48,49,50])
#above 44
b=a>44

c=a[b]
print(c)
