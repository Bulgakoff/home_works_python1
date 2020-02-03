# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class Ex(Exception):
    def __init__(self, pasr = None):
        self.txt = pasr

    def __str__(self):
        return f' запрещено !! деление на 000'


try:
    data_user1 = int(input('enter txt1 '))
    data_user2 = int(input('enter txt2 '))
    # res_div = data_user1 / data_user2
    if data_user2 == 0:
        raise Ex()
except Ex as eee:
    print(eee)
except ValueError:
    print('не число ')
else:
    res_div = data_user1 / data_user2
    print(f'>>>>>>>> {round(res_div, 2)}')
