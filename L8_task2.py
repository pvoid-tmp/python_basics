# Lesson 8 task 2

# проверка на корректность входных данных - функция из задачи 3
# my_isfloat() является ли аргумент вещественным числом? экспоненциальная форма не поддерживается
def my_isfloat(s):
    for c in s:
        if c not in "-.0123456789":
            return False
    if s.count('-') > 1 or s.count('-') == 1 and s.index('-') > 0:
        return False
    if s.count('.') > 1 or s == "." or s == "-" or s == "-.":
        return False
    return True


class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg


while True:
    a = input("Делимое (Q для выхода): ")
    if a.upper() == 'Q':
        break
    b = input("Делитель: ")
    try:
        if not my_isfloat(a):
            raise MyException(f"{a} is not a number")
        if not my_isfloat(b):
            raise MyException(f"{b} is not a number")
        if (b := float(b)) == 0.0:
            raise MyException("Division by 0")
        a = float(a)
        print(f"{a} / {b} = {round(a / b, 6)}")
    except MyException as e:
        print(e)
