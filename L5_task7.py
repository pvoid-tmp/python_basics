# Lesson 5 task 7
# файл "text_7.txt" из материалов урока

from functools import reduce
import json

try:
    with open("text_7.txt", "r", encoding="utf-8") as f_text:
        my_dict = {}
        n_lines = sum(1 for _ in f_text)
        f_text.seek(0)
        for _ in range(n_lines):
            line = [el for el in f_text.readline().split()]
            my_dict.update({line[0]: int(line[2]) - int(line[3])})
        profit = round(reduce((lambda a, b: a + b), tmp := [el for el in my_dict.values() if el > 0]) / len(tmp), 2)
        print(out_list := ([my_dict, {"average_profit": profit}]))
    with open("text7.json", "w", encoding="utf-8") as f_json:
        json.dump(out_list, f_json, indent=4, ensure_ascii=False)
except Exception as e:
    print(e)
