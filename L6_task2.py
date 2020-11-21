# Lesson 6 task 2
# проверки типов данных отсуствуют

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self, thickness):
        return int(self._width) * int(self._length) * 25 * int(thickness)


# main
r = Road(20, 5000)
print(f"Масса асфальта: {r.weight(5) // 1000} тонн")
