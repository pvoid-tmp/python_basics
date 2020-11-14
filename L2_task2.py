# Lesson 2 task 2

my_lst = []
while True:
    s = input("Input something for my list and just press the Enter key to complete it\n: ")
    if s == "":
        break
    my_lst.append(s)
print(my_lst)

i = 0
while i < len(my_lst) - len(my_lst) % 2:
    s = my_lst[i]
    my_lst[i] = my_lst[i+1]
    my_lst[i+1] = s
    i += 2
print(my_lst)
