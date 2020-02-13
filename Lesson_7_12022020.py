# class Car:
#     def __init__(self):
#         self.modules = []
#         self.fc = 7
#
#     def __add__(self, other):
#         self.modules.append(other)
#
#     def __str__(self):
#         return 'Авто с модулями:{}'.format(self.modules)
#
#     def __del__(self):
#         print('объект удален')
#
#     # def __setattr__(self, key, value):
#         # super().__setattr__(key, value)
#         # self.__dict__[key] = value
#         # print(f'добавлена {key} со значением {value}')
#
#     def __getitem__(self, item):
#         return self.modules[item]
#
#     def __call__(self, price=None):
#         # self.price = price
#         print(f'Машина {self.model}, Модули: {self.modules}, Цена: {price}')
#
#     def __eq__(self, other):
#         return self.fc == other.fc
#
# car = Car()
# car + 'люк'
# car + 'колесо'
# car + 'электродвижок'
# car.model = 'Tesla'
# # print(car.modules)
# # print(car.modules[2])
# # print(car[2])
# # car(50000)
# print('Равно' if car == 8 else 'Не равно')

# class Auto:
#     def fuel_cons(self, f_c):
#         self.f_c = f_c
#         print(f'{f_c} литров на сотню')
#
#
# class EAuto(Auto):
#     def fuel_cons(self, f_c):
#         self.f_c = f_c
#         print(f'{f_c} квч на сотню')


# from abc import ABC, abstractmethod
#
# class MyAbcMethod(ABC):
#     @abstractmethod
#     def my_method_1(self):
#         pass
#
#     @abstractmethod
#     def my_method_2(self):
#         pass
#
#
# class MyClass(MyAbcMethod):
#     def my_method_1(self):
#         pass
#
#     def my_method_2(self):
#         pass
# a = MyClass()

#
# class Iterator:
#     def __init__(self):
#         self.i = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i <= 5:
#             return self.i
#         else:
#             raise StopIteration
#
#
# qwe = Iterator()
# for a in qwe:
#     print(a)

#
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self._age = age
#         self.sex = sex
#
#     @property
#     def age(self):
#         # age
#         return self._age
#
#
# human = Human('Ivan', 20, 'м')
# # много кода
# print(human.name)
# print(human.age)

class WinDoor:
    def __init__(self, wd, hd):
        self.square = wd * hd

class Room:
    def __init__(self, len_1, len2, h):
        self.square = 2 * h * (len_1 + len2)
        self.wd = []

    def add_windoor(self, wd, hd):
        self.wd.append(WinDoor(wd, hd))

    def common_squre(self):
        main_square = self.square
        for el in self.wd:
            main_square -= el.square
        return main_square


r = Room(17, 10, 3.7)
print(r.square)
r.add_windoor(2, 2)
r.add_windoor(20, 3)
print(r.common_squre())
