import json
from random import randint

# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

filepath = "file1.txt"
with open(filepath, "w") as my_file:
    user_input = None
    while user_input != "":
        user_input = input('Введите строку для записи в файл >>>')
        my_file.write(f'{user_input}\n')

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

filepath = "file2.txt"
with open(filepath) as my_file:
    lines_number = 0
    words_number = []
    for line in my_file:
        lines_number += 1
        words_number.append(len(line.split()))

print(f'Количество строк: {lines_number}')
for i, number in enumerate(words_number, 1):
    print(f'Номер строки: {i}. Количество слов: {number}')

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

filepath = "file3.txt"
with open(filepath) as my_file:
    salary_dict = dict()
    for line in my_file:
        line = line.split()
        salary_dict.update({line[0]: int(line[1])})

poor_employees = [key for key in salary_dict if salary_dict[key] < 20000]
print(f'Сотрудники с окладом менее 20 тыс.: {poor_employees}')

average_salary = sum(salary_dict.values())/len(salary_dict)
print(f'Средний оклад: {average_salary}')

# 4. Создать (не программно) текстовый файл со следующим содержимым: One — 1 Two — 2 Three — 3 Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

filepath = "file4.txt"
write_filepath = "file4_1.txt"

numbers_dict = {"Zero": "Ноль",
                "One": "Один",
                "Two": "Два",
                "Three": "Три",
                "Four": "Четыре",
                "Five": "Пять",
                "Six": "Шесть",
                "Seven": "Семь",
                "Eight": "Восемь",
                "Nine": "Девять"}

with open(filepath, encoding="UTF-8")as my_file:
    with open(write_filepath, "w", encoding="UTF-8") as my_file2:
        for line in my_file:
            line = line.split()
            line[0] = numbers_dict[line[0]]
            my_file2.write(f'{" ".join(line)}\n')


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

filepath = "file5.txt"
with open(filepath, "w") as my_file:
    line_of_numbers = list(map(str, [randint(0, 100) for x in range(10)]))
    print(line_of_numbers)
    my_file.write(' '.join(line_of_numbers))

with open(filepath) as my_file:
    line_of_numbers = my_file.read().split()
    list_numbers = map(float, line_of_numbers)
    print(f'Сумма чисел в файле: {sum(list_numbers)}')

# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает
# учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

filepath = "file6.txt"
with open(filepath, encoding="UTF-8") as my_file:
    disciplines = []
    hours = []
    for line in my_file:
        line = line.split()
        disciplines.append(line[0])
        hour = 0
        for elem in line:
            if elem.find("(") != -1:
                hour += int(elem[:elem.index("(")])
        hours.append(hour)

discp_dict = dict(zip(disciplines, hours))

# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки. Необходимо построчно прочитать файл,
# вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки,
# в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

filepath = "file7.txt"

with open(filepath) as my_file:
    profit_list = []
    firm_list = []
    for line in my_file:
        line = line.split()
        firm_list.append(line[0])
        profit = int(line[2]) - int(line[3])
        profit_list.append(profit)
    print(profit_list)

average_profit = sum([profit for profit in profit_list if profit > 0])/len(profit_list)

dict_1 = dict(zip(firm_list, profit_list))
dict_2 = {'Средняя прибыль': average_profit}
result_list = [dict_1,
               dict_2]

json_path = "exercise7.json"
with open(json_path, "w") as json_file:
    json.dump(result_list, json_file)



