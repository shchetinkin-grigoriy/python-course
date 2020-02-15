# 1) Реализовать класс ​ Matrix ​ (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()​ ), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — ​ система некоторых математических величин, расположенных в виде прямоугольной схемы. Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# 31 22       3 5 32      3 5 8 3
# 37 43       2 4 6       8 3 7 1
# 51 86       -1 64 -8
# Следующий шаг — реализовать перегрузку метода ​ __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода ​ __add__() для реализации операции сложения двух объектов класса ​ Matrix ​ (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix_list):
        self._matrix = matrix_list
        self.__index = 0

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self._matrix])

    def __getitem__(self, item):
        return self._matrix[item]

    def __iter__(self):
        return enumerate(self._matrix)

    def __add__(self, matrix_add):
        matrix_new = []
        for i, row in self:
            matrix_new.append([el_1 + matrix_add[i][el_i] for el_i, el_1 in enumerate(row)])
        return Matrix(matrix_new)


matrix_1 = Matrix([[5, 8, 10], [1, 0, -1], [8, 10, 20]])
matrix_2 = Matrix([[-5, 6, 10], [-1, 7, 8], [-8, 10, 0]])
print('#1 Matrix 1:\n{}'.format(matrix_1))
print('#1 Matrix 2:\n{}'.format(matrix_2))
print('#1 Matrix add operation:\n{}'.format(matrix_1 + matrix_2))

# 2) Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — ​ одежда​ , которая может иметь определенное название.
# К типам одежды в этом проекте относятся ​ пальто ​ и ​ костюм​ .
# У этих типов одежды существуют параметры: ​ размер ​ (для ​ пальто​ ) ​ и ​ рост ​ (для ​ костюма​ ).
# Это могут быть обычные числа: ​ V и H​ , соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5)​ , для костюма ​ (2*H + 0.3)​ .
# Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора ​ @property​ .
from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def calculate_textile(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def name(self):
        return "Coat"

    def calculate_textile(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(self, height)
        self.height = height

    @property
    def name(self):
        return "Suit"

    def calculate_textile(self):
        return 2 * self.height + 0.3


coat = Coat(50)
suit = Coat(1.70)
print(f'#2 For {coat.name} needs {coat.calculate_textile():.2f} textiles')
print(f'#2 For {suit.name} needs {suit.calculate_textile():.2f} textiles')


# 3) Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (​ __add__()​ ), вычитание (​ __sub__()​ ), умножение (​ __mul__()​ ), деление (​ __truediv__()​ ).
# Данные методы должны применяться ​ только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
#
# Сложение​. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание​ . Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение​ . Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление​ . Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
#
# В классе необходимо реализовать метод ​ make_order() , принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида ​ *****\n*****\n*****​ ..., где количество ячеек между ​ \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() ​ вернет строку: ​ *****\n*****\n**​ .
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() ​ вернет строку: ​ *****\n*****\n*****​ .
# Подсказка: подробный список операторов для перегрузки доступен по ​ ссылке​ .

class OrganicCell:
    def __init__(self, cell_count):
        self.cell_count = cell_count

    def __add__(self, other_cell):
        return self.cell_count + other_cell.cell_count

    def __sub__(self, other_cell):
        count = self.cell_count - other_cell.cell_count
        if count <= 0:
            raise Exception("Operation is not possible")
        return count

    def __mul__(self, other_cell):
        return self.cell_count * other_cell.cell_count

    def __truediv__(self, other_cell):
        return self.cell_count // other_cell.cell_count

    # версия 1 - через срезы
    def make_order(self, count):
        result_string = "*" * self.cell_count
        return '\n'.join([result_string[i - count: i] for i in range(count, self.cell_count + count, count)])

    # версия 2 - через расчет количества - генератор
    def make_order_v2(self, count):
        return '\n'.join(['*' * (count if (self.cell_count - i) > count else self.cell_count - i) for i in
                          range(0, self.cell_count, count)])

    # версия 3 - через расчет количества - чикл
    def make_order_v3(self, count):
        result_string = ""
        for i in range(0, self.cell_count, count):
            result_string += '*' * (count if (self.cell_count - i) > count else self.cell_count - i) + '\n'
        return result_string


organic_cell = OrganicCell(12)
print(f'#3 Result order is: \n{organic_cell.make_order(5)}')
print(f'#3 Result order V2 is: \n{organic_cell.make_order_v2(5)}')
print(f'#3 Result order V3 is: \n{organic_cell.make_order_v3(5)}')
