# Lesson 4 task 6

# формирует словарь; ключи (int) создаются с помощью itertools.count()
# значения (str) собираются из списка строк с помощью  itertools.cycle()

from itertools import count, cycle, islice

my_dict = dict()
for n in islice(count(5), 6):
    s = ""
    for el in islice(cycle(["s1", "s2"]), 3):
        s += el
    my_dict.update({n: s})
print(my_dict)
