# 3.	Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы
# методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
# равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
# количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки
# определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр
# класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.
class Cell:
    def __init__(self, param):
        self.xxx = param

    def __add__(self, other):
        return Cell(self.xxx + other.xxx)

    def __sub__(self, other):  # разность количества ячеек двух клеток больше нуля, иначе сообщение.
        sub_c = self.xxx - other.xxx
        if sub_c < 0:
            print('первая клетка меньше второй - ошибка')
        else:
            return Cell(sub_c)

    def __mul__(self, other):
        return Cell(self.xxx * other.xxx)

    def __truediv__(self, other):
        div_c = round((self.xxx / other.xxx), 2)
        return Cell(div_c)

    def make_order(self, p_row):
        if self.xxx < p_row:
            print('Клетка неделима')
        else:
            www = self.xxx // p_row
            rrr = self.xxx % p_row
            ddd = '*' * rrr
            aaa = '*' * 5 + '\n'
            sss = aaa * www
            xxx = sss + ddd
            return xxx

    def __str__(self):
        return f' == {self.xxx} ячеек'


cell1 = Cell(12)
cell2 = Cell(2)
cell3 = Cell(5)
cell4 = Cell(2)
cell5 = Cell(13)

print(f'клетка 1 {cell1}')
print(f'клетка 2 {cell2}')
print(f'клетка 3 {cell3}')
pl_cells = cell1 + cell2
print(f'сложение клеток --- {pl_cells} ')
sub_cells = pl_cells - cell3
print(f'вычитание клеток --- {sub_cells} ')
mul_cells = pl_cells * cell4
print(f'умножение  клеток --- {mul_cells} ')
mul_cells = pl_cells / cell5
print(f'деление  клеток --- {mul_cells}  ')
print(f'клетка с количеством ячеек {cell1} \n{cell1.make_order(5)}')
print(f'клетка с количеством ячеек {cell5} \n{cell5.make_order(5)}')