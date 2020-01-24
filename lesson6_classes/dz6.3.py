## 3.Реализовать базовый класс Worker (работник), в котором определить атрибуты:
## name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
## Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного
# имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income  # {"wage": wage, "bonus": bonus}. не получилось
        # передать словарь в метод расчета зп (только через геттер)


class Position(Worker):
    def get_full_name(self):
        return f'сотрудник по имени {self.name} и по фамилии {self.surname}'

    def get_total_income(self):
        return self._income

    def calc_salary(self, income):
        value_sum = sum(income.values())
        print(f'зп сотрудника {self.surname} {self.name}  с учетом премии == {value_sum}')


position_worker1 = Position('Иван', 'Иванов', 'дворник', {"wage": 5000, "bonus": 1000})
position_worker2 = Position('Петр', 'Петров', 'бух', {"wage": 10000, "bonus": 3000})
print(position_worker1.get_full_name())
print(position_worker1.get_total_income())
position_worker1.calc_salary(position_worker1.get_total_income())
position_worker2.calc_salary(position_worker2.get_total_income())
