# Lesson 2 tak 4

s = input("Введите строку\n: ")
s_lst = s.split()
for i in range(len(s_lst)):
    print(f"{i+1}: {s_lst[i]:.10s}")
