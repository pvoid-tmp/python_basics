# Lesson 5 task 2
# файл "L5_task2.txt" загрузил в git

try:
    with open("L5_task2.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        n_lines = len(lines)
        print(f"всего строк: {n_lines:d}")
        for i in range(n_lines):
            print(f"строка {i+1:d}: {len(lines[i].split()):d} слов")
except Exception as e:
    print(e)
