# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран

with open('t5.txt', 'w') as ff:
    row_nums = '1 2 3 4 6 7 78 90 7 4 5 6 7 6 3 3 5'
    ff.write(row_nums)

with open('t5.txt', 'r') as ff:
    res_readff = ff.read()
    res_split_lst = res_readff.split()
    res_lst_int = [int(p) for p in res_split_lst]
    print(res_lst_int)
    res_sum_lst = sum(res_lst_int)
    print(f'сумма чисел в файле  == {res_sum_lst}')
