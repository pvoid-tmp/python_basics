# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

phi = np.linspace(0, 2*np.pi, 100)
r = 0*phi + 3.0
plt.polar(phi, r)

r = np.linspace(0, 5, 100)
gamma = np.arctan(1)
phi = 0*r + gamma
plt.polar(phi, r)

plt.show()
