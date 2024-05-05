import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object').astype(str)
unique_values,unique_quantity = np.unique(iris[:,4], return_counts=True)
print("Уникальные значения:", unique_values,"Количество:",unique_quantity)