# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.

# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл,
import json
#
# with open('t7.txt', 'r', encoding='utf-8') as ff:
#     res_readlines = ff.readlines()
#     print(res_readlines)
#     ff.seek(0)
#
#
#     def rlp(res_readlines):
#         for i in range(len(res_readlines)):
#             res_readff = ff.readline()
#             print(res_readff, end=' ')
#             split_lst = res_readff.split()
#             # print(split_lst)
#
#             revenue = {split_lst[i]: int(split_lst[-2]) for i in range(len(split_lst)) if 'firm' in split_lst[i]}
#             loss = {split_lst[i]: int(split_lst[-1]) for i in range(len(split_lst)) if 'firm' in split_lst[i]}
#             profit = {split_lst[i]: int(split_lst[-2]) - int(split_lst[-1]) for i in range(len(split_lst)) if
#                       'firm' in split_lst[i]}
#
#             print(f'доход компании {split_lst[0]}  == {int(split_lst[-2])}')
#             print(f'прибыль компании {split_lst[0]} == {int(split_lst[-2]) - int(split_lst[-1])}')
#             print(f'издержки компании {split_lst[0]} == {int(split_lst[-1])}\n')
#             yield profit
#
#
#     res_rlp = list(rlp(res_readlines))
#     print('Общий список фирм c прибылями: ')
#     print(res_rlp)
#
#     res_sum_v = 0
#     for i in range(len(res_rlp)):
#         for k, v in res_rlp[i].items():
#             res_sum_v += v
#     average_profit = res_sum_v / len(res_readlines)
#     print(f'расчет средней прибыли {average_profit}')
#     aver_d = {'average_profit': average_profit}
#     res_rlp.append(aver_d)
#     print(res_rlp)
#
# # вычислить прибыль каждой компании,
# # а также среднюю прибыль.
# # Если фирма получила убытки, в расчет средней прибыли ее не включать.
#
# # Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# # а также словарь со средней прибылью. Если фирма получила убытки,
# # также добавить ее в словарь (со значением убытков).
# # Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# # Итоговый список сохранить в виде json-объекта в соответствующий файл.
# # Пример json-объекта:
# # [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# # Подсказка: использовать менеджер контекста.
# with open('t7.1.txt', 'w') as ff:
#     json.dump(res_rlp, ff)
#
# with open('t7.1.txt', 'r') as ff:
#     print(json.load(ff))

firm_dict = {}
average_profit = []
with open('t7.txt',encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
        name, form, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        firm_dict[name] = profit
        if profit > 0:
            average_profit.append(profit)

average_profit = sum(average_profit) / len(average_profit)
out_info = [firm_dict, {'average_profit': average_profit}]

with open('t7.json', 'w') as f_json:
    json.dump(out_info, f_json)

with open('t7.json') as f_json:
    print(json.load(f_json))
