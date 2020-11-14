# Lesson 3 task 5

grand_total = 0.0
continue_flag = True
while continue_flag:
    line_total = 0
    input_line = input("Введите строку чисел, разделенных пробелами; Q для выхода\n: ").split()
    for i in range(len(input_line)):
        try:
            line_total += float(input_line[i])
        except ValueError:
            if input_line[i].upper() == 'Q':
                continue_flag = False
                break  # игнорируем числа после Q|q
            else:
                print(f"Недопустимое значение: {input_line[i]:s}; можно вводить числа и символ Q для выхода")
                continue  # продолжаем собирать числа (или ждать Q) после недопустимого значения
    grand_total += line_total
    print(f"Итого по строке: {line_total:.2f}; ВСЕГО: {grand_total:.2f}")
