
# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
u = input('enter user data (name, age ,birth_year, location, phone) : ').split()
def user_data(user_data):
    uu = ','.join(user_data)
    return uu
res_user_data = user_data(u)
print(f'Данные в соответствии  с порядком: name, age ,birth_year, location, phone === {res_user_data}')
