import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([2, 5, 11])

q, r = np.linalg.qr(a)
print(q)
print(r)
r1 = r[:2, :2]
print(r1)
b1 = np.dot(q.T, b)[:2]
print(b1)
x = np.append(np.linalg.solve(r1, b1), 0)
print(x)
