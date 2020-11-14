# Lesson 3 task 3

# my_func()
"""принимает три позиционных аргумента,
    возвращает сумму наибольших двух аргументов,
    округлённую до трёх знаков;
    контроль вохдных значений - на вызывающем блоке
"""


def my_func(n1, n2, n3):
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    return round(n1 + n2 + n3 - min(n1, n2, n3), 3)


while True:
    num1 = input("число #1 или Q для выхода: ")
    if num1.upper() == 'Q':
        break
    num2 = input("число #2: ")
    num3 = input("число #3: ")
    try:
        print(my_func(num1, num2, num3))
    except ValueError as e:
        print(e)
