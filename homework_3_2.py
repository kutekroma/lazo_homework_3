### Задание 2

#Создайте класс TriangleChecker в котором можно проверить, возможно ли из представленных отрезков условной длины сформировать треугольник. На вход приниматются только положительные числа. С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
#- Ура, можно построить треугольник!;
#- С отрицательными числами ничего не выйдет!;
#- Нужно вводить только числа!;
#- Жаль, но из этого треугольник не сделать.

#Выполнил Лазо Александр

from dataclasses import dataclass
@dataclass
class TriangleChecker:
    sides: list[float]
    #метод проверки числового значения сторон
    def is_numeric(num):
        return isinstance(num, float) or isinstance(num, int)

    #метод проверки отрицательного числа сторон
    @property
    def is_positive(self):
        if any(side < 0 for side in self.sides):
            return True
        #else:
            #raise TypeError("Отрицательных сторон быть не может у треугольника")

    #проверка треугольника
    def is_triangle(self):
        if not all(map(TriangleChecker.is_numeric, self.sides)):
            return 'Нужно вводить только числа!'
        # сумма двух сторон больше третьей, тогда строим треугольник
        elif sum(self.sides) / 2 > max(self.sides):
            return 'Ура, можно построить треугольник!'
        elif self.is_positive:
            return 'С отрицательными числами ничего не выйдет!'
        elif not all(map(TriangleChecker.is_numeric, self.sides)):
            return 'Нужно вводить только числа!'
        else:
            return 'Жаль, но из этого треугольник не сделать.'


if __name__ == '__main__':
    triangle_1 = TriangleChecker([4, 10, "b"])
    print(triangle_1.is_triangle())

    triangle_2 = TriangleChecker([4, 4, 5])
    print(triangle_2.is_triangle())

    triangle_3 = TriangleChecker([10, 5, -433])
    print(triangle_3.is_triangle())

    triangle_4 = TriangleChecker([2, 3333, 1])
    print(triangle_4.is_triangle())


