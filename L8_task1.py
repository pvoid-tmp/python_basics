# Lesson 8 task 1

class MyDate:

    def __init__(self, date_s):
        self.date_s = date_s

    @classmethod
    def get_date(cls, obj):
        return tuple([int(el) for el in obj.date_s.split("-")])

    @staticmethod
    def is_my_date(my_obj):
        if len(date_n := MyDate.get_date(my_obj)) != 3:
            return False
        if (year := date_n[2]) not in range(1, 10000):  # год от 1 до 9999
            return False
        if (month := date_n[1]) not in range(1, 12+1):  # месяц
            return False
        if (day := date_n[0]) not in range(1, 31+1):  # 31 день
            return False
        if month in (4, 6, 9, 11) and day > 30:  # 30 дней
            return False
        if month == 2 and day > 29:  # февраль
            return False
        if month == 2 and day == 29:  # 29 февраля
            if year % 4 != 0:
                return False
            if year > 1582 and year % 100 == 0 and year % 200 != 0:  # после введения григориаского календаря
                return False
        return True


# main
for s in ("27-11-2020", "1-1-1", "29-02-1300", "29-02-1900", "29-02-2000", "31-12-9999", "01-01-10000", "27", "27-11"):
    d = MyDate(s)
    if MyDate.is_my_date(d):
        print(MyDate.get_date(d))
    else:
        print(f"{d.date_s} не является корректной датой")
