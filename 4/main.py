import numpy as np
x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
ind_with_0 = np.where(x[:-1] == 0)[0]
ind_without_0 = np.where(x[ind_with_0+1]!=0)[0]
ind = ind_with_0[ind_without_0]
print(x[ind+1].max())