# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

name = input("Input your name, please: ")

age = int(input("Your age: "))
salary = 300_000
greeting_string = 'welcome'

print('{} {}! Your age is {}(s) and your salary will be {}'.format(greeting_string.title(), name, age, salary))

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
time_sec = int(input('Input time in seconds: '))
seconds_in_minute = 60
seconds_in_hour = seconds_in_minute * 60
seconds_in_day = seconds_in_hour * 24

time_sec %= seconds_in_day
hours = time_sec // seconds_in_hour
minutes = (time_sec - hours * seconds_in_hour) // seconds_in_minute
seconds = time_sec % seconds_in_minute

print(f'{hours:02}:{minutes:02}:{seconds:02}')

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
n = str(abs(int(input('Input number: '))))
i = 1
summa = 0
while i <= 3:
    summa += int(n*i)
    i += 1
print('Total sum is: ', summa, sep='')

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
number = abs(int(input('Input any number: ')))
i = 0
max_digit = None
while number > 0:
    last_digit = number % 10
    number = number // 10
    if max_digit is None or last_digit > max_digit:
        max_digit = last_digit
print(max_digit)

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
gain = int(input('Input gain: '))
costs = int(input('Input costs: '))
profit = gain - costs;
if profit >= 0:
    print(f'Profit is {profit}')
    print(f'Profitability is {gain / costs:.2f}')
    count = int(input('Input count people in a company: '))
    print(f'Profit by person is {profit / count:.2f}')

else:
    print(f'Costs is {-profit}')

# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
#
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

a = int(input('Input A km: '))
b = int(input('Input B km: '))
day = 1
while a < b:
    a *= 1.1
    day += 1
    print('Day %d: %.2f' % (day, a))

print(f'Yoy need {day} day(s)')
