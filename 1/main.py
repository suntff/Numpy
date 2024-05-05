import numpy as np
data = np.loadtxt('input.txt', delimiter=',', unpack=True)
print("Сумма элементов:",data.sum(),"Мининмальный элемент:",data.min(),"Максимальный элемент:",data.max())
