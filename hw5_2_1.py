# сложить вероятности (отн. частоты) для чёт, нечет, zero
# результат при больших n должен стремиться к 1

from random import randint

n = 10000
p = [0.0, 0.0, 0.0]

for _ in range(n):
    if (x := randint(0, 36)) == 0:
        p[0] += 1/n
    elif x % 2 == 0:
        p[1] += 1/n
    else:
        p[2] += 1/n

print(f"P(zero) = {p[0]:.6f}")
print(f"P(even) = {p[1]:.6f}")
print(f"P(odd) = {p[2]:.6f}")
print(f"P(zero+even+odd) = {(p[0] + p[1] + p[2]):.6f}")
