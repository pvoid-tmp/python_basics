# Lesson 1 task 1
# no input data control
# Запрашивает возраст, пол, профессиональную область
# и выдает соотвествующий показатель летальности для COVID-19
# ! учебный пример, не предназначено для практического использования
# источник статистики по летальности: https://habr.com/ru/post/487366/

while True:
    gender = input("Введите пол (Ж/М); или любое другое значение для выхода: ")
    if gender != 'Ж' and gender != 'М':
        break
    age = int(input("Возраст в годах: "))
    if age < 0:
        print("Ошибка: требуется неотрицательное значение")
        continue

    print("Профессиональная область")
    print("""    1 Промышленность
    2 Сельское хозяйство
    3 Медицина
    4 Пенсионер
    5 (или любое значение, кроме 1-4) Другое""")
    occupation = input(": ")

    if gender == 'Ж':
        gender_factor = 0.756
    else:
        gender_factor = 1.244

    if occupation == '1':
        occupation_factor = 0.372
        occupation = "Промышленность"
    elif occupation == '2':
        occupation = "Сельское хозяйство"
        occupation_factor = 0.745
    elif occupation == '3':
        occupation = "Медицина"
        occupation_factor = 0.160
    elif occupation == '4':
        occupation_factor = 2.713
        occupation = "Пенсионер"
    else:
        occupation_factor = 1.011
        occupation = "Другое"

    if age < 10:
        mortality = 0.0
    elif age < 40:
        mortality = gender_factor * occupation_factor * 0.2
    elif age < 50:
        mortality = gender_factor * occupation_factor * 0.4
    elif age < 60:
        mortality = gender_factor * occupation_factor * 1.3
    elif age < 70:
        mortality = gender_factor * occupation_factor * 3.6
    elif age < 80:
        mortality = gender_factor * occupation_factor * 8.0
    else:
        mortality = gender_factor * occupation_factor * 14.8

    print(f"Пол: {gender:s}; Возраст: {age:d}; Проф. группа: {occupation:s}")
    print(f"Летальность: {mortality:.2f}%\n")
