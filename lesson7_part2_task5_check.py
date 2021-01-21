# проверка решения из текстового файла
import numpy as np

a = np.array([[1, 2, -1], [8, -5, 2]])
b = np.array([1, 12])
print(np.linalg.lstsq(a, b, rcond=None))
