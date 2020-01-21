# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников
# имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
with open('t3.txt', 'r', encoding='utf-8') as ff:
    employ_lst = ff.readlines()
    employ_lst2 = []
    for p in employ_lst:
        employ_lst2.append(p.split())
    print(employ_lst2)

    # //////////////////////////////////////////////
    def foo1(employ_lst2):
        favorits = []
        losers = []
        for i in range(len(employ_lst2)):
            lst_to_dict_fav = {}
            lst_to_dict_los = {}
            for j in range(len(employ_lst2[i])):
                key = employ_lst2[i][0]
                value = float(employ_lst2[i][1])
                if value >= 20000:
                    lst_to_dict_fav[key] = value
                else:
                    lst_to_dict_los[key] = value

            favorits.append(lst_to_dict_fav)
            losers.append(lst_to_dict_los)

        common_lst = favorits + losers
        return common_lst


    r_foo1 = foo1(employ_lst2)


    # ////////////////////////////////////////////////////////////////////////////////////////////
    def foo2(r_foo1):
        lst_for_mid_salary = []
        favorit_lst_dict = []  # убираем пустые словари
        losers_lst_dict = []  # убираем пустые словари
        for i in range(len(r_foo1)):
            for k, v in r_foo1[i].items():
                p = r_foo1[i]
                lst_for_mid_salary.append(v)
                if v >= 20000:
                    print(f'Сотрудник {k} имеет оклад {v} - более 20 тыс. уе ')
                    favorit_lst_dict.append(p)

                else:
                    print(f'Сотрудник {k} имеет оклад {v}  - менее 20 тыс. уе ')
                    losers_lst_dict.append(p)
        result = sum(lst_for_mid_salary) / len(lst_for_mid_salary)
        print(f'средняя зп {int(result)}')


    foo2(r_foo1)
