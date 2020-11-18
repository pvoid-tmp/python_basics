# Lesson 5 task 6
# файл "text_6.txt" из материалов урока

# x_num()
""" извлекает числа из такого, как в задании, вида строк:) и возвращает их сумму  """


def x_num(s):
    if s == '-':
        return 0
    return int(s[:s.index('(')])


try:
    with open("text_6.txt", "r", encoding="utf-8") as f:
        print({
            el.split()[0][:len(el.split()[0]) - 1]: x_num(el.split()[1]) + x_num(el.split()[2]) + x_num(el.split()[3])
            for el in f.readlines()})
except Exception as e:
    print(e)
