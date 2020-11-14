# Lesson 4 task 2

from random import randint

# source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# source_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

source_list = [el*0 + randint(0, 1000) for el in range(0, randint(0, 40))]
print(source_list)

print([el for i, el in enumerate(source_list) if i > 0 and source_list[i] > source_list[i-1]])
