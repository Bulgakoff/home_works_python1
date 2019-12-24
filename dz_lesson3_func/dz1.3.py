# 3.  Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_func(n1, n2, n3):
    lst = [n1, n2, n3]
    lst_min = []

    for i, item in enumerate(lst):
        if min(lst) == item:
            lst_min.append(item)
            lst.remove(item)
            sum_max_two = sum(lst)

    return sum_max_two


res_my_func = my_func(5, 9, 10)
print(f'сумма двух максимальных элементов === {res_my_func}')
