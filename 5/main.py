import numpy as np
from scipy.stats import multivariate_normal
import time
def ln_p(x, m, C):
    constant_term = -0.5 * m.shape[0]* np.log(2 * np.pi)
    quadratic_term = np.sum(np.dot((x - m), np.linalg.inv(C)) * (x - m), axis=1)
    return constant_term - 0.5 * np.log(np.linalg.det(C)) - 0.5 * quadratic_term
start_time = time.time()
m = np.array([0, 0])
C = np.array([[1, 0.5], [0.5, 2]])
x = np.random.normal(size=(12, 2))
log_density_custom = ln_p(x, m, C)
print("собственная реализация:",log_density_custom,sep='\n')
custom_time = time.time() - start_time
print("Время выполнения (собственная реализация):", custom_time)
start_time = time.time()
ln_density_scipy = multivariate_normal(m, C).logpdf(x)
print("scipy:",ln_density_scipy,sep='\n')
scipy_time = time.time() - start_time
print("Время выполнения (scipy):", scipy_time)
