##6.Реализовать класс Stationery (канцелярская принадлежность).
## Определить в нем атрибут title (название) и метод draw (отрисовка).
## Метод выводит сообщение “Запуск отрисовки.”
## Создать три дочерних класса Pen (ручка),Pencil (карандаш), Handle (маркер).
## В каждом из классов реализовать переопределение метода draw.
## Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки ')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки простым карандашем')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки шариковой ручкой')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером ')


pen = Pen('Карандаш')
pen.draw()
pencil = Pencil('Ручка')
pencil.draw()
handle = Handle('Маркер')
handle.draw()
