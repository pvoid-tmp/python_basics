# Lesson 8 task 3

class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg


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


lst = []
while True:
    inp_s = input("Введите число или числа через пробел (Q для выхода): ")
    if inp_s.upper() == 'Q':
        break
    for el in inp_s.split():
        try:
            if not my_isfloat(el):
                raise MyException(f"{el} is not a number")
            lst.append(float(el))
        except MyException as e:
            print(e)
print(lst)
