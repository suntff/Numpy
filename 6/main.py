import numpy as np
a = np.arange(16).reshape(4,4)
print(a)
cols = [2, 1, 0, 3]
a = a[cols,:]
print(a)
