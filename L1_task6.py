# Lesson 1 task 6
# no input data control

while True:
    a = input("Введите результат первого дня или N для выхода: ")
    if a == 'N' or a == 'n':
        break
    b = float(input("Введите целевой результат:"))
    a = float(a)
    if a <= 0 or b <= 0:
        print("Ошибка: требуются положительные значения")
        continue
    days = 1
    while a < b:
        print(f"День {days:d}: {a:.2f}")
        a *= 1.1
        days += 1
    print(f"День {days:d}: {a:.2f} - целевой реультат {b:.2f} достигнут")
