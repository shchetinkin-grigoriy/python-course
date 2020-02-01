# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def divide_numbers(a, b):
    try:
        print(f'#1 Result is {a/b:.2f}')
    except ZeroDivisionError:
        print('#1 Second argument is 0')
    except:
        print('#1 Some arguments are not correct')

divide_numbers(10, 3)
divide_numbers(10, 0)
divide_numbers(10, None)

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
# name = input('Please, input name: ')
# surname = input('Please, input surname: ')
# birthday = input('Please, input age: ')
# city = input('Please, input city: ')
# email = input('Please, input email: ')
# phone = input('Please, input phone: ')

name = 'Mike'
surname = 'Johnson'
birthday = '10.10.1990'
city = 'Moscow'
email = 'mike@mail.ru'
phone = '+7987654321'

def print_person(name, surname, birthday, city, **kwargs):
    print(f"#2 User info: {surname} {name} from {city}.Birthday: {birthday}. {('Contacts: ' + ','.join(kwargs.values())) if kwargs else ''}")

print_person(surname=surname, name=name, city=city, email=email, phone=phone, birthday=birthday)

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

# вариант 1
def my_func_1(a, b, c):
    min_value = min(a, b, c)
    return sum(filter(lambda x: x != min_value, [a, b, c]))

# вариант 2
def my_func_2(*args):
    return sum(filter(lambda x: x != min(args), args))

print('#3 Case 1: {}'.format(my_func_1(5, 17, 8)))
print('#3 Case 2: {}'.format(my_func_2(5, 17, 8)))

# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

# вариант 1
def pow_func_1(x, y):
    return x ** y

# вариант 2
def pow_func_2(x, y):
    result = 1
    for _ in range(0, y, -1):
        result *= 1 / x
    return result

print('#4 Pow function, case 1: %s'%(pow_func_1(5, -2)))
print('#4 Pow function, case 2: %s'%(pow_func_2(5, -2)))

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
SPECIAL_SYMBOL = 'S'
def sum_func(num_string):
    if num_string:
        return sum(map(lambda x : int(x), num_string.split(' ')))
    return 0

total_sum = 0
spec_symbol_pos = -1
while spec_symbol_pos == -1:
    numbers_str = input('Input number strings: ')
    spec_symbol_pos = numbers_str.find(SPECIAL_SYMBOL)
    total_sum += sum_func(numbers_str[:spec_symbol_pos - 1] if spec_symbol_pos > -1 else numbers_str)

print('#5 Total sum is {}'.format(total_sum))
# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(text):
    return text.capitalize()

join_string = ' '.join(map(int_func, 'any string may be hear'.split(' ')))
print('#6 Result:', join_string)
