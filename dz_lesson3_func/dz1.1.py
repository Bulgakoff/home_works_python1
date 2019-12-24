# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
num1 = int(input('enter one number : '))
num2 = int(input('enter second number : '))


def two_numbers(n1, n2):
    try:
        result = n1 / n2
        return result
    except ZeroDivisionError as q:
        print(f' ошибка ---> {q}')
        return q


res_two_numbers = two_numbers(num1, num2)
print(f'==={res_two_numbers}')



