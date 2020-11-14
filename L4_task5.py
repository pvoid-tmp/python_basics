# Lesson 4 task 5

from functools import reduce


# просто умножение без контроля аргументов
def my_mul(a, b):
    return a * b


print(reduce(my_mul, [el for el in range(100, 1000+1) if el % 2 == 0]))
