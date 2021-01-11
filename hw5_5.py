import numpy as np

n = 100
r = 0.7
x = np.random.rand(n)
y = r*x + (1 - r)*np.random.rand(n)
print(f"встроенная функиця: {np.corrcoef(x, y)[0][1]:.6f}")

R = np.sum((x - np.mean(x))*(y - np.mean(y))) / np.sqrt(np.sum((x - np.mean(x))**2)*np.sum((y - np.mean(y))**2))
print(f"ручная функция: {R:.6f}")
