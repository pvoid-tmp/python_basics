# Lesson 6 task 1

import colorama
from colorama import Back, Style
from time import sleep


# Светофор на цветной псевдографике, расположенный горизонтально (з)(ж)(к)
# протестировано в cmd.exe Windows 10-64, а также в PyCharm Community 2020.2
# в Python IDLE 3.9.0 НЕ работает нормально: Esc-последовательности не отрабатывают
class TrafficLight:
    __color = Back.RED

    def __init__(self):
        colorama.init()

    # __light_up()
    # включает один сигнал цвета color в позиции position на время duration,
    # "гасит" все остальные сигналы
    # duration только от 0 до 9 (чтобы не сломать псевдографику), проверок не стал громоздить
    def __light_up(self, color, duration, position):
        self.__color = color
        for i in range(duration, 0, -1):
            print(Style.RESET_ALL + "( )" * (int(position) - 1), end="")
            print(self.__color + "(" + str(i) + ")", end="")
            print(Style.RESET_ALL + "( )" * (3 - int(position)), end="")
            sleep(1)
            print('\b' * 9, end="")  # "вернуться" на первую позицию

    # running()
    # прогоняет number_of_cycles циклов "зелёный-жёлтый-красный"
    # порядок переключения из задания нарушен осознанно
    def running(self, number_of_cycles):
        for _ in range(number_of_cycles):
            self.__light_up(Back.GREEN, 9, 1)
            self.__light_up(Back.YELLOW, 2, 2)
            self.__light_up(Back.RED, 7, 3)
        print(Style.RESET_ALL + "( )" * 3)  # "погасить" все сигналы


# main
print()
tl = TrafficLight()
tl.running(3)
