# 1
types_list = [10, 2.0, True, 'str', [1, 2, 3], (1, 2, 3), {1, 2, 3}, {'1': 1, '2': 2}]

for elem in types_list:
    print(type(elem))

# 2
some_list = []
count = int(input('Введите длину списка >>> '))

for i in range(0, count):
    some_list.append(input(f'Введите {i + 1} элемент списка >>> '))

print(some_list)

for i in range(0, len(some_list) - 1, 2):
    if i + 1 >= len(some_list):
        break
    some_list[i], some_list[i + 1] = some_list[i + 1], some_list[i]

print(some_list)

# 3
# list


try:
    month_number = int(input('Введите номер месяца в виде числа от 1 до 12 >>> '))
    month_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето',
                  'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
    print(month_list[month_number - 1])

    # dict

    month_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето',
                  7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}
    print(month_dict[month_number])
except ValueError:
    print('Введите число')
except IndexError:
    print('Введите число от 1 до 12!')

# 4

user_str = input('Введите строку >>> ')
user_str = user_str.split()
for i, word in enumerate(user_str):
    print(f'{i + 1}. {user_str[i][:10]}')  # Можно добавить \n, но вывод и так с новой строки

# 5

rate_list = [5, 4, 4, 3, 2]
user_num = int(input('Введите число >>> '))

if user_num > max(rate_list):
    rate_list.insert(0, user_num)

# проверка наличия значений меньше введенного
elif min(rate_list) < user_num:
    for num in rate_list:
        if num < user_num:
            rate_list.insert(rate_list.index(num), user_num)
            break
else:
    rate_list.append(user_num)

print(rate_list)

# 6 Решение получилось громоздкое, возможно что-то не так понял

count = int(input('Введите количество товаров >>> '))

goods = []

for i in range(count):
    name = input('Введите название товара >>>')
    price = input('Введите цену товара >>>')
    quantity = input('Введите количество товара >>>')
    unit = input('Введите единицу измерения >>>')
    goods.append((i + 1, {'Название': name, 'Цена': price, 'Количество': quantity, 'Ед.': unit}))

for good in goods:
    print(good)

# for good in list(zip(*goods))[1]:
#     print(good)

name_list = [dicti['Название'] for dicti in list(zip(*goods))[1]]
price_list = [dicti['Цена'] for dicti in list(zip(*goods))[1]]
quantity_list = [dicti['Количество'] for dicti in list(zip(*goods))[1]]
unit_list = [dicti['Ед.'] for dicti in list(zip(*goods))[1]]

statistic = {'Название': list(set(name_list)), 'Цена': list(set(price_list)),
             'Количество': list(set(quantity_list)), 'Ед.': list(set(unit_list))}

print(statistic)