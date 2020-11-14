# Lesson 3 task 1

# my_div
"""делит a на b; контроль вохдных значений - на вызывающем блоке"""


def my_div(a, b):
    return a / b


while True:
    n1 = input("Введите делимое или Q для выхода: ")
    if n1.upper() == 'Q':
        break
    n2 = input("Делитель: ")
    try:
        print(f"{my_div(float(n1), float(n2)):.3f}")
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)


