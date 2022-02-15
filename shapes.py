from tkinter import ARC

width = 500
height = 500
center_x = width / 2
center_y = height / 2
line = 2
pi = 3.14


class Draw:
    @staticmethod
    def change_x_y_z_for_draw(x, y, z):
        if x > y and x > z:
            x = 0.7 * width
            y = (y / x) * (0.7 * height)
            z = (z / x) * (0.2 * height)
        elif y > z and y > x:
            y = 0.7 * height
            x = (x / y) * (0.7 * width)
            z = (z / y) * (0.2 * height)
        elif z > x and z > y:
            z = 0.2 * width
            y = (y / z) * 0.7 * height
            x = (x / z) * 0.7 * width
        return x, y, z

        pass

    @staticmethod
    def change_x_y_for_draw(x, y):
        if x >= y:
            x = 0.6 * width
            y = y / x * (0.6 * height)
        else:
            y = 0.6 * height
            x = x / y * (0.6 * width)
        return x, y

    @staticmethod
    def change_x_for_draw():
        return 0.6 * width

    def draw_figure(self, canvas_for_figure):
        pass


class Figure:

    def get_square(self):
        return "Отсутствует"

    def get_perimeter(self):
        return "Отсутствует"

    def get_volume(self):
        return "Отсутствует"

    @classmethod
    def cls_method(cls):
        return 'cls Method'


class Square(Figure, Draw):

    def __init__(self, x):
        super().__init__()
        self.x = x

    @staticmethod
    def get_name_figure():
        return "Квадрат"

    def get_area(self):
        return self.x ** 2

    def get_perimeter(self):
        return 4 * self.x

    def draw_figure(self, canvas):
        Draw.draw_figure(self, canvas)

        canvas.create_rectangle(
            0.3 * width, 0.3 * height,
            0.7 * width, 0.7 * height,
            width=line
        )


class Circle(Square, Figure, Draw):

    def __init__(self, x):
        super().__init__(x)

    @staticmethod
    def name_figure():
        return "Круг"

    def get_area(self):
        return pi * self.x ** 2

    def get_perimeter(self):
        return 2 * pi * self.x

    def draw_figure(self, canvas):
        Draw.draw_figure(self, canvas)

        x = Draw.change_x_for_draw()
        canvas.create_oval(center_x - x / 2, center_y - x / 2,
                           center_x + x / 2, center_y + x / 2,
                           width=line)


class Rectangle(Square, Figure):

    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    @staticmethod
    def get_name_figure():
        return "Прямоугольник"

    def get_area(self):
        return self.x * self.y

    def get_perimeter(self):
        return 2 * (self.x + self.y)

    def draw_figure(self, canvas):
        Draw.draw_figure(self, canvas)

        x, y = Draw.change_x_y_for_draw(self.x, self.y)

        canvas.create_rectangle(
            center_x - x / 2, center_y - y / 2,
            center_x + x / 2, center_y + y / 2,
            width=line
        )


class Triangle(Rectangle):

    def __init__(self, x, y):
        super().__init__(x, y)

    @staticmethod
    def get_name_figure():
        return "Треугольник"

    def get_perimeter(self):
        return self.x + self.y + (self.x ** 2 + self.y ** 2) ** 0.5

    def get_area(self):
        return 0.5 * self.x * self.y

    def draw_figure(self, canvas):
        Draw.draw_figure(self, canvas)

        x, y = Draw.change_x_y_for_draw(self.x, self.y)

        canvas.create_line(
            center_x - x / 2, center_y + y / 2,
            center_x - x / 2, center_y - y / 2,
            center_x + x / 2, center_y + y / 2,
            center_x - x / 2, center_y + y / 2,
            width=line
        )


class Trapezoid(Rectangle, Figure, Draw):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    @staticmethod
    def get_name_figure():
        return "Трапеция"

    def get_area(self):
        return self.y * (self.x + self.z) / 2

    def get_perimetr(self):
        return self.x + self.z + 2 * ((((self.x - self.z) / 2) ** 2 + self.y ** 2) ** 0.5)

    def draw_figure(self, canvas):
        Draw.draw_figure(self, canvas)
        x, y, z = Draw.change_x_y_z_for_draw(self.x, self.y, self.z)

        canvas.create_line(
            center_x - x / 2, center_y + y / 2,
            center_x + x / 2, center_y + y / 2,
            center_x + x / 2 - z / 2, center_y - y / 2,
            center_x - x / 2 + z / 2, center_y - y / 2,
            center_x - x / 2, center_y + y / 2,
            width=line
        )


class Rhombus(Rectangle, Figure, Draw):

    def __init__(self, x, y):
        super().__init__(x, y)

    @staticmethod
    def get_name_figure():
        return "Ромб"

    def get_area(self):
        return self.x * self.y

    def get_perimeter(self):
        return 4 * self.x

    def draw_figure(self, canvas):
        Draw.draw_figure(self, canvas)

        x, y = Draw.change_x_y_for_draw(self.x, self.y)

        canvas.create_line(
            center_x, center_y - y / 2,
                      center_x - x / 2, center_y,
            center_x, center_y + y / 2,
                      center_x + x / 2, center_y,
            center_x, center_y - y / 2,
            width=line
        )


class Sphere(Circle, Figure, Draw):

    def __init__(self, x):
        super().__init__(x)

    @staticmethod
    def get_name_figure():
        return "Сфера"

    def get_perimeter(self):
        return Figure.get_perimeter(self)

    def get_area(self):
        return 4 * pi * self.x

    def get_volume(self):
        return (4 / 3) * self.x ** 3

    def draw_figure(self, canvas):
        Draw.draw_figure(self, canvas)
        Circle.draw_figure(self, canvas)

        x = Draw.change_x_for_draw()

        canvas.create_arc(
            center_x - x / 2, center_y - 20,
            center_x + x / 2, center_y + 20,
            start=180,
            extent=180, style=ARC,
            width=line
        )

        canvas.create_arc(
            center_x - x / 2, center_y - 20,
            center_x + x / 2, center_y + 20,
            start=0,
            extent=180, style=ARC, dash=(10, 10)
        )


class Cube(Square, Figure, Draw):

    def __init__(self, x):
        super().__init__(x)

    @staticmethod
    def get_name_figure():
        return "Куб"

    def get_area(self):
        return 6 * self.x

    def get_perimeter(self):
        return 12 * self.x

    def get_volume(self):
        return self.x ** 3

    def draw_figure(self, canvas):
        Draw.draw_figure(self, canvas)
        Square.draw_figure(self, canvas)

        canvas.create_line(
            0.7 * width, 0.7 * height,
            0.8 * width, 0.5 * height,
            0.8 * width, 0.1 * height,
            0.7 * width, 0.3 * height,
            width=line
        )
        canvas.create_line(
            0.3 * width, 0.3 * height,
            0.4 * width, 0.1 * height,
            0.8 * width, 0.1 * height,
            width=line
        )
        canvas.create_line(
            0.3 * width, 0.7 * height,
            0.4 * width, 0.5 * height,
            0.8 * width, 0.5 * height,
            dash=(10, 10)
        )
        canvas.create_line(
            0.4 * width, 0.5 * height,
            0.4 * width, 0.1 * height,
            dash=(10, 10)
        )


class Parallelepiped(Trapezoid, Figure, Draw):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def get_name_figure():
        return "Параллелепипед"

    def get_area(self):
        return 2 * (self.x * self.y + self.x * self.z + self.y * self.z)

    def get_volume(self):
        return self.x * self.y * self.z

    def get_perimeter(self):
        return 4 * (self.x + self.y + self.z)

    def draw_figure(self, canvas):
        Draw.draw_figure(self, canvas)
        x, y, z = Draw.change_x_y_z_for_draw(self.x, self.y, self.z)

        canvas.create_line(
            center_x - x / 2, center_y - y / 2,
            center_x + x / 2, center_y - y / 2,
            center_x + x / 2, center_y + y / 2,
            center_x - x / 2, center_y + y / 2,
            center_x - x / 2, center_y - y / 2,
            width=line
        )
        canvas.create_line(
            center_x + x / 2, center_y + y / 2,
            center_x + x / 2 + z, center_y + y / 2 - z,
            center_x + x / 2 + z, center_y - y / 2 - z,
            center_x + x / 2, center_y - y / 2,
            width=line
        )
        canvas.create_line(
            center_x - x / 2, center_y - y / 2,
            center_x - x / 2 + z, center_y - y / 2 - z,
            center_x + x / 2 + z, center_y - y / 2 - z,
            width=line
        )
        canvas.create_line(
            center_x - x / 2, center_y + y / 2,
            center_x - x / 2 + z, center_y + y / 2 - z,
            center_x - x / 2 + z, center_y - y / 2 - z,
            dash=(10, 10)
        )
        canvas.create_line(
            center_x - x / 2 + z, center_y + y / 2 - z,
            center_x + x / 2 + z, center_y + y / 2 - z,
            dash=(10, 10),
        )


class Pyramid(Trapezoid, Figure, Draw):

    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    @staticmethod
    def get_name_figure():
        return "Пирамида"

    def get_volume(self):
        return (1 / 3) * self.x * self.y * self.z

    def get_area(self):
        return self.x * self.y + self.x * self.z + self.y * self.z

    def draw_figure(self, canvas):
        Draw.draw_figure(self, canvas)
        x, y, z = Draw.change_x_y_z_for_draw(self.x, self.y, self.z)

        canvas.create_line(
            center_x, center_y - y / 2,
                      center_x - x / 2, center_y + y / 2,
                      center_x + x / 2, center_y + y / 2,
            center_x, center_y - y / 2,
            width=line
        )
        canvas.create_line(
            center_x + x / 2, center_y + y / 2,
            center_x + x / 2 + z, center_y + y / 2 - z,
            center_x, center_y - y / 2,
            width=line
        )
        canvas.create_line(
            center_x - x / 2, center_y + y / 2,
            center_x - x / 2 + z, center_y + y / 2 - z,
            center_x, center_y - y / 2, dash=(10, 10),
        )

        canvas.create_line(
            center_x - x / 2 + z, center_y + y / 2 - z,
            center_x + x / 2 + z, center_y + y / 2 - z,
            dash=(10, 10)
        )


class Cylinder(Rectangle, Figure, Draw):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def get_name_figure():
        return "Цилиндр"

    def get_perimeter(self):
        return Figure.get_perimeter(self)

    def get_area(self):
        return 2 * pi * self.x * self.y

    def get_volume(self):
        return pi * self.x ** 2 * self.y

    def draw_figure(self, canvas):
        Draw.draw_figure(self, canvas)
        x, y = Draw.change_x_y_for_draw(self.x, self.y)

        canvas.create_oval(
            center_x - x // 2, center_y - y // 2,
            center_x + x // 2, (center_y - y // 2) + 24,
            width=line
        )

        canvas.create_arc(
            center_x - x // 2, center_y + y // 2,
            center_x + x // 2, (center_y + y // 2) + 24, start=180,
            extent=180, style=ARC,
            width=line
        )

        canvas.create_line(
            center_x - x // 2, center_y - y // 2 + 12,
            center_x - x // 2, center_y + y // 2 + 12,
            width=line
        )
        canvas.create_line(
            center_x + x // 2, center_y - y // 2 + 15,
            center_x + x // 2, center_y + y // 2 + 15,
            width=line
        )


class Cone(Rectangle, Figure, Draw):

    def __init__(self, x, y):
        super().__init__(x, y)

    @staticmethod
    def get_name_figure():
        return "Конус"

    def get_perimeter(self):
        return Figure.get_perimeter(self)

    def get_area(self):
        return pi * self.x * (self.y ** 2 + self.x ** 2) ** 0.5

    def get_volume(self):
        return (1 / 3) * pi * (self.x ** 2) * self.y

    def draw_figure(self, canvas):
        Draw.draw_figure(self, canvas)
        x, y = Draw.change_x_y_for_draw(self.x, self.y)

        canvas.create_arc(
            center_x - x // 2, center_y + y // 2,
            center_x + x // 2, (center_y + y // 2) + 24,
            start=180,
            extent=180, style=ARC, width=line
        )

        canvas.create_line(
            center_x - x // 2, center_y + y // 2 + 12,
            center_x, center_y - y // 2,
            width=line
        )
        canvas.create_line(
            center_x + x // 2, center_y + y // 2 + 12,
            center_x, center_y - y // 2,
            width=line
        )
