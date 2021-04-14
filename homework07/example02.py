from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calculate(self):
        pass


class Suite(Clothes):
    height: int

    def __init__(self, height):
        self.height = height

    @property
    def calculate(self):
        return 2 * self.height + 3


class Coat(Clothes):
    size: int

    def __init__(self, size):
        self.size = size

    @property
    def calculate(self):
        return self.size / 6.5 + 0.5


my_suite = Suite(10)
my_coat = Coat(50)

print(my_suite.calculate)
print(my_coat.calculate)