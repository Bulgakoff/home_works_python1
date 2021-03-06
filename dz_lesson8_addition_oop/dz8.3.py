# 3. Создайте собственный класс-исключение, который должен проверять
# содержимое списка на наличие только чисел. Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
#
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и
# вносить его в список, только если введено число. Класс-исключение должен не позволить
# пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.
class Own_ex(Exception):
    def __init__(self, pars=None):
        self.text_ex = pars

    def __str__(self):
        return ' ошибочно введен текст - не число'


lst_nums_text = []
while True:
    user_dates = input('>>введите число >>>>> : ')
    lst_nums_text.append(user_dates)
    if user_dates == 'stop':
        lst_nums_text.remove('stop')
        break
print(lst_nums_text)
lst_nums_only = []
for p in lst_nums_text:
    try:
        num = int(p)
        lst_nums_only.append(num)
    except ValueError:
        continue

print(f'----------только числа -----------> {lst_nums_only}')


