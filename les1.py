#1 variables

some_int = 54
some_float = 346.567
some_str = 'hello, world'
some_list = ['1', 2, '3']
some_boolean = True
some_tuple = (1, 3, 5, 7)
some_dict = {'key1': 'value1', 'key2': 'value2'}

user_str = input('Введите строку >>>')
user_float = float(input('Введите число >>>'))

print(f'Вы ввели строку: "{user_str}" и число {user_float}')

#2 time

seconds = int(input('Введите время в секундах: '))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')

#3 sum nnn

n = input('Введите число n: ')
nn = int(2 * n)
nnn = int(3 * n)
n = int(n)

print(n + nn + nnn)

#4 max digit

user_num = input('Введите число: ')

i = 1
max_digit = int(user_num[0])

while i < len(user_num):
    if int(user_num[i]) > max_digit:
        max_digit = int(user_num[i])
    i += 1

print(f'Максимальная цифра в этом числе: {max_digit}')

#5

income = float(input('Введите доход фирмы >>>'))
expences = float(input('Введите издержки фирмы >>>'))
profit = income - expences

if expences > income:
    print('Фирма работает в убыток')
elif expences == income:
    print('Фирма работает в ноль')
else:
    print(f'Прибыль фирмы: {profit}\n'
          f'Рентабельность фирмы {profit / income}')
    emp_number = int(input('Введите число сотрудников >>>'))
    print(f'Прибыль фирмы в расчете на одного сотрудника: {profit / emp_number}')

#6 sport

result = int(input('Введите результат спортсмена в первый день (в километрах) >>>'))
target = int(input('Введите нужное кол-во километров >>>'))

day = 1
while result < target:
    result *= 1.1
    day += 1

print(f'Спортсмен пробежит {target} километров в {day} день')

