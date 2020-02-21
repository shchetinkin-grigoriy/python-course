# 1) Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
import datetime


class Data:

    def __init__(self, date_str):
        self.date_str = date_str

    def __str__(self):
        return self.date_str

    @classmethod
    def converto_to_number(cls, data):
        date_str = str(data)
        if not Data.validate_date(date_str):
            raise Exception("#1 Date is not correct")

        return int(datetime.datetime.strptime(date_str, '%d-%m-%Y').timestamp())

    @staticmethod
    def validate_date(date_str):
        return date_str[0:2].isdigit() and date_str[3:5].isdigit() and date_str[6:9].isdigit()


data = Data('25-12-2020')
print(f'#1 Result time in seconds: {Data.converto_to_number(data)}')
# 2) Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

import traceback


class MyZeroDivisionError(ZeroDivisionError):
    pass


try:
    i = int(input('#2 Input number: '))
    if i == 0:
        raise MyZeroDivisionError('#2 Number is 0')
    print(f'#2 Division is {1 / i:.2f}')
except MyZeroDivisionError as error:
    print(f'#2 Zero division error: {traceback.format_exc()}')
    pass
except:
    print(f'#2 Another error: {traceback.format_exc()}')


# 3) Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class IncorrectItemError(Exception):

    def __init__(self, item):
        self.item = item


number_list = []
while True:
    try:
        item = input('#3 Input number: ')
        if item == 'stop':
            break
        elif not item.isdigit():
            raise IncorrectItemError(item)
        else:
            number_list.append(int(item))
    except IncorrectItemError as ex:
        print(f'#3 Error item: {ex.item}')

print(f'#3 Result list: {number_list}')


# 4) Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5) Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

class Storage:
    def __init__(self):
        self._items = dict()

    def add_item(self, item):
        self._items.setdefault(item.get_type(), []).append(item)

    def remove_item(self, item_type, count):
        items = self._items.get(item_type)
        if not items or len(items) < count:
            raise Exception(f'#6 Items are not enough to remove')

        result_list = []
        i = 0
        while i < count:
            result_list.append(items.pop())
            i += 1
        return result_list

    def __str__(self) -> str:
        return str(len(sum(self._items.values(), [])))


import abc


class Equipment(abc.ABC):
    def __init__(self, brand):
        self.brand = brand

    def get_type(self):
        return self._type


class Printer(Equipment):
    def __init__(self, brand, is_color):
        super().__init__(brand)
        self.is_color = is_color
        self._type = 'P'


class Scanner(Equipment):
    def __init__(self, brand, size):
        super().__init__(brand)
        self.size = size
        self._type = 'S'


class Xerox(Equipment):
    def __init__(self, brand, speed):
        super().__init__(brand)
        self.speed = speed
        self._type = 'X'


# 6) Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
storage = Storage()
storage.add_item(Printer("Sony", True))
storage.add_item(Printer("Philips", False))
storage.add_item(Scanner("LG", "A4"))
storage.add_item(Scanner("Samsung", "A4"))
storage.add_item(Xerox("LG", 10))
storage.add_item(Xerox("Sony", 8))

print(f'#6 Storage before: {storage}')
while True:

    n = input("#6 How many equipments remove from storage: ")
    if not n:
        break

    try:
        if not n.isdigit():
            raise Exception(f'#6 It is not a valid number')

        equip_type = input("#6 Input type to remove Printer(P), Scanner(S) or Xerox(X) : ")
        if equip_type != 'P' and equip_type != 'S' and equip_type != 'X':
            raise Exception(f'#6 It is not a valid equipment type')

        storage.remove_item(equip_type, int(n))
    except Exception as ex:
        print(ex)
print(f'#6 Storage after: {storage}')


# 7) Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
class ComplexNumber:
    def __init__(self, real, imag):
        self.number = complex(real, imag)

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number


complex_number_1 = ComplexNumber(2, 5)
complex_number_2 = ComplexNumber(5, 2)
print(f'#7 Sum complex numbers: {complex_number_1 + complex_number_2}')
print(f'#7 Mul complex numbers: {complex_number_1 * complex_number_2}')
