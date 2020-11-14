# Lesson 1 task 3
# no input data control

while True:
    n = input("Enter a number or N to exit: ")
    if n == 'N' or n == 'n':
        break
    if int(n) < 0:
        print("Error: negative value")
        continue
    print(f"{int(n):d} + {int(n+n):d} + {int(n+n+n):d} = {int(n) + int(n+n) + int(n+n+n):d}")
