# Lesson 5 task 3
# файл "text_3.txt" из материалов урока

from functools import reduce

try:
    with open("text_3.txt", "r", encoding="utf-8") as f:
        lst = [[el.split()[0], float(el.split()[1])] for el in f.readlines()]
        print("оклад < 20 k:", [el[0] for el in lst if el[1] < 20000.0])
        print("ср. оклад по всем:", reduce((lambda a, b: a + b), [el[1] for el in lst]) / len(lst))
except Exception as e:
    print(e)
