# Первый, с декоратором @classmethod, должен извлекать число, месяц,
# # год и преобразовывать их тип к типу «Число».
# def take_off(par):
#     qqq = par.split('-')
#     print(qqq)
#
#
#
#
#
# take_off('30-01-2020')
class Date(object):

    def __init__(self, day=None, month=None, year=None):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f' ===== датаs == {self.day}, {self.month}, {self.year}'

    @classmethod
    def take_off(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)

        return f'---{date1}-'

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


data0 = Date(3, 1, 2012)
print(data0)
print(Date.take_off('30-01-2020'))
print(Date.is_date_valid('30-01-2020'))
