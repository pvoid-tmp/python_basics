# Lesson 1 task 5
# no input data control

while True:
    revenue = input("Ввведите значение выручки или N для выхода: ")
    if revenue == 'N' or revenue == 'n':
        break
    revenue = float(revenue)
    expenses = float(input("Ввведите значение издержек: "))
    if revenue < 0.0 or expenses < 0.0:
        print("Ошибка: отрицательные значения недопустимы")
        continue
    balance = revenue - expenses
    if balance > 0:
        print(f"Прибыль: {balance:.2f}")
        print(f"Рентабельность: {balance/revenue:.2f}")

        # в общем случае численность сотрудников не обязательно целое число
        # например, при использовании full-time equivalent
        staff = float(input("Введите численность сотрудников: "))
        if staff > 0:
            print(f"Прибыль на 1 сотрудника: {balance/staff:.2f}")
        else:
            print("Прибыль на нулевое/отрицательное число сотрудников не может быть рассчитана")

    elif balance < 0:
        print(f"Убытки: {-balance:.2f}")
    else:
        print("Прибыль и убытки: 0.00")
