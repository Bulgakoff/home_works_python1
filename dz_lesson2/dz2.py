# 6 *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.

# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).

# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# my_dict = {
#     'название': ['компьютер', 'принтер', 'сканер'],
#     'цена': [20000, 6000, 2000],
#     'количество': [5, 2, 7],
#     'eд': ['шт.']
# }


def goods_dict(d):
    dict_comp = {}
    for i in range(d):
        k = input('enter key :  ')
        if k == '':
            print('Error - enter correct key!!!')
            continue
        v = input('enter value :  ')
        if v == '':
            print('Error - enter correct value!!!')
            continue
        dict_comp[k] = v

    return dict_comp


res_goods_dict = goods_dict(3)
print(f'==создание словаря в списке ==={res_goods_dict}')


def create_list(qwe):
    list_my = []
    for i in range(1, qwe):
        internal = []
        for j in range(qwe - 2):
            internal.append(i)
            internal.append(goods_dict(1))
        list_my.append(internal)
    return list_my


res_create_list = create_list(3)


# print(res_create_list)  # [[1, {'название': 'компьютер'}], [2, {'название': 'принтер'}]]
def to_tuple(qw):  #
    list_with_tuple = []
    for p in qw:
        list_with_tuple.append(tuple(p))
    return list_with_tuple


res_to_tuple = to_tuple(res_create_list)
print(
    f'>>>перевод в кортеж элементы списка>>>>>>{res_to_tuple}')
# [(1, {'название': 'компьютер'}), (2, {'название': 'принтер'})]

def frm_dict_to_dict(rgd):
    mdict = {}

    for i in range(len(rgd)):
        k = input('enter key :  ')
        if k == '':
            print('Error - enter correct key!!!')
            continue
        lv = []
        for j in range(3):
            uv = input('Enter value for data analyst  :')
            if uv == '':
                print('Error - enter correct value!!!')
                continue
            lv.append(uv)
        mdict[k] = lv

    return mdict


res_frm_dict_to_dict = frm_dict_to_dict(res_goods_dict)
print(f'-----{res_frm_dict_to_dict}')
