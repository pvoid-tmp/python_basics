import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[12, 2, 1]])
print(f"det = {np.linalg.det(a)}")
c = np.concatenate((a, b.T), axis=1)
print(c)
ra = np.linalg.matrix_rank(a)
rc = np.linalg.matrix_rank(c)
print(f"ранг A: {ra}, ранг C: {rc}")
if ra != rc:
    print("0 решений")
elif ra == len(a[0]):
    print("1 решение")
else:
    print("бесконечное множество решений")

# понизить ранг C, заменив поледний столбец на копию 1-го столбца
b[0] = a.T[0]
c = np.concatenate((a, b.T), axis=1)
print(c)
ra = np.linalg.matrix_rank(a)
rc = np.linalg.matrix_rank(c)
print(f"ранг A: {ra}, ранг C: {rc}")
if ra != rc:
    print("0 решений")
elif ra == len(a[0]):
    print("1 решение")
else:
    print("бесконечное множество решений")
# решение системы - в текстовом файле
