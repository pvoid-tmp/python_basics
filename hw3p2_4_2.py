import numpy as np
from scipy.optimize import fsolve


def f1(x, y):
    return (x ** 2 - y - 1)


xy = []
x1 = 1
for y1 in range(0, 5):
    q = fsolve(f1, x1, y1)
    if np.exp(x1) + x1 * (1 - y1) > 1:
        xy.append((round(q[0], 2), y1))
print(xy)

input("\n Press Enter key to exit")
