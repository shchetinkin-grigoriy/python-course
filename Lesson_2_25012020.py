# print(abs(-5))
# print(abs(5))
# print(5 & 3)
# print(5 | 3)
# print(5 ^ 3)
# print(6 >> 1)
# print(6 << 3)


# print(int('0101', 36))
# print(bin(17))
# print(oct(17))
# print(hex(10))

# float(67)
# float(-67)

# a + ib
# complex(5, 6)  # 5 + 6i

my_bla = 'Aнастасия пришла Учить python'
# my_bla[5] = 'c'
# my_bla = my_bla + ' 3.5'
# print(my_bla)
# my_bla1 = 'Aнастасия'
# email = 'ivan@mail.ru'
# print(my_bla)
# print(my_bla + my_bla)
# print(my_bla * 3)
# print(my_bla[1:2:2])  # [start:stop:step]
# print(my_bla[::-2])
# print(len(my_bla))
# print(email.split('@'))
# print(' '.join(['qwe', 'asd']))
# print(my_bla.title())
# print(my_bla.capitalize())
# print(my_bla.lower())
# print(my_bla.upper())
# print(my_bla1.istitle())
# print('при' in my_bla)
# print(my_bla.count('а'))
# print(my_bla.find('и', 20))

# my_list = ['qwe', 1, True, 'ZXC', 12.6, [1, 2, 3]]
# print(list(my_bla)[1:10:3])
# print(list(my_bla)[1:10:3])
# my_list.append('word')
# my_list.insert(2, 'Damir')
# my_list.pop()
# my_list.reverse()
# print(my_list.count([1, 2, 3]))
# print(my_list.index(12.6))
# print(my_list[4])
# print(10 in my_list)
# print(my_list[5][1])

# my_tuple = ('qwe', 1, True, 'ZXC', 12.6, [1, 2, 3])

# a = 10
# b = 10
# print(id(a), id(b))
# print(a is b)  # id(a) == id(b)
# print(a == b)


# my = [1, 2, 3, 44, 5, 6, 7, 7, 8, 1, 12, 43, 5, 1, 1, 1, 11, 1, 0]
# print(my)
# print(set(my))
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a | b)
# print(a == b)
# print(a & b)
# print(a - b)
# a.remove(2)
# a.discard(6)
# print(a)

# human = {'name': 'Ivan', 'age': 35}
# human['data'] = [1, 2, 3]
# print(human.get('qwe'))
# print(human.pop('age'))
# print(human.popitem())
# print(human.keys())
# print(human.values())
# print(human.items())

# print(bool(0))
# print(bool(1))
# print(bool(-1))
# print(bool(False))
# print(bool(True))
# print(bool(None))
# print(bool(''))
# print(bool('as'))
# print(bool([]))
# print(bool(['q']))

# print(b'text')
# print('йцу'.encode('utf-8'))
# print(bytes('text'.encode('utf-8')))

# try:
#     print(10 / 1)
#     print(int('qwe'))
# except ZeroDivisionError:
#     print('Не дели на ноль!')
# except ValueError:
#     print('Вводить число')
# print('qwe')

# some_list = [0, 1, 2, 3, 4]
# for _ in some_list:
#     print('Hello')

# human = {'name': 'Ivan', 'age': 35}
# for value in human.values():
#     print(value)

# a = 5 if 5 < 6 else 0
# print(a)

# print('Welcome' if int(input('Age: ')) >= 18 else 'No Access')

my_list = [ 10 ,  20 ,  20 ,  20 ,  30 ,  50 ,  70 ,  30 ]
print(sorted(my_list, key=my_list.count))
print(max(set(my_list), key=my_list.count))

my_list = [[ 10 ,  20 ,  30 ], [ 40 ,  50 ], [ 60 ], [ 70 ,  80 ,  90 ]]
print(sum(my_list, []))

l = (10, 20, 30) + (40, 50)

print(l)

item_list = [7, 5, 3, 3, 2]
rating = 8  # int(input('Input rating: '))
print(id(item_list))
print(range(item_list))