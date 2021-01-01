# Пересекает ли игла линию?
# Предполагается, что ось X совпадает с одной из линеек
# Абсцисса нижней точки в этом случае не нужна
# Касание линейки и нахождение на линейке не считаются пересечением

import numpy as np


def is_intersect(a, y, b, alpha):
    # найти одрдинату ближайшей к нижней точке (сверху) линейки:
    r = 0
    if y >= 0:
        while r < y:
            r += a
    else:
        while r > y:
            r -= a
        r += a
    # ордината нижней точки плюс длина проекции иглы на ось Y больше ординаты до ближайшей линейки?
    if y + b * np.sin(alpha) > r:
        return True
    return False


# main
print(is_intersect(2, 0.5, 1, np.pi/4))
print(is_intersect(2, 0.5, 10, np.pi/4))
print(is_intersect(2, -1, 1, np.pi/4))
print(is_intersect(2, -1, 10, np.pi/4))
