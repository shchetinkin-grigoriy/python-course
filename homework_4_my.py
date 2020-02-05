# 1) Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в # час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv


def person_salary(hour, rate, reward):
    return hour * rate + reward


try:
    *other, hour, rate, reward = argv
    print(f'#1 Salary is {person_salary(float(hour), float(rate), float(reward))}')
except ValueError:
    print('#1 Some params are not correct')
except:
    print('#1 Something wrong')

# 2) Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
origin_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# вариант 1 - через range
result_list = [origin_list[idx] for idx in range(len(origin_list)) if
               idx != 0 and origin_list[idx - 1] < origin_list[idx]]
print('#2 Result list is: {}'.format(result_list))
# вариант 1 - через enumerate
result_list = [item[1] for item in enumerate(origin_list) if item[0] != 0 and origin_list[item[0] - 1] < item[1]]
print('#2 Result list is: {}'.format(result_list))

# 3) Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию ​ range()​ и генератор.
result_list = [number for number in range(20, 241) if (not number % 20) or (not number % 21)]

print('#3 Result list is: {}'.format(result_list))

# 4) Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

origin_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_list = [number for number in origin_list if origin_list.count(number) == 1]

print('#4 Result list is: {}'.format(result_list))

# 5) Реализовать формирование списка, используя функцию ​ range() и возможности генератора. В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка. Подсказка: использовать функцию ​ reduce()​ .
from functools import reduce

origin_list = [number for number in range(100, 1001, 2)]
print('#5 Origin list is: %s' % (origin_list))
print('#5 Result is: %s' % (reduce(lambda x, y: x * y, origin_list)))

# 6) Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию ​ count() и cycle() модуля ​ itertools​ . Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
import itertools

# start_number = int(input("#6 Input start number: "))
start_number = 15
# вариант 1 - через for
iter_1 = (el for el in itertools.count(start_number))
for item in iter_1:
    print('#6.1 Current number is %d' % item)
    if item > 20:
        break
# вариант 2 - через while
iter_2 = (number for number in itertools.cycle([10, 20, -40, 50, 20, 100]))
times = 0
while True:
    item = next(iter_2)
    print('#6.2 Current item is %d' % item)
    if times > 10:
        break
    times += 1

# 7) Реализовать генератор с помощью функции с ключевым словом ​ yield​ , создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: ​ for el in fact(n)​ .
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
import math


def outer_func_fact(n):
    def inner_func_fact(n):
        return math.factorial(n)

    for i in range(1, n + 1):
        yield inner_func_fact(i)


n = int(input('#7 Input n: '))
generator = outer_func_fact(n)
for _ in range(n):
    print(f'#7 {next(generator)}')
