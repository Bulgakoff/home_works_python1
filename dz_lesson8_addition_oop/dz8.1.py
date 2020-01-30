# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год».

# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число».
#
# Второй, с декоратором @staticmethod
# , должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class Data:
    def __init__(self, day=None, month=None, year=None):
        self.da = day
        self.mo = month
        self.ye = year

    def __str__(self):
        return f' =====текущая дата == >>>> {self.da}--{self.mo}--{self.ye}'

    @classmethod
    def take_off_str_to_int(cls, str_data):
        d, m, y = map(int, str_data.split('-'))
        print(f'>>> введенная списком  для проверки {cls(d, m, y)}')

    @staticmethod
    def valid_num(d_for_valid):
        d, m, y = map(int, d_for_valid.split('-'))
        if 0 < d <= 31:
            print(f'день {d} норма')
        else:
            print(f'вы вышли за рамки day == {d}')
        if 0 < m <= 12:
            print(f'месяц {m} норма')
        else:
            print(f'вы вышли за рамки month == {m}')
        if 2000 < y <= 2020:
            print(f'год  {y} норма')
        else:
            print(f'вы вышли за рамки диапазони лет == {y}')


dates = '32-13-2021'
data1 = Data(30, 1, 2020)
print(data1)
Data.take_off_str_to_int(dates)  # ghbyn
Data.valid_num(dates)  # ghbyn
