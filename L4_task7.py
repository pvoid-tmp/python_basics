# Lesson 4 task 7

def my_factorial(n):
    f = 1
    for r in range(1, n+1):
        f *= r
    return f


def fact(n):
    for f in range(1, n+1):
        yield my_factorial(f)


# main
while True:
    num = input("\nn: (Q for exit): ")
    if num.upper() == 'Q':
        break
    try:
        g = fact(int(num))
        for el in g:
            print(el)
    except ValueError as e:
        print(e)
        continue
