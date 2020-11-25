# Lesson 7 task 2

from abc import ABC, abstractmethod
from math import ceil


class Apparel(ABC):

    @abstractmethod
    def consumption(self):
        pass


class Coat(Apparel):

    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 32:
            self.__size = 32
        else:
            self.__size = size

    @property
    def consumption(self):
        return ceil(float(self.size) / 2 / 6.5 + 0.5)


class Suit(Apparel):

    def __init__(self, height):
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 120:
            self.__height = 120
        else:
            self.__height = height

    @property
    def consumption(self):
        return ceil(float(self.height) / 100 * 2.0 + 0.3)


# main
coat = Coat(22)
print(f"Fabric consumption for size {coat.size} coat: {coat.consumption} m")

suit = Suit(164)
print(f"Fabric consumption for {suit.height} cm suit: {suit.consumption} m")
