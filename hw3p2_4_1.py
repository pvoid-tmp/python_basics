import numpy as np
from scipy.optimize import fsolve


def equ_sys(p):
    x, y = p
    return (x ** 2 - y - 1, np.exp(x) + x * (1 - y) - 1)


x1, x2 = fsolve(equ_sys, (1, 1))
print(x1, x2)

input("\n Press Enter key to exit")
