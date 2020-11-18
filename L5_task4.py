# Lesson 5 task 4
# файл "text_4.txt" из материалов урока

my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

try:
    with open("text_4.txt", "r", encoding="utf-8") as f_source, open("RU_4.txt", "w", encoding="utf-8") as f_target:
        n_lines = sum(1 for _ in f_source)
        f_source.seek(0)
        eol = '\n'
        for i in range(n_lines):
            line = [el for el in f_source.readline().split()]
            line[0] = my_dict.get(line[0])
            if i == n_lines-1:
                eol = ""  # последняя строка без EOL, как в исходном файле
            f_target.write(' '.join(line) + eol)
except Exception as e:
    print(e)
