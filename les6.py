from itertools import cycle
from time import sleep
from functools import reduce

# TODO 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
#  Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
#  красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
#  второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами
#  должно осуществляться только в указанном порядке (красный, желтый, зеленый).
#  Проверить работу примера, создав экземпляр и вызвав описанный метод.


class TrafficLight:
    def __init__(self):
        self.__color = 'Green'

    def running(self):
        for i in cycle(range(20)):
            if 0 <= i < 8:
                self.__color = 'Red'
            elif 8 <= i < 10:
                self.__color = 'Yellow'
            else:
                self.__color = 'Green'
            sleep(1)


# TODO 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
#  Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
#  Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
#  Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
#  толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.

class Road:
    def __init__(self, length, width, thickness):
        self._length = length
        self._width = width
        self.mass = 25
        self.thickness = thickness

    def asphalt_mass(self):
        return reduce((lambda x, y: x * y), vars(self).values())

# TODO 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
#  position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
#  содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
#  Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения
#  полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
#  Проверить работу примера на реальных данных (создать экземпляры класса Position,
#  передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": wage,
                       "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, income):
        super().__init__(name, surname, position, wage, income)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_full_income(self):
        return self.income['wage'] + self.income['bonus']


developer = Position('Nikita', 'Cherenkov', 'Developer', 100500, 100500)
print(developer.get_full_income())
print(developer.get_full_name())

# TODO 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
#  speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
#  что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
#  TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать
#  текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
#  При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.


class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала прямо!')

    def stop(self):
        print(f'{self.name} остановилась!')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}!')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость: {self.speed} км/ч')
        if self.speed > 60:
            print(f'{self.name} превышает скорость!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость: {self.speed} км/ч')
        if self.speed > 40:
            print(f'{self.name} превышает скорость!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


my_car = TownCar(70, 'green', 'Nissan', False)

my_car.show_speed()
my_car.turn('налево')

police = PoliceCar(90, 'white', 'Ford', True)

print(police.is_police)
print(police.name)

# TODO 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
#  и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
#  Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
#  Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
#  что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'В {self.title} закончились чернила!')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} не заточен!')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} высох!')


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

pen.draw()
pencil.draw()
handle.draw()
