# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и
# передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
class Departments:
    def __init__(self, dep_name):
        self.dep_name = dep_name

    def __str__(self):
        return f' {self.dep_name}'


class Stock(Departments):
    def __init__(self, dep_name):
        super().__init__(dep_name)
        self.equ_stock = {}

    def from_stock_to_office(self, equipments, depart, cсс):
        depart.to_get(equipments, cсс)

    def into_stock(self, equipments, count):
        self.equ_stock[equipments] = count


class Office_dep(Departments):
    def __init__(self, dep_name):
        super().__init__(dep_name)
        self.equipments = {}

    def to_get(self, equ, count):
        self.equipments[equ] = count

    def from_offic_to_stock(self, equipm, stock, count):
        stock.into_stock(equipm, count)


class Office_equ:
    def __init__(self, name_eq):
        self.name_eq = name_eq

    def lst_equ(self):
        return self.name_eq


class Printer(Office_equ):
    def pr_ter(self):
        print('вывод на печать ')


class Scanner(Office_equ):
    def sc_sc(self):
        print('сканирует документ ')


class Copier(Office_equ):
    def co_py(self):
        print('копирует документ ')


p = Printer("Printer")
c = Copier('ксерокс')
s = Scanner('Scanner')
stock = Stock('Stock office equipment')
print(stock)
# ///////////////////////////////////
bug = Office_dep('Бухгалтерия')
office_sell = Office_dep('офис продаж')
logistic = Office_dep('Логистика')
print(bug, office_sell, logistic)
# /////////////////////////////////////

stock.from_stock_to_office(p, bug, 6)
print(f' бухгалтерия получила {bug.equipments} единицы')
# ///////////////////////////////////////////////////
bug.from_offic_to_stock(p, stock, 4)
print(f'cклад получил {stock.equ_stock} единицы')
stock.from_stock_to_office(c, logistic, 10)
print(f' отдел логистики получил {logistic.equipments} единицы')
logistic.from_offic_to_stock(c, stock, 3)
print(f'cклад получил {stock.equ_stock} единицы')
logistic.from_offic_to_stock(c, stock, 2)
print(f'cклад получил еще {stock.equ_stock} единицы')
