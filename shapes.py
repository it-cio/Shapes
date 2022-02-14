class Shape:

    _title = 'Фигура'

    def area(self):
        pass

    def perimetr(self):
        pass


class Square(Shape):

    _title = 'Квадрат'

    def __init__(self, x):
        super().__init__()

        self.__x = x

    def area(self):
        return self.__x ** 2

    def perimetr(self):
        return self.__x * 4