## 2.Реализовать класс Road (дорога), в котором определить атрибуты:
## length (длина), width (ширина). Значения данных атрибутов должны передаваться
## при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 5000м*20м*25кг*5см = 12500 т

class Road:
    def __init__(self, length, width):
        self._leng = length
        self._wid = width

    def get_leng(self):
        return self._leng

    def get_wid(self):
        return self._wid

    def calc_weight(self):
        common_w = self._leng * self._wid * 25 * 5
        return common_w
        # print(common_w, 'тонн')


road1 = Road(5000, 20)
print( f'вес дороги ---- >{road1.calc_weight()} тонн')
print(f' длина дороги ---- > {road1.get_leng()} м ')
