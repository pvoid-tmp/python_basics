# Lesson 5 task 5

from random import random, randint

try:
    with open("L5_task5.txt", "w", encoding="utf-8") as f:
        f.write(' '.join([str(round(random()*10, 4)) for _ in range(randint(3, 9))]))
    with open("L5_task5.txt", "r", encoding="utf-8") as f:
        total = 0.0
        for i in range(len(lst := f.readline().split())):
            total += float(lst[i])
        print(total)
except Exception as e:
    print(e)
