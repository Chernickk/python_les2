from abc import ABC, abstractmethod

# TODO 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
#  «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
#  число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
#  валидацию числа, месяца и года (например, месяц — от 1 до 12).
#  Проверить работу полученной структуры на реальных данных.

class Date:
    days_range = range(1, 32)
    month_range = range(1, 13)

    def __init__(self, date):
        date = list(map(int, date.split('-')))
        self.day = date[0]
        self.month = date[1]
        self.year = date[2]

    @staticmethod
    def date_number(date):
        if date.__class__.__name__ == 'Date':
            return date.day, date.month, date.year
        elif date.__class__.__name__ == 'str':
            date = list(map(int, date.split('-')))
            return date[0], date[1], date[2]
        else:
            raise TypeError('incorrect input')


    @classmethod
    def validation(cls, date):
        if date.__class__.__name__ == 'Date':
            if date.day in cls.days_range and date.month in cls.month_range:
                return True
            else:
                return False
        elif date.__class__.__name__ == 'str':
            date = list(map(int, date.split('-')))
            return date[0], date[1], date[2]
        else:
            raise TypeError('incorrect input')




date1 = Date('29-10-2020')

print(Date.date_number(date1))

print(Date.validation(date1))
#print(Date.validation('29-10-2020'))

# TODO 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
#  Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
#  программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyZeroDivisionError(Exception):
    def __init__(self, text):
        self.text = text


try:
    user_input = input("Введите выражение в формате '5/3' >>> ")
    if user_input.strip()[-2:] == "/0":
        raise MyZeroDivisionError("На ноль делить нельзя!")
    else:
        print(eval(user_input))
except MyZeroDivisionError as myerr:
    print(myerr)
except NameError as err:
    print(f"Вы ввели непральное выражение. Ошибка {err}")


# TODO 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
#  Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
#  Класс-исключение должен контролировать типы данных элементов списка.
#  Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
#  пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
#  При этом скрипт завершается, сформированный список выводится на экран.
#  Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
#  При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
#  только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
#  соответствующее сообщение. При этом работа скрипта не должна завершаться.

class NotANumberList(Exception):
    def __init__(self, text):
        self.text = text


try:
    user_input = True
    result = []
    while user_input:
        user_input = input("Введите числа для записи в список, если хотите закончить оставьте пустую строку >>> ")
        user_input = user_input.split()

        for el in user_input:
            #print(el)
            if el.isnumeric():
                result.append(float(el))
            else:
                raise NotANumberList("Вы ввели не число!")
except NotANumberList as myerr:
    print(f'Вы ввели не число :{myerr}')
finally:
    print(result)

# TODO 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
#  А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
#  (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
#  В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#  .
#  5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
#  передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
#  а также других данных, можно использовать любую подходящую структуру, например словарь.
#  .
#  6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
#  Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#  Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
#  изученных на уроках по ООП.

class AlreadyInWarehouse(Exception):
    def __init__(self, text):
        self.text = text


class NotInWarehouse(Exception):
    def __init__(self, text):
        self.text = text


class InvalidInput(Exception):
    def __init__(self, text):
        self.text = text


class Warehouse:
    def __init__(self):
        self.items_count = 0
        self.all_price = 0
        self.items = dict()

    def accept(self, item):
        try:
            if item.model_name in self.items:
                count = 0
                for key in self.items:
                    if key.startswith(item.model_name):
                        count += 1
                item.model_name = f'{item.model_name}_{count}'
            if not item.in_warehouse:
                self.items_count += 1
                self.all_price += item.price
                self.items[item.model_name] = item
                item.in_warehouse = True
            else:
                raise AlreadyInWarehouse('Уже на складе!')
        except AlreadyInWarehouse as err:
            print(f'Ошибка! {item.model_name} {err}')

    def send_to(self, item_name, destination):
        try:
            if self.items[item_name].in_warehouse and self.items[item_name] in self.items.values():
                self.items_count -= 1
                self.all_price -= self.items[item_name].price
                self.items[item_name].in_warehouse = False
                destination.items[self.items[item_name].model_name] = self.items[item_name]
                self.items.pop(item_name)
            else:
                raise NotInWarehouse('Нет на складе!')
        except AlreadyInWarehouse as err:
            print(f'Ошибка! {item_name} {err}')


class Office:
    def __init__(self):
        self.items = dict()

    @property
    def items_count(self):
        return len(self.items)

    @property
    def items_price(self):
        result = 0
        for key in self.items:
            result += self.items[key].price
        return result


class OfficeEquipment(ABC):

    @abstractmethod
    def __init__(self, price, model_name, date_of_manufacture):
        try:
            if (isinstance(price, int) or isinstance(price, float)) and isinstance(model_name, str):
                self.price = price
                self.model_name = model_name
                self.date_of_manufacture = Date(date_of_manufacture)
                self.in_warehouse = False
            else:
                raise InvalidInput('Неправильный ввод!')
        except InvalidInput as err:
            print(f'Ошибка: {err}')

    @abstractmethod
    def break_down(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, price, model_name, ink_value, date_of_manufacture):
        super().__init__(price, model_name, date_of_manufacture)
        self.ink_value = ink_value
        self.is_broken = False

    def break_down(self):
        self.is_broken = True


class Scanner(OfficeEquipment):
    def __init__(self, price, model_name, scan_speed, date_of_manufacture):
        super().__init__(price, model_name, date_of_manufacture)
        self.scan_speed = scan_speed
        self.is_broken = False

    def break_down(self):
        self.is_broken = True


class Xerox(OfficeEquipment):
    def __init__(self, price, model_name, scan_speed, ink_value, date_of_manufacture):
        super().__init__(price, model_name, date_of_manufacture)
        self.ink_value = ink_value
        self.scan_speed = scan_speed
        self.is_broken = False

    def break_down(self):
        self.is_broken = True


printer2 = Printer(10000, 'HP b100', ink_value=100, date_of_manufacture='21-10-2010')
printer3 = Printer(15000, 'Epson', ink_value=100, date_of_manufacture='25-05-2016')

xerox1 = Xerox(100000, 'ac123', ink_value=100, date_of_manufacture='1-04-2019', scan_speed=10)
xerox2 = Xerox(100000, 'ac123', ink_value=100, date_of_manufacture='1-04-2019', scan_speed=10)
xerox3 = Xerox(100000, 'ac123', ink_value=100, date_of_manufacture='1-04-2019', scan_speed=10)
scanner = Scanner(12000, 'HP c300', 13, date_of_manufacture='12-12-2012')

warehouse = Warehouse()
office = Office()

warehouse.accept(printer2)
warehouse.accept(printer3)
warehouse.accept(xerox1)
warehouse.accept(scanner)
warehouse.accept(xerox2)
warehouse.accept(xerox3)

print(warehouse.items)
print(warehouse.items_count)

warehouse.send_to('ac123', office)

print(office.items)

# TODO 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
#  реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры
#  класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
#  Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f'{self.real} + {self.imaginary}i'

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                             self.real * other.imaginary + self.imaginary * other.real)


