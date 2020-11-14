# Lesson 3 task 2

# personal_data
""" принимает несколько параметров, описывающих данные пользователя
    возвращает данные о пользователе одной строкой
"""


def personal_data(name, last_name, year_of_birth, city, email, phone):
    return name + ' ' + last_name + ", " + year_of_birth + ", " + \
           city + ", " + email + ", " + phone


while True:
    i_last_name = input("Фамилия (пустое значение для выхода): ")
    if i_last_name == "":
        break
    i_name = input("Имя: ")
    i_year_of_birth = input("Год рождения: ")
    print(personal_data(name=i_name, last_name=i_last_name, year_of_birth=i_year_of_birth,
                        city=input("Город проживания: "), phone=input("Телефон: "),
                        email=input("Адрес электронной почты: ")))
