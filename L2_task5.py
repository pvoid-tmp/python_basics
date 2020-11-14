# Lesson 2 task 5

my_lst = [7, 5, 3, 3, 2]
while True:
    new_item = input("Введите натуральное число или N для выхода: ")
    if new_item == 'N' or new_item == 'n':
        break
    if new_item.isnumeric() and int(new_item) != 0:
        new_item = int(new_item)
        i = 0
        while i < len(my_lst) and new_item <= my_lst[i]:
            i += 1
        my_lst.insert(i, new_item)
        print(my_lst)
    else:
        print(f"{new_item} не является натуральным числом")
        continue
