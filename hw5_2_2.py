# %matplotlib inline

import numpy as np
import matplotlib.pyplot as plt

samplings = 10
numbers = 10
a = []

for _ in range(samplings):
    a.append(sum(np.random.rand(numbers)))

num_bins = 5
n, bins, patches = plt.hist(a, num_bins)
plt.xlabel("sum")
plt.ylabel('P')
plt.show()
