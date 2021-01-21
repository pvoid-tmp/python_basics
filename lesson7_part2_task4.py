import numpy as np
from scipy.linalg import lu

a = np.array([[1, 2, 3], [2, 16, 21], [4, 28, 73]])
plu = lu(a)
print(plu[0])
print(plu[1])
print(plu[2])
print(f"det = {np.linalg.det(a)}")

b = np.array([12, 2, 1])
print(f"решение: {np.linalg.solve(a, b)}")
