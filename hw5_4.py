import itertools
import math

print("сочетания из 3 по 2")
for p in itertools.combinations("XYZ", 2):
    print(p)

print("\nразмещения из 3 по 2")
for p in itertools.permutations([0, 1, 2], 2):
    print(p)

print("\nперестановки из 2")
for p in itertools.permutations((math.pi, math.e), 2):
    print(p)
