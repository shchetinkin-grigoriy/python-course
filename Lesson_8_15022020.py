# class DataBaseConnection:
#     @staticmethod
#     def connect():
#         print('connecting')
#
#     def select(self):
#         print('selecting')


# db = DataBaseConnection()
# db.select()
# db.connect()
# DataBaseConnection.connect()

# class MyClass:
#     @classmethod
#     def my_method(cls, param):
#         print(cls, param)
#
#
#     def qwe(self):
#         print('qwe')
#
# MyClass.my_method(50)
# my = MyClass
# my.my_method(70)

# class Customer:
#     """Что это за класс"""
#
#     def __init__(self, name, phone, address):
#         self.name = name
#         self.phone = phone
#         self.address = address
#
#
# john = Customer('John', 8961522424, 'USA')
# print(john.__dict__)
# print(john.__doc__)
# print(john.__class__)
# print(john.__class__.__name__)
# print(john.__module__)
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __str__(self):
#         return self.name + ' ' + self.surname
#
#
# class Teacher(Person):
#     def to_teach(self, subj, *pupils):
#         for pupil in pupils:
#             pupil.to_take(subj)
#
#
# class Pupil(Person):
#     def __init__(self, name, surname):
#         super().__init__(name, surname)
#         self.knowledges = []
#
#     def to_take(self, subj):
#         self.knowledges.append(subj)
#
#
# class Subject:
#     def __init__(self, *subjects):
#         self.subjects = list(subjects)
#
#     def my_list(self):
#         return self.subjects
#
#
# s = Subject('math', 'chemistry', 'physics')
# t = Teacher('Ivan', 'Ivanov')
# p_1 = Pupil('Petr', 'Petrov')
# p_2 = Pupil('Sidr', 'Sidorov')
# t.to_teach(s, p_1, p_2)
# t.to_teach(s, p_1)
# print(p_1.knowledges[1].my_list())

# class OwnError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# input_data = input('Введите положительное число: ')
#
# try:
#     input_data = int(input_data)
#     if input_data < 0:
#         raise OwnError('Вы ввели отрицательное число')
#     else:
#         print('Все ок')
# except OwnError as err:
#     print(err)
# except ValueError:
#     print('Вы ввели не число')

# import psutil
# print(psutil.cpu_stats())
# print(psutil.disk_usage('C:'))
# print(psutil.virtual_memory())

# import requests
# response = requests.get('https://www.bbc.com/')
# print(response.content)

from copy import deepcopy
my_list = [1, 7, [500]]
a = deepcopy(my_list)
for i, el in enumerate(a):
    if i == 2:
        my_list[i].append(600)
print(my_list, a)

