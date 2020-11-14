# Lesson2 task 6
from typing import Dict, Union

item_catalogue = []
item_card_fields = dict()

num_of_record = 1
proceed = 'Y'
while proceed == 'Y' or proceed == 'y':
    name = input("название: ")
    price = input("цена: ")
    # не стал городить проверку через исключение
    float(price)
    qty = input("количество: ")
    if qty.isdigit():
        qty = int(qty)
    UoM = input("единица измерения: ")
    item_card_fields = {"название": name, "цена": price, "количество": qty, "ед": UoM}
    item_card = (num_of_record, item_card_fields)
    item_catalogue.append(item_card)
    proceed = input("Еще один товар (введите Y, если да)? ")

card_fields_keys = []
analytics_lst = []
analytics = dict()
card_fields_keys.extend(item_card_fields.keys())

for i in range(len(item_card_fields)):
    s = card_fields_keys[i]

    # делаю список сетов, т.к. в задании в выводе только уникальные значения
    analytics_lst.append(set())

    for j in range(len(item_catalogue)):
        analytics_lst[i].add(item_catalogue[j][1][s])
    analytics.update({s: analytics_lst[i]})
for i in range(len(item_card_fields)):
    s = card_fields_keys[i]
    print(f"{s:s}: {analytics[s]}")
