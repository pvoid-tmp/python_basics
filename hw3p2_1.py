# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt


def plot_cos(x, k, a, b, c="#000000"):
    plt.plot(x, k * np.cos(x - a) + b, color=c)


def main():
    x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    plt.plot(x, x * 0, color="#cccccc")

    plot_cos(x, 1, 0, 0)
    plot_cos(x, 0.5, 0, 0, "#ff0000")
    plot_cos(x, 1, np.pi / 2, 0, "#00ff00")
    plot_cos(x, 1, 0, 0.5, "#0000ff")
    plot_cos(x, 0.5, np.pi / 2, 0, "#ffff00")
    plot_cos(x, 0.5, 0, 0.5, "#ff00ff")
    plot_cos(x, 1, np.pi / 2, 0.5, "#00ffff")

    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('tight')
    plt.show()


main()
