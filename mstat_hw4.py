from math import sqrt

# lesson 4 task1
a = 200
b = 800
print(f"среднее значение: {(a+b) / 2}")
print(f"дисперсия : {(b-a)**2 / 12}\n")

# lesson 4 task2
d = 0.2
a = 0.5
# (b-a)**2 = 12*d
b1 = sqrt(12*d)+a
b2 = -sqrt(12*d)+a
if b1 > a > b2:
    print(f"правая граница: {b1:.6f}")
    print(f"среднее значение: {(a + b1) / 2:.6f}\n")
elif b1 < a < b2:
    print(f"правая граница: {b2:.6f}")
    print(f"среднее значение: {(a + b2) / 2:.6f}\n")
else:
    print("N/A")

# lesson 4 task3
# f(x) = (1 / (4 * sqrt(2*pi))) * (exp(-((x+2)**2) / 32))
print(f"M(X) = {-2};")
print(f"D(X) = {32/2};")
print(f"std(X) = {4}\n")

# lesson 4 task4
m = 174
s = 8
print(f"а) >182| число сигм(+): {(182-m)/s}; P по графику: {1-(1/2+0.68/2):.3f}, по таблице: {1-0.8413:.3f}")
print(f"б) >190| число сигм(+): {(190-m)/s}; P по графику: {1-(1/2+0.954/2):.3f}, по таблице: {1-0.9772:.3f}")
print(f"в) >166,<190| число сигм(-): {(166-m)/s}; число сигм(+): {(190-m)/s}; P по графику: {0.68/2+0.954/2:.3f},"
      f" по таблице: {0.9772-0.1587:.3f}")
print(f"г) >166,<182| число сигм(-): {(166-m)/s}; число сигм(+): {(182-m)/s}; P по графику: {0.68:.3f},"
      f" по таблице: {0.8413-0.1587:.3f}")
print(f"д) >158,<190| число сигм(-): {(158-m)/s}; число сигм(+): {(190-m)/s}; P по графику: {0.954:.3f},"
      f" по таблице: {0.9772-0.0228:.3f}")
print(f"е) <150,>190| число сигм(-): {(150-m)/s}; число сигм(+): {(190-m)/s}; P по графику: {1-(0.9972/2+0.954/2):.3f},"
      f" по таблице: {0.0014+(1-0.9772):.3f}")
print(f"ё) <150,>198| число сигм(-): {(150-m)/s}; число сигм(+): {(198-m)/s}; P по графику: {1-0.9972:.3f},"
      f" по таблице: {0.0014+(1-0.9986):.3f}")
print(f"ж) <166| число сигм(-): {(166-m)/s}; P по графику: {1/2-0.68/2:.3f}, по таблице: {0.1587:.3f}")

# lesson 4 task5
a = 190
m = 178
d = 25
print(f"\nчисло сигм: {(a-m) / sqrt(d)}")

input("\nPress the Enter key for exit.")
