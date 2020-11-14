# Lesson 1 task 4
# no input data control

while True:
    n = input("Enter a positive number or N to exit: ")
    if n == 'N' or n == 'n':
        break
    n = int(n)
    if n < 0:
        print("Error: negative value")
        continue
    max_digit = 0
    while n > 0:
        current_num = n % 10
        if current_num > max_digit:
            max_digit = current_num
        n //= 10
    print(f"Highest digit: {max_digit:d}")
