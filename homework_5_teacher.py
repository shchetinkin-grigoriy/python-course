'''1. Создать программно файл в текстовом формате, записать
в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.'''
# with open('test.txt', 'w') as f:
#     while True:
#         line = input('Введите строку: ')
#         if line == '':
#             break
#         f.write(line + '\n')


'''2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.'''

# with open('test.txt') as f:
#     lines = f.readlines()
#     print('Количество строк:', len(lines))
#     for num_line, line in enumerate(lines, start=1):
#         print('{} строка содержит - {} слов'.format(num_line, len(line.split())))


'''3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников 
и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., 
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.'''
# Записываем в формате:
# Имя1 - 20000
# Имя2 - 30000
# with open('salaries.txt') as f:
#     salaries = []
#     lines = f.readlines()
#     for line in lines:
#         name, salary = line.split(' - ')
#         salaries.append(int(salary))
#         if int(salary) < 20000:
#             print(line, end='')
#     print('\nСредняя зп:', sum(salaries) / len(salaries))


'''4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую 
построчно данные. При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.'''
# with open('eng.txt') as f:
#     lines = f.readlines()
#
#
# with open('rus.txt', 'w') as f:
#     for line in lines:
#         if '1' in line:
#             line = line.replace('One', 'Один')
#         elif '2' in line:
#             line = line.replace('Two', 'Два')
#         elif '3' in line:
#             line = line.replace('Three', 'Три')
#         elif '4' in line:
#             line = line.replace('Four', 'Четыре')
#         f.write(line)


'''5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
ее на экран.'''
# with open('5.txt', 'w') as f:
#     nums = input('Введите целые числа через пробел: ')
#     f.write('Введенные числа: ' + nums + '\n')
#     nums = map(int, nums.split())  # without list
#     sum_nums = sum(nums)
#     f.write('Сумма чисел: ' + str(sum_nums))
#     print('Сумма введенных чисел:', sum_nums)
# print('Все записано в файл')

'''6. Необходимо создать (не программно) текстовый файл, где каждая строка 
описывает учебный предмет и наличие лекционных, практических и лабораторных 
занятий по этому предмету и их количество. Важно, чтобы для каждого предмета 
не обязательно были все типы занятий. Сформировать словарь, содержащий название 
предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб)
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# 
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''
# my_dict = dict()
# with open('6.txt') as f:
#     lines = f.readlines()
#     for line in lines:
#         splitted_line = line.split()
#         subject = splitted_line[0]
#         sum_lessons = sum([int(x[:x.find('(')]) for x in splitted_line[1:] if '(' in x])
#         my_dict[subject] = sum_lessons
# print(my_dict)


'''7. Создать (не программно) текстовый файл, в котором каждая строка должна 
содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, 
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли 
ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их 
прибылями, а также словарь со средней прибылью. Если фирма получила убытки, 
также добавить ее в словарь (со значением убытков).
# Пример списка: 
[{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.'''

import json

firm_dict = {}
average_profit = []
with open('7.txt') as f:
    lines = f.readlines()
    for line in lines:
        name, form, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        firm_dict[name] = profit
        if profit > 0:
            average_profit.append(profit)

average_profit = sum(average_profit) / len(average_profit)
out_info = [firm_dict, {'average_profit': average_profit}]

with open('7.json', 'w') as f_json:
    json.dump(out_info, f_json)

with open('7.json') as f_json:
    print(json.load(f_json))
