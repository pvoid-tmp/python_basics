# Lesson 7 task 3

class Cell:

    def __init__(self, bins):
        self.bins = int(bins)
        if self.bins < 0:
            self.bins = 0

    def __add__(self, other):
        return Cell(self.bins + other.bins)

    def __sub__(self, other):
        r = self.bins - other.bins
        # по заданию при отрицательной разности требовалось
        # не выполнять операцию и вывести соотв. сообщение, например, так:
        if r < 0:
            print(f"операция Cell({self.bins}) - Cell({other.bins}) отменяется")
            return self
        return Cell(r)
        # очень не нравится print() в перегруженном операторе,
        # я бы обработал это так:
        # return Cell(r) if r > 0 else Cell(0)  # отрицательный результат заменяется на нулевой

    def __mul__(self, other):
        return Cell(self.bins * other.bins)

    def __truediv__(self, other):
        if other.bins == 0:  # деление на 0 в задании не предусмотрено; не делаем с делимым ничего
            return self
        return Cell(int(round(self.bins / other.bins)))

    def make_order(self, by_row):
        lst = []
        if (by_row := int(by_row)) == 0:
            return '*' * self.bins  # если задано 0 ячеек в ряду, выводить одной строкой
        for _ in range(self.bins // by_row):
            lst.append('*' * by_row)
        lst.append('*' * (self.bins % by_row))
        return '\n'.join(lst)


# main
# print((Cell(23) + Cell(5) + Cell(3)).make_order(10))
# print((Cell(23) - Cell(5) - Cell(3)).make_order(10))
# print((Cell(6) - Cell(8) + Cell(5)).make_order(10))
# print((Cell(2) * Cell(5) * Cell(3)).make_order(10))
# print((Cell(23) / Cell(5) / Cell(3)).make_order(10))
# print((Cell(23) / Cell(0) / Cell(3)).make_order(10))
print((Cell(23) + Cell(5) - Cell(2) * Cell(3) / Cell(2)).make_order(10))  # = 25
