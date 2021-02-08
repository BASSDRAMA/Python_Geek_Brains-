from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param1):
        self.name = param1

    @property
    def consum(self):
        return f'Всего ткани затрачено: {self.name / 6.5 + 0.5 + 2 * self.name + 0.3 :.2f}'

    @abstractmethod
    def abstract(self):
        return 'wow'


class Coat(Clothes):
    def consum(self):
        return f'Для пошива пальто нужно: {self.name / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        return 'wowowow'


class Suit(Clothes):
    def consum(self):
        return f'Для костюма нужно: {2 * self.name + 0.3 :.2f} ткани'

    def abstract(self):
        pass


coat = Coat(500)
suit = Suit(450)

print(coat.consum())
print(suit.consum())
print(coat.abstract())