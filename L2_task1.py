# Lesson 2 Task 1

my_bytes = b"text1"
my_bytearray = bytearray(b"text2")

# jokes
e = Exception(0)
t = int

my_lst = [0, 2.0, 0 + 3 + 0j, 's4', [5, 6.0], ((7 + 0j), 's8'), {9, 10.0},
          {(11 + 0j): "s12"}, True, my_bytes, my_bytearray, None, e, t]
for i in range(len(my_lst)):
    print(my_lst[i], type(my_lst[i]))

input("\n\nPress the Enter key to exit.")