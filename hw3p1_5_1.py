# %matplotlib inline
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)

X = arange(-5, 5, 0.5)
Y = arange(-5, 5, 0.5)
X, Y = meshgrid(X, Y)
Z = -.4*X - .6*Y - 11.8
ax.plot_surface(X, Y, Z, color="blue")
Z = -.4*X - .6*Y
ax.plot_wireframe(X, Y, Z, color="green")
ax.scatter(0, 0, 0, 'z', 20, color="red")

show()
