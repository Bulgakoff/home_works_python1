#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

qwe, production, rate, prize = argv

def param_salary(q, w, e):
    arr1 = []
    arr1.append(q)
    arr1.append(w)
    arr1.append(e)
    arr2 = list(map(lambda p: int(p), arr1))

    return arr2


res_param_salary = param_salary(production, rate, prize)
print(f' ----- {res_param_salary}')
production, rate, prize = res_param_salary
total_salary = (production*rate)+prize
print(f' итоговая сумма ЗП === {total_salary} рублей ')
# # print(f' итоговая сумма ЗП === {(int(production) * int(rate)) + int(prize)} рублей ')










