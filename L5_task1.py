# Lesson 5 task 1

try:
    with open("L5_task1.txt", "+w", encoding="utf-8") as f:
        while line := input(": "):
            f.write(line + '\n')
        f.seek(0)
        for line in f:
            print(line, end="")
except Exception as e:
    print(e)
