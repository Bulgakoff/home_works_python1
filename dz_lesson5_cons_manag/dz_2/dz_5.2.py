# 2.Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить # подсчет количества строк, количества слов в каждой строке.
with open('t2.txt', 'r', encoding='utf-8') as ff:
    res_lst = ff.readlines()
    print(res_lst)
    num_strings = len(res_lst)
    print(f'количество строк текста == {num_strings}')
    c = 0
    for p in res_lst:
        c += 1
        print(f"количество букв в строке {c}  == {len(p) - p.count(' ') - p.count(',') - p.count('.') - 1}")
