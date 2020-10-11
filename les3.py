# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Ошибка - деление на ноль!'


# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
# email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data(name, last_name, birth_year, city, email, phone_number):
    return f'Имя пользователя: {name} {last_name}, {birth_year}-го года рождения \n' \
           f'Город проживания: {city}, электронная почта: {email}, номер телефона: {phone_number}'


print(user_data(name='Иван', last_name='Иванов', birth_year=1990, city='Москва',
                email='Ivanov@gmail.com', phone_number='+79991112233'))
print(user_data('Иван', 'Иванов', 1990, 'Москва', 'Ivanov@gmail.com', '+79991112233'))


# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def sum_of_two_max_items(a, b, c):
    return a + b + c - min(a, b, c)


# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде
# функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции
# возведения числа в степень.

def my_pow1(number, grade):
    return number ** grade


def my_pow2(number, grade):
    result = 1
    if grade > 0:
        for i in range(grade):
            result *= number
    elif grade < 0:
        for i in range(abs(grade)):
            result /= number
    return result


# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел
# будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def my_sum():
    result = 0
    while True:
        user_insert = input('Введите строку чисел, разделенных пробелом\n'
                            'если хотите закончить - введите Q >>>').split()
        if user_insert == 'q' or user_insert == 'Q':
            break
        elif 'q' in user_insert:
            user_insert = sum(list(map(int, user_insert[:-1])))
            result += user_insert
            break
        else:
            user_insert = sum(list(map(int, user_insert)))
            result += user_insert
        print(user_insert)
    return result


def my_sum1():
    result = 0
    while True:
        user_insert = input('Введите строку чисел, разделенных пробелом\n'
                            'если хотите закончить - введите Q >>>').split()
        for symbol in user_insert:
            if symbol == 'q' or symbol == 'Q':
                return result
            else:
                try:
                    result += int(symbol)
                except ValueError:
                    print('Вы ввели неправильную строку!')
        print(result)

# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
# возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def int_func(s):  # Аналог s.capitalize()
    return f'{s[0].upper()}{s[1:].lower()}'


some_str = input('Введите строку из слов, разделенных пробелом >>>')

# 6.1
new_str = []
for word in some_str.split():
    new_str.append(int_func(word))

print(' '.join(new_str))

# 6.2
print(' '.join(list(map(int_func, some_str.split()))))



