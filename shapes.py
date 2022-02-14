class Shape:
    _title = 'Фигура'

    def area(self):
        pass

    def perimetr(self):
        pass


class Circle(Shape):
    _title = 'Круг'

    def __init__(self, x):
        super().__init__()

        self.__x = x

    def area(self):
        return int(3.14 * self.__x ** 2)

    def perimetr(self):
        return int(2 * 3.14 * self.__x)


class Square(Shape):
    _title = 'Квадрат'

    def __init__(self, x):
        super().__init__()

        self.__x = x

    def area(self):
        return int(self.__x ** 2)

    def perimetr(self):
        return int(self.__x * 4)


class Rectangle(Shape):
    _title = 'Прямоугольник'

    def __init__(self, x, y):
        super().__init__()

        self.__x = x
        self.__y = y

    def area(self):
        return int(self.__x * self.__y)

    def perimetr(self):
        return int(2 * (self.__x + self.__y))


class Cube(Square):
    title = 'Куб'

    def area(self):
        return int(6 * self.__x ** 2)

    def perimetr(self):
        return int(self.__x * 12)