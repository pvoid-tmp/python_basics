# Lesson 2 task3 (using list)

month_nums = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
months = ["зима", "весна", "лето", "осень"]
while True:
    month_num = input("Введите номер месяца от 1 до 12 (без нулей спереди) или N для выхода: ")
    if month_num == 'N' or month_num == 'n':
        break
    if month_num in month_nums:
        month_num = int(month_num)
        if month_num == 12:
            # "move" December to the beginning of winter
            month_num = 0
        print(months[month_num // 3])
    else:
        print(f"{month_num:s} не является номером месяца")
