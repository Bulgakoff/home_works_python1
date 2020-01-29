'''# 2.	Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.'''
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes:
    def __init__(self, param_f):
        self.fc = param_f

    @abstractmethod
    def fabric_co(self):
        pass

    @property
    def fc(self):
        return self._fc

    @fc.setter
    def fc(self, prs):
        if prs < 20:
            self._fc = 20
            print(f'Аргумент-атрибут {prs} введенн ниже нормы --> нижнее значение внесем {self._fc} ')

        elif prs >= 80:
            self._fc = 79
            print(f'Аргумент-атрибут {prs} введенн выше нормы --> верх значения {self._fc}')

        else:
            self._fc = prs

    def __str__(self):
        return f'Аргумент-атрибут {self._fc}'


class Coat(Clothes):
    def fabric_co(self):
        print(f'расход ткани по пальто == {int(self._fc / 6.5 + 0.5)}')


class Suit(Clothes):
    def fabric_co(self):
        print(f'расход костюму по пальто == {2 * self._fc + 0.3}')
    @property
    def fc(self):
        return self._fc

    @fc.setter
    def fc(self, prs):
        if prs < 50:
            self._fc = 50
            print(f'Аргумент-атрибут {prs} введенн ниже нормы --> нижнее значение внесем {self._fc} ')

        elif prs >= 200:
            self._fc = 199
            print(f'Аргумент-атрибут {prs} введенн выше нормы --> верх значения {self._fc}')

        else:
            self._fc = prs

coat = Coat(10)
coat.fabric_co()
print(coat)
suit = Suit(40)
suit.fabric_co()
print(suit)