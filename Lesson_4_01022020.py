# import qwe.my_module as lib
# from my_module import my_func
# from my_module import *


# lib.my_func(10, 5)
# print(lib.pow(10, 5))
# print(lib.pow(10, 5))


# import time
# time_start = time.time()
# time.sleep(2)
# time_end = time.time()
# print(time_end - time_start)


# import math
# print(math.pi)

# from sys import argv
# copy_from = argv[1]
# copy_to = argv[2]
# print('copy from {} to {}'.format(copy_from, copy_to))

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_list = [el ** 2 for el in my_list if el % 2 == 0]
# print(new_list)
#
# my_dict = {el: el ** 2 for el in range(10, 20)}
# print(my_dict)

# from random import randint, randrange
# import random
# print(randint(0, 10))
# print(randrange(10))
# print(randrange(10, 20))
# print(randrange(10, 20, 3))
# print(randrange(100, 200, 50))
# print(random.random()*100)


# yield
#
# generator = (param ** 2 for param in range(5))
# print(generator)
# for i in generator:
#     print(i)
#
# for i in generator:
#     print(i)

# def generator():
#     for el in [10, 20, 30, 50]:
#         yield el
#
# g = generator()
# print(g)
#
# for i in g:
#     print(i)
#
# for i in g:
#     print(i)

# import os
# print(os.getcwd())
# os.removedirs('123')
# print(os.listdir())
# print(os.path.exists('qwe2'))
# os.mkdir()

from functools import reduce, partial

# def my_f(num1, num2):
#     return num1 + num2
#
#
# print(reduce(my_f, [10, 20, 30, 40]))

# def my(p1, p2):
#     return p1 ** p2
#
# new_func = partial(my, 2)
#
# print(new_func)
# print(new_func(4))

# from itertools import count, cycle
#
# # for qwe in count(start=-4, step=1):
# #     if qwe > 15:
# #         break
# #     print(qwe)
#
# c = 0
# for el in cycle('abc'):
#     if c > 10:
#         break
#     print(el)
#     c += 1
