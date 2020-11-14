# Lesson 3 task 4

# my_func()
"""принимает действительное положительное число x и целое отрицательное число y,
    выполнет возведение числа x в степень y и возвращает результат как float
    при ошибках возвращает свои собственные строковые "коды"
"""


def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        return "ve"
    if x <= 0.0:
        return "-x"
    if y >= 0:
        return "+y"
    # return round(x ** y, 6)
    res = 1.0
    while y < 0:
        res *= x
        y += 1
    return round(1 / res, 6)


while True:
    num1 = input("Введите положительное вещественное число или Q для выхода: ")
    if num1.upper() == 'Q':
        break
    num2 = input("Введите целое отрицательное число: ")
    power = my_func(num1, num2)
    if power == "ve" or power == "-x" or power == "+y":
        print("Введены неверные данные\n")
        continue
    else:
        print(f"{num1} ** {num2} = {power}")
