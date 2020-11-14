# Lesson 2 task3 (using dict)

month_nums = {'1': "зима", '2': "зима", '3': "весна", '4': "весна",
              '5': "весна", '6': "лето", '7': "лето", '8': "лето",
              '9': "осень", '10': "осень", '11': "осень", '12': "зима"}
while True:
    month_num = input("Введите номер месяца от 1 до 12 (без нулей спереди) или N для выхода: ")
    if month_num == 'N' or month_num == 'n':
        break
    if month_num in month_nums:
        print(month_nums[month_num])
    else:
        print(f"{month_num:s} не является номером месяца")
