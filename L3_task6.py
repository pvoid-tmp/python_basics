# Lesson 3 task 6

# int_func(str)
""" принимает слово из маленьких латинских букв
    и возвращает его же, но с прописной первой буквой
"""


def int_func(word):
    for i in range(len(word)):
        if ord(word[i]) not in range(ord('a'), ord('z')+1):
            return '1'
    return word.capitalize()


# main
while True:
    input_line = input("Введите произвольную строку или символ Q для выхода\n: ")
    if input_line.upper() == 'Q':
        break
    out_list = input_line.split()
    for i in range(len(out_list)):
        out_list[i] = int_func(out_list[i])
    for i in range(out_list.count('1')):
        out_list.remove('1')
    print(' '.join(out_list))
