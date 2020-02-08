import os
import functools
DIR = 'lesson_05'

file_name = functools.partial(lambda dir, name: os.path.join(dir, name), DIR)
if not os.path.exists(DIR):
    os.mkdir(DIR)

# 1) Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
try:
    file_1 = open(file_name('1.txt'), 'wt')
    while True:
        string = input('#1. Please, input any string: ')
        if not string:
            break
        file_1.write(string + '\n')
except IOError:
    print('#1 Problem with file appeared')
finally:
    file_1.close()

# 2) Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
count_lines = 0
count_symbols = 0
with open(file_name('2.txt'), 'r') as file_2:
    for line in file_2:
        count_lines += 1
        count_symbols += len(line.split(' '))

print(f'#2 Count lines is {count_lines}, words: {count_symbols}')

# 3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

total_salary = 0
with open(file_name('3.txt'), 'r') as file_3:
    line_list = file_3.readlines()
    for line in line_list:
        surname, salary = line.split(' ')
        salary = float(salary)
        total_salary += salary
        if salary < 20000:
            print(f'#3 Surname {surname}, salary {salary}')

    print(f'#3 Average Salary {total_salary / len(line_list)}')

# 4) Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
dict_numbers = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять',
                'Six': 'Шесть', 'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять'}
try:
    with open(file_name('4.txt')) as file_4:
        file_num = 0
        for line in file_4:
            file_num += 1
            name, *other, number = line.split(" ")
            with open(file_name(f'4.{file_num}.txt'), 'w') as file_4_wr:
                file_4_wr.write(f'{dict_numbers[name]} - {number}')
except IOError:
    print('#4 Some error appears hear')

# 5) Создать(программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random
import functools

try:
    with open(file_name('5.txt'), 'w+') as file_5:

        #запись в файл
        for _ in range(random.randint(10, 50)):
            file_5.write(str(random.randint(0, 100)) + ' ')
        #чтение
        file_5.seek(0)
        print(f"5# Result function: {sum(map(int, file_5.read().strip().split(' ')))}")
except IOError as ex:
    print(f'#5 Some error appears hear {ex}')

# 6) Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) ​ — ​ 10(лаб)
# Физкультура: ​ — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
result_dict = {}
try:
    with open(file_name('6.txt'), 'r') as file_6:
        for line in file_6:
            name, other = line.split(":")
            hour_list = other.replace('(лаб)', '').replace('(л)', '').replace('(пр)', '').strip().split(' ')
            result_dict[name] = sum(map(int, hour_list))
    print(f"6# Total houres by subjects: {result_dict}")
except IOError as ex:
    print(f'#6 Some error appears hear {ex}')

# 7) Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать​.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{​ "firm_1"​ : ​ 5000​ , ​ "firm_2"​ : 3000​ , ​ "firm_3"​ : ​ 1000​ }, {​ "average_profit"​ : ​ 2000​ }]
# Подсказка: использовать менеджер контекста

import json
result_dict = {}
result_list_1 = []
result_list_2 = []
try:
    with open(file_name('7.txt'), 'r') as file_7:
        for line in file_7:
            name, type, gain, charge = line.split(" ")
            gain, charge = int(gain), int(charge)
            result_list_1.append({"name": name, "profit": int(gain) - int(charge)})

except IOError as ex:
    print(f'#6 Some error appears hear {ex}')

profit_list = list(filter(lambda x: x["profit"] > 0, result_list_1))
average_profit = sum(map(lambda x: x["profit"], profit_list)) / len(profit_list)
print(f"7# Average profit: {average_profit}")

for item in result_list_1:
    result_dict[item['name']] = item['profit']
result_list_2.append(result_dict)
result_list_2.append({"average_profit" : average_profit})
with open(file_name('7.json'), 'w') as file_7:
    json.dump(result_list_2, file_7)
