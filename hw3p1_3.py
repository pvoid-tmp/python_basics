# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

# окружность
R = 10
x0 = 1
y0 = -1
x = np.linspace(-R+x0, R+x0, R*20+1)
y = [y0+sqrt(abs(R**2-(c-x0)**2)) for c in x]
plt.plot(x, y, color="#000000")
y = [y0-sqrt(abs(R**2-(c-x0)**2)) for c in x]
plt.plot(x, y, color="#000000")

# эллипс с центром в начале координат, оси которого совпадают с осями координат
A = 12
B = 9
x = np.linspace(-A, A, A*30+1)
y = [sqrt(abs(B**2 - B**2*c**2/A**2)) for c in x]
plt.plot(x, y, color="#FF0000")
y = [-sqrt(abs(B**2 - B**2*c**2/A**2)) for c in x]
plt.plot(x, y, color="#FF0000")

# гипербола
A = 6
B = 4
x = np.linspace(-A*3, -A, A*30+1)
y = [sqrt(abs(B**2 * (c**2 / A**2 - 1))) for c in x]
plt.plot(x, y, color="#00FF00")
y = [-sqrt(abs(B**2 * (c**2 / A**2 - 1))) for c in x]
plt.plot(x, y, color="#00FF00")
x = np.linspace(A, A*3, A*30+1)
y = [sqrt(abs(B**2 * (c**2 / A**2 - 1))) for c in x]
plt.plot(x, y, color="#00FF00")
y = [-sqrt(abs(B**2 * (c**2 / A**2 - 1))) for c in x]
plt.plot(x, y, color="#00FF00")

# отрисовка
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.show()
