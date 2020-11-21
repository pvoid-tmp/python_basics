# Lesson 6 task 5
# проверки типов данных отсуствуют

class Stationery:

    def __init__(self):
        self.title = "Запуск отрисовки"

    def draw(self):
        print(f"{self.title}")


class Pen(Stationery):

    def draw(self):
        print(f"{self.title}: Ручка")


class Pencil(Stationery):

    def draw(self):
        print(f"{self.title}: Карандаш")


class Handle(Stationery):

    def draw(self):
        print(f"{self.title}: Маркер")


# main
t = Pen()
t.draw()
t = Pencil()
t.draw()
t = Handle()
t.draw()
