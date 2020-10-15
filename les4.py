from sys import argv
from functools import reduce
from itertools import count, cycle
from os import system, name
from time import sleep


# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

def salary(hours, rate, award):
    return int(hours) * int(rate) + int(award)


print(salary(*argv[1:]))

# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

some_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [some_list[i] for i in range(1, len(some_list)) if some_list[i] > some_list[i - 1]]
print(new_list)

# 3.  Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

some_shiny_list = [x for x in range(20, 241) if not x % 20 or not x % 21]
print(some_shiny_list)

# 4 Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

x = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_x = [elem for elem in x if x.count(elem) == 1]

print(new_x)

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.

x = [x for x in range(100, 1001, 2)]
print(x)
print(reduce(lambda x, y: x * y, x))


# 6  Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.

# a


def count_gen(n):
    counter = count(3)
    for i in range(n):
        yield next(counter)


a = count_gen(8)

for i in range(8):
    print(next(a), end=' ')


# б

def cycle_gen(some_list):
    cycler = cycle(some_list)
    while True:
        yield next(cycler)


b = cycle_gen([1, 2, 3, 4, 5])

for i in range(8):
    print(next(b), end=' ')


# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
# for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо
# выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def fact(n):
    result = 1
    for elem in count(1):
        if elem > n:
            break
        else:
            result *= elem
            yield result


g = fact(6)

for elem in g:
    print(elem)

# BONUS
# timer
# Работает как задумано только через командную строку (Windows) или терминал (Unix)

try:
    user_time = input('Введите время для таймера в формате 00:00:00\n >>>').split(':')
    sec = int(user_time[0]) * 3600 + int(user_time[1]) * 60 + int(user_time[2])
    for i in range(sec, -1, -1):
        system('CLS' if name == 'nt' else 'clear')
        print(f'{i // 3600:02d}:{i % 3600 // 60:02d}:{i % 60:02d}')
        sleep(1)
    else:
        print('Время вышло!')
except ValueError as err:
    print('Возникла ошибка', err)
