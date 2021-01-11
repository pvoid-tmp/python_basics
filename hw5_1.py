from random import randint

while True:
    if input("Quit (Q) or continue (any)? ").upper() == 'Q':
        break
    print(f"Result: {randint(0, 36):2d}")
