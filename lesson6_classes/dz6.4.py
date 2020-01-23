## 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
## speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police=None):  # is_police --> bull
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police  # не понял зачем это свойство
        self.show_speed()

    def show_speed(self):
        print(f'current speed car {self.name} ')

    def go(self):
        print(f'машина {self.name} поехала')

    def stop(self):
        print(f'машина  {self.name} остановилась ')

    def turn(self):
        print(f'машина  {self.name} повернула в город ')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'превышение скорости  для {self.name} на {self.speed - 60} км/ч - допустимый предел 60 км/ч ')
        else:
            print(f'текущая скорость {self.name} {self.speed} - норма')


class SportCar(Car):
    def show_speed(self):
        if self.speed > 90:
            print(f'превышение скорости  для {self.name} на {self.speed - 90} км/ч - допустимый предел 90 км/ч ')
        else:
            print(f'текущая скорость {self.name} {self.speed} - норма')


class WorkCar(Car):
    def show_speed(self):
        if self.is_police == True:
            if self.speed > 40:
                print(f'для грузовика в городе допустимый предел 40 км/ч {self.name} '
                      f'- вы превысили норму на {self.speed - 40} км/ч и оштрафованы на 500')
            else:
                print(f'текущая скорость {self.name} {self.speed} - норма')
        else:
            if self.speed > 40:
                print(f'для грузовика в городе допустимый предел 40 км/ч {self.name} '
                      f'- вы превысили норму на {self.speed - 40} км/ч ')
            else:
                print(f'текущая скорость {self.name} {self.speed} - норма')
class PoliceCar(Car):  # куда к и чему применить ?
    pass


workCar1 = WorkCar(70, 'black', 'грузовик', True)
townCar1 = TownCar(60, 'black', 'минивен')
sportCar = SportCar(100, 'black', 'ferrary')
print(sportCar.name)
polic = PoliceCar(120, 'black', 'седан')
sportCar.go()
townCar1.turn()
