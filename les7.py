from abc import ABC, abstractmethod

# TODO 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
#  который должен принимать данные (список списков) для формирования матрицы.
#  Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#  Примеры матриц вы найдете в методичке.
#  Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#  Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
#  (двух матриц). Результатом сложения должна быть новая матрица.


class Matrix:
    def __init__(self, matrix):
        self.rows = matrix

    def __str__(self):
        result = list(map(str, self.rows))   # избегаем конкатенацию
        return '\n'.join(result)

    def __add__(self, other):
        result = []
        try:
            for i in range(len(self.rows)):
                row = []
                for j in range(len(self.rows[0])):
                    row.append(self.rows[i][j] + other.rows[i][j])
                result.append(row)
        except Exception as ex:
            print(f'Матрицы разного размера! Ошибка: {ex}')
        return Matrix(result)

    def __sub__(self, other):
        result = []
        try:
            for i in range(len(self.rows)):
                row = []
                for j in range(len(self.rows[0])):
                    row.append(self.rows[i][j] - other.rows[i][j])
                result.append(row)
        except Exception as ex:
            print(f'Матрицы разного размера! Ошибка: {ex}')
        return Matrix(result)

    def __mul__(self, other):
        result = []
        try:
            for i in range(len(self.rows)):
                row = []
                for j in range(len(self.rows[0])):
                    row.append(self.rows[i][j] * other.rows[i][j])
                result.append(row)
        except Exception as ex:
            print(f'Матрицы разного размера! Ошибка: {ex}')
        return Matrix(result)


a = Matrix([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])

b = Matrix([[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]])


# TODO 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
#  Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
#  К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
#  размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
#  Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
#  для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
#  Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
#  реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


class Wear(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def cloth_expense(self):
        pass


class Coat(Wear):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def cloth_expense(self):
        return self.size/6.5 + 0.5


class Suit(Wear):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def cloth_expense(self):
        return self.height * 2 + 0.3


# coat = Coat("пальто", 5)
# print(coat.cloth_expense)
#
# suit = Suit('Костюм', 5)
# print(suit.cloth_expense)

# TODO 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
#  В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
#  В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
#  вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться
#  только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток,
#  соответственно. В методе деления должно осуществляться округление значения до целого числа.
#  .
#  Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме
#  ячеек исходных двух клеток.
#  .
#  Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек
#  двух клеток больше нуля, иначе выводить соответствующее сообщение.
#  .
#  Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение
#  количества ячеек этих двух клеток.
#  .
#  Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное
#  деление количества ячеек этих двух клеток.
#  .
#  В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
#  Данный метод позволяет организовать ячейки по рядам.
#  Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно
#  переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
#  Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
#  Тогда метод make_order() вернет строку: *****\n*****\n**.
#  Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
#  Тогда метод make_order() вернет строку: *****\n*****\n*****.


class Cell:
    def __init__(self, count: int):
        if count < 1:
            raise Exception('Невозможно создать клетку без ячеек или с отрицательным значением')
        elif not isinstance(count, int):
            raise ValueError('Количество ячеек должно быть целым числом')
        else:
            self.cell_count = count

    def __add__(self, other):
        return Cell(self.cell_count + other.cell_count)

    def __sub__(self, other):
        if self.cell_count - other.cell_count > 0:
            return Cell(self.cell_count - other.cell_count)
        else:
            raise ValueError('Ошибка!')

    def __str__(self):
        return f'Клетка: {self.cell_count} ячеек'

    def __mul__(self, other):
        return Cell(self.cell_count * other.cell_count)

    def __truediv__(self, other):
        return Cell(self.cell_count // other.cell_count)

    def make_order(self, n):
        rows = '\n'.join((self.cell_count // n) * ['*' * n])
        return f'{rows}\n{(self.cell_count % n) * "*"}'
