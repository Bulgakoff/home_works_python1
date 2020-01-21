# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
# with open('t6.txt', 'r', encoding='utf 8') as ff:
#     res_readff = ff.read()
#     print(res_readff)
#     res_split = res_readff.split()
#     print(res_split)
#     # Важно, чтобы для каждого предмета не обязательно были все типы занятий.
#     # Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
#     d = {res_split[i]: res_split[i + 1] for i in range(len(res_split)) if '(' and ')' not in res_split[i]}
#     # d = {}
#     # for i in range(len(res_split)):
#     #     if '(' and ')' not in res_split[i]:
#     #         d[res_split[i]] = res_split[i + 1]
#     print(d)
# my_dict = dict()
# with open('t6.txt') as f:
#     lines = f.readlines()
#     for line in lines:
#         splitted_line = line.split()
#         subject = splitted_line[0]
#         sum_lessons = sum([int(x[:x.find('(')]) for x in splitted_line[1:] if '(' in x])
#         my_dict[subject] = sum_lessons
# print(my_dict)

with open('t6.txt', 'r', encoding='utf 8') as ff:
    d = {}
    lst_readed = ff.readlines()
    print(lst_readed)
    i = 0
    for el in lst_readed:
        i += 1
        splited_el = el.split()
        print(i, splited_el)
        d[splited_el[0]] = sum([int(v[:v.find('(')]) for v in splited_el[1:]])
    print(d)
