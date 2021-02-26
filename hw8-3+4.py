import numpy as np
from scipy.optimize import fsolve


def eq(p):
    x1, x2 = p
    u1 = x1**2 - x2**2 + 3*x1*x2**3 - 2*x1**2*x2**2 + 2*x1 - 3*x2 - 5
    u2 = 3*x2**3 - 2*x1**2 + 2*x1**3*x2 - 5*x1**2*x2**2 + 5
    return u1, u2


res = []
epsilon = 7
for i in range(-10, 10, 1):
    for j in range(-10, 10, 1):
        (x, y), info, ier, msg = fsolve(eq, np.array([i*10, j*10]), full_output=True)
        x = round(x, epsilon)
        y = round(y, epsilon)
        if ier == 1 and res.count([x, y]) == 0:
            res.append([x, y])
print(res)

input("\n\nPress Enter to exit.")
