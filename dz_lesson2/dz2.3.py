
#3 Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
u = int(input('enter number :  '))
# РЕАЛИЗАЦИЯ ЧЕРЕЗ ЛИСТ
# season_list = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
# if u in season_list[0]:
#     print('winter')
# elif u in season_list[1]:
#     print('spring')
# elif u in season_list[2]:
#     print('Summer')
# elif u in season_list[3]:
#     print('Autumn')

# РЕАЛИЗАЦИЯ ЧЕРЕЗ СЛОВАРЬ
season_dict = {'winter': (12, 1, 2), 'spring': (3, 4, 5), 'Summer': (6, 7, 8), 'Autumn': (9, 10, 11)}
if u in season_dict['winter']:
    print('winter')
elif u in season_dict['spring']:
    print('spring')
elif u in season_dict['Summer']:
    print('Summer')
elif u in season_dict['Autumn']:
    print('Autumn')