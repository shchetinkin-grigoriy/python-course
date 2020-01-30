# Task 1

some_var = ['123', 123, [123], 123.0, False]
for i in some_var:
    print(type(i))

# Task 2
my_list = list(input('Enter text'))
for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]

print(my_list)

# Task 3
month = int(input('Enter month: '))

if month <= 0 or month >= 13:
    print('Incorrect month')

elif month >= 3 and month <= 5:
    print('Spring')

elif month >= 6 and month <= 8:
    print('Summer')

elif month >= 9 and month <= 11:
    print('Autumn')

else:
    print('Winter')

# второй вариант
seasons_dict = {
    1: 'Winter',
    2: 'Winter',
    3: 'Spring',
    4: 'Spring',
    5: 'Spring',
    6: 'Summer',
    7: 'Summer',
    8: 'Summer',
    9: 'Autumn',
    10: 'Autumn',
    11: 'Autumn',
    12: 'Winter',
}
month = int(input('Enter month: '))
print(seasons_dict[month])

# третий вариант:
seasons_list = ['',
                'Winter',
                'Winter',
                'Spring',
                'Spring',
                'Spring',
                'Summer',
                'Summer',
                'Summer',
                'Autumn',
                'Autumn',
                'Autumn',
                'Winter']
month = int(input('Enter month: '))
print(seasons_list[month])

# Task 4
line = input()
words = line.split()
for i, word in enumerate(words):
    print(i, word[:10])

# Task 5
my_list = [7, 5, 3, 3, 2]
user_num = int(input())

if min(my_list) > user_num:
    my_list.append(user_num)  # все числа в нашем list больше чем введенно пользователем
else:
    for i, num in enumerate(my_list):
        if user_num >= num:
            my_list.insert(i, user_num)
            break
print(my_list)

# Task6
goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analitics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
while True:
    if input('Выход - Q, \nЛюбая клавиша - продолжить: ').upper() == 'Q':
        break
    num += 1
    for f in features.keys():
        user_data = input('{}: '.format(f))
        features[f] = int(user_data) if (f == 'цена' or f == 'количество') else user_data
        analitics[f].append(features[f])
    goods.append((num, features))
    print('Текущая аналитика по товарам:\n')
    for key, value in analitics.items():
        print(key, value)
