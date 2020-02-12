# 1) Создать класс ​ TrafficLight ​ (светофор) и определить у него один атрибут ​ color ​ (цвет) и метод running ​ (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) ​ — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# * Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from itertools import cycle
import time


class TrafficLight:
    states = ({"name": "Red", "during": 7, "order": 1}, {"name": "Yellow", "during": 2, "order": 2},
              {"name": "Green", "during": 5, "order": 3},
              {"name": "Yellow", "during": 2, "order": 4})

    def __init__(self):
        self.__color = None
        self.__prev_state = None

    def get_color(self):
        return self.__color

    def get_prev_state(self):
        return self.__prev_state

    def _order_diff(self, state):
        return state["order"] - self.get_prev_state()["order"]

    def running(self):
        for i, state in enumerate(cycle(TrafficLight.states)):
            if self.get_prev_state() != None and self._order_diff(state) not in (1, -3):
                raise Exception("#1 Order is incorrect error!")
            self.__prev_state = state
            self.__color = state["name"]
            print(f'#1 Light {self.get_color()}')
            time.sleep(state["during"])
            if i > 10:
                break


traffic_light = TrafficLight()
traffic_light.running()


# 2) Реализовать класс ​ Road ​ (дорога), в котором определить атрибуты: ​ length ​ (длина), ​ width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода. Например: 20м*5000м*25кг*5см = 12500 т

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate(self, weight, depth_sm):
        return self._length * self._width * weight * depth_sm / 1000


road = Road(5000, 20)
print(f'#2 Total weight is {road.calculate(25, 5):.0f}')


# 3) Реализовать базовый класс ​ Worker ​ (работник), в котором определить атрибуты: name, surname, position(должность), income(доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например {"wage": wage, "bonus": bonus}. ​
# Создать класс ​ Position ​ (должность) на базе класса ​ Worker​.
# В классе Position реализовать методы получения полного имени сотрудника (​ get_full_name​ ) и дохода с учетом премии (​ get_total_income​ ).
# Проверить работу примера на реальных данных (создать экземпляры класса ​ Position​ , передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return '{} {}'.format(self.surname, self.name)

    def get_total_income(self):
        return sum(self._income.values())


position = Position('Mike', 'Stone', 'Manager', 50_000, 10_000)
print(f'#3 Full name: {position.get_full_name()}')
print(f'#3 Total income: {position.get_total_income()}')


# 4) Реализуйте базовый класс ​ Car​ . У данного класса должны быть следующие атрибуты: ​ speed​ , color​ , ​ name​ , ​ is_police ​ (булево).
# А также методы: ​ go​ , ​ stop​ , ​ turn(direction)​ , которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: ​ TownCar​ , ​ SportCar​ , ​ WorkCar​ , ​ PoliceCar​ .
# Добавьте в базовый класс метод show_speed​ , который должен показывать текущую скорость автомобиля.
# Для классов TownCar ​ и ​ WorkCar ​ переопределите метод ​ show_speed​ . 
# При значении скорости свыше 60 (​ TownCar​ ) и 40 (​ WorkCar​ ) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    # states = ("Stop", "Turn", "Go")
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self._state = "Stop"

    def go(self):
        self._state = "Go"

    def stop(self):
        self._state = "Stop"

    def turn(self, direction):
        self._state = "Turn {}".format(direction)

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'#4 Speed is over out the rule')
        return super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'#4 Speed is over out the rule')
        return super().show_speed()


class PoliceCar(Car):
    pass


townCar = TownCar(70, 'Yellow', 'Lada', False)
workCar = WorkCar(50, 'Red', 'Volga', False)
sportCar = SportCar(170, 'White', 'Merc', False)
policeCar = PoliceCar(100, 'Blue', 'BMV', True)

print(f'#4 Town car speed: {townCar.show_speed()}, color {townCar.color}')
print(f'#4 Work car speed: {workCar.show_speed()}, color {workCar.color}')
print(f'#4 Sport car speed: {sportCar.show_speed()}, color {sportCar.color}')
print(f'#4 Police car speed: {policeCar.show_speed()}, color {policeCar.color}')


# 5) Реализовать класс ​ Stationery ​ (канцелярская принадлежность). Определить в нем атрибут ​ title (название) и метод ​ draw ​ (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса ​ Pen ​ (ручка), ​ Pencil ​ (карандаш), ​ Handle ​ (маркер).
# В каждом из классов реализовать переопределение метода ​ draw​ .
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('#5 Запуск отрисовки')


class Pencil(Stationery):
    def draw(self):
        print('#5 Запуск отрисовки карандашом')


class Pen(Stationery):
    def draw(self):
        print('#5 Запуск отрисовки кручкой')


class Handle(Stationery):
    def draw(self):
        print('#5 Запуск отрисовки маркером')


Stationery("Канцелярская принадлежность").draw()
Pencil("Карандаш").draw()
Pen("Кручка").draw()
Handle("Маркер").draw()
