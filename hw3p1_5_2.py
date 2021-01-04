# %matplotlib inline
from pylab import *
from mpl_toolkits.mplot3d import Axes3D


def sqrt_a(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] = sqrt(a[i][j]) if a[i][j] >= 0 else None
    return a


fig = figure()
ax = Axes3D(fig)

# сфера
R = 5
X = arange(-5, 5, 0.1)
Y = arange(-5, 5, 0.1)
X, Y = meshgrid(X, Y)
Z = sqrt_a(R**2 - X**2 - Y**2)
ax.plot_wireframe(X, Y, Z, color="#000000")
ax.plot_wireframe(X, Y, -Z, color="#000000")

# гиперболоид
A = 1
B = 1
C = 1.5
X = arange(-5, 5, 0.1)
Y = arange(-5, 5, 0.1)
X, Y = meshgrid(X, Y)
Z = sqrt_a(X**2/A**2 + Y**2/B**2 - 1) / C
ax.plot_wireframe(X, Y, Z, color="#FF0000")
ax.plot_wireframe(X, Y, -Z, color="#FF0000")

show()
