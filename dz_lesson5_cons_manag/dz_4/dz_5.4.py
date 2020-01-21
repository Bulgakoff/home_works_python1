# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#

import json

with open('t4.txt', 'r', encoding='utf-8') as ff:
    qwe = len(ff.readlines())
    ff.seek(0)


    # Необходимо написать программу, открывающую файл на чтение и
    # считывающую построчно данные.
    def foo(qq):
        for i in range(1, qq + 1):
            str_line = ff.readline().split(' ')
            yield str_line


    # При этом английские числительные должны заменяться на русские.

    res_foo = list(foo(qwe))
    c = 0
    for i in range(len(res_foo)):
        c += 1
        for j in range(len(res_foo[i])):
            if res_foo[i][0] != type(int):
                res_foo[i][0] = str(c)


    # Новый блок строк должен записываться в новый текстовый файл.
    def foo_for_dump(res_foo):
        for p in res_foo:
            print(' '.join(p), end=' ')  # не понял как перевести
            # числительные английские в русские (и перевел в цифры)
            yield ' '.join(p)


    with open('t4.1.txt', 'w', encoding='utf-8') as f:
        for el in foo_for_dump(res_foo):
            json.dump(el, f)

