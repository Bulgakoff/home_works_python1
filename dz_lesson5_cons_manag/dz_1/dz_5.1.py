# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем.
with open('t1.txt', 'w', encoding='utf-8') as ff:
    for i in range(4):
        ff.write(input('>>user_dates>>>'))
        ff.write('\n')


    # data_str = ['Фамилия\n', 'Имя\n', 'Отчество\n', 'год Рожденияя',' ']# Об окончании ввода данных
    # # свидетельствует пустая строка. (ЧТО ЗНАЧИТ ЭТО УСЛОВИЕ?)
    # ff.writelines(data_str)
    # # for p in data_str:
    # #     ff.write(p)
