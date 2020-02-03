# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). printer, scanner, copier
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
class Stock:
    def __init__(self):
        self.height = 100
        self.width = 200
        self.len = 300


class Office_e:  # базовый класс
    def __init__(self, *args):
        self.param = args


class Printer(Office_e):
    def pr_ter(self):
        print('вывод на печать ')


class Scanner(Office_e):
    def sc_sc(self):
        print('сканирует документ ')


class Copier(Office_e):
    def co_py(self):
        print('копирует документ ')
