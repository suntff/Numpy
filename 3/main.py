import numpy as np
a = np.random.normal(size=40).reshape(10,4)
print("Стандартное отклонение: ",a.std(),"Мининмальное значение:",a.min(),"Максимальное значение:",a.max(),"Среднее значение: ",a.mean())
m = a[:5,:]
print(m)