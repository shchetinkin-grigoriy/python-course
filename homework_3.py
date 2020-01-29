print('asd')
# max min для строк сравниваю по ASCII
print(max('aaa', 'asss', key=len))
print(max('saaa', 'aaas'))

print(int(round(1.3222, 2)))
# float  - при приведении к int - НЕ ПАДАЕТ - а отрезает
print(enumerate([2, 3, 5, 6], start=1))
# мои ошибки - итерация изначальо с 1 и через 1
# изначально можно было срезать до 10
# ключевые слова можно предопределить, что опасно!!!
x = 100


# args - кортеж!не лист
def func(name, *args):
    global x
    x = 10
    print(args)


func('asd', 1, 2)
print(x, x * 2, None)


def func2(age, **kwargs):
    print(age, kwargs)


func2(age=100, name='Name')

names = ['name1', 'name2', 'name3']
surnames = ['name1', 'name2', 'name3']
print(zip(names, surnames))
print(list(zip(names, surnames)))
print(dict(zip(names, surnames)))

for name, surname in zip(names, surnames):
    print(name, surname)

numbers = [1, 2, 4, 6, 7]
print(list(map(lambda x, y: x**2, numbers)))
# print(map()) возвращают объекты map и filter
# print(filter())
