import numpy as np

k, n = 0, 10000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k += 1
print(k, n, k/n)

# по формуле
k, n = 2, 4
print(np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n-k)) * (1 / 2**n))

print()

# из 3 испытаний 0 успехов
k, n = 0, 10000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
x = a + b + c
for i in range(0, n):
    if x[i] == 0:
        k += 1
print(k, n, k/n)
# по формуле
k, n = 0, 3
print(np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n-k)) * (1 / 2**n))
