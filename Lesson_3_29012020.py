# print(max(1, 2, 3, 4, 8))
# print(max('zz', 'aaa', key=len))
# print(round(7.5))

# for index, letter in enumerate(['a', 'b', 'c'], start=5):
#     print(index, letter)

# def say_hello(name):
#     print(f'Hello {name}!')
#
#
# say_hello('Ivan')
# say_hello('Petr')


# def average(numbers):
#     count = len(numbers)
#     my_sum = sum(numbers)
#     answer = my_sum / count
#     return answer
#
# qwe = average([1, 2, 3, 4, 5, 6])
# print(qwe)

#
# def my_func(x):
#     pass
#
#
# my_func(1)


# def print(text):
#     pass
# print('qwe')


# x = 100
#
#
# def test(w):
#     w += 10
#     return w
#
#
# x = test(x)
# print(x)


# def func(name, surname=''):
#     print(name, surname)
# func('Ivan')
# func('Ivan', 'Petrov')

# def func(name, *args):
#     что угодно
# print(name, args)
#
# func('Ivan', 50, 10, 30, 50, 80)
# func('Petr', 50, 1)


# def func(name, surname, age):
#     """Описание функции"""
#     print(name, surname, age)
#
# func(surname='Sidorov', name='Ivan', age=50)

# def func(name, surname, **kwargs):
#     print(name, surname, kwargs)
#
# func(surname='Sidorov', name='Ivan', age=50, asd='qwe')

# names = ['Alex', 'Vova', 'Petr']
# surnames = ['Alexov', 'Vovanov', 'Petrov']
#
# # for name, surname in zip(names, surnames):
# #     print(name, surname)
#
# print(list(zip(names, surnames)))
# print(dict(zip(names, surnames)))

# def my_pow(x):
#     return x ** 2


# print(my_pow(5))
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 91]
# result = []
# for num in data:
#     result.append(my_pow(num))
# print(result)
#
# print(list(map(my_pow, data)))
# def my_filter(x):
#     return x > 0


# data = [1, 2, -3, 4, -5, 6, 7, 8, -9, 91]
# print(list(filter(my_filter, data)))

# print(list(filter(lambda x: x > 0, data)))
# print(list(map(lambda x: x ** 2, data)))

# for _ in range(10):
#     print('qwe')

my_list = [[10, 20, 30], [40, 50], [60], [70, 80, 90]]
print(sum(my_list, []))
