from shapes import *
from tkinter import *
from functools import partial
from tkinter import messagebox

window = Tk()
window.title("Геометрический калькулятор")
window.configure(bg='grey20')
window.overrideredirect(True)


def make_canvas():
    window = Tk()
    window.title("Холст")
    canvas = Canvas(window, width=500, height=500, bg='grey')
    canvas.pack()
    return canvas


def draw_shape(shape_name, shape_entry):
    try:
        entry = shape_entry.get().replace(' ', '').split(',')
        entry = tuple(map(int, entry))
        name = shape_name

        if len(entry) == 1:
            one_entry = {"Круг": Circle(*entry),
                         "Квадрат": Square(*entry),
                         "Сфера": Sphere(*entry),
                         "Куб": Cube(*entry),
                         }
            figure = one_entry[name]

        elif len(entry) == 2:
            two_entry = {"Прямоугольник": Rectangle(*entry),
                         "Ромб": Rhombus(*entry),
                         "Цилиндр": Cylinder(*entry),
                         "Конус": Cone(*entry),
                         "Треугольник": Triangle(*entry)
                         }
            figure = two_entry[name]
        elif len(entry) == 3:
            three_entry = {"Параллелепипед": Parallelepiped(*entry),
                           "Трапеция": Trapezoid(*entry),
                           "Пирамида": Pyramid(*entry)
                           }
            figure = three_entry[name]

        canvas = make_canvas()
        figure.draw_figure(canvas)

        messagebox.showinfo("Расчет",
                            f'Площадь: {figure.get_area()}\n'
                            f'Периметр: {figure.get_perimeter()}\n'
                            f'Объем: {figure.get_volume()}')

    except Exception as ex:
        messagebox.showerror('Расчет', 'Необходимо ввести корректные данные!')
        print(ex)


# Плоские фигуры
Label(window, text="Плоские фигуры", font=('Arial Bold', 14), bg='grey20', fg='green yellow') \
    .grid(row=0, column=0, columnspan=6, pady=10, sticky='nsew')
Label(window, text="Введите требуемые данные через запятую и нажмите на кнопку с именем фигуры",
      font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=1, column=0, columnspan=6, sticky='nsew')

entry_circle = Entry(window, bg='grey30', fg='green yellow')
entry_circle.grid(row=4, column=0, padx=5, sticky='nsew')
Button(window, text="Круг", width=14, height=2, bg='grey30', fg='green yellow',
       command=partial(draw_shape, 'Круг', entry_circle)) \
    .grid(row=2, column=0, padx=5, pady=5, sticky='nsew')
Label(window, text="Радиус", font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=3, column=0, padx=5, sticky=W)

entry_square = Entry(window, bg='grey30', fg='green yellow')
entry_square.grid(row=4, column=1, padx=5, sticky='nsew')
Button(window, text="Квадрат", width=14, height=2, bg='grey30', fg='green yellow',
       command=partial(draw_shape, 'Квадрат', entry_square)) \
    .grid(row=2, column=1, padx=5, pady=5, sticky='nsew')
Label(window, text="Одна сторона", font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=3, column=1, padx=5, sticky=W)

entry_rectangle = Entry(window, bg='grey30', fg='green yellow')
entry_rectangle.grid(row=4, column=2, padx=5, sticky='nsew')
Button(window, text="Прямоугольник", width=14, height=2, bg='grey30', fg='green yellow',
       command=partial(draw_shape, 'Прямоугольник', entry_rectangle)) \
    .grid(row=2, column=2, padx=5, pady=5, sticky='nsew')
Label(window, text="Две стороны", font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=3, column=2, padx=5, sticky=W)

entry_triangle = Entry(window, bg='grey30', fg='green yellow')
entry_triangle.grid(row=4, column=3, padx=5, sticky='nsew')
Button(window, text="Треугольник", width=14, height=2, bg='grey30', fg='green yellow',
       command=partial(draw_shape, 'Треугольник', entry_triangle)) \
    .grid(row=2, column=3, padx=5, pady=5, sticky='nsew')
Label(window, text="Два катета", font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=3, column=3, padx=5, sticky=W)

entry_trapeze = Entry(window, bg='grey30', fg='green yellow')
entry_trapeze.grid(row=4, column=4, padx=5, sticky='nsew')
Button(window, text="Трапеция", width=14, height=2, bg='grey30', fg='green yellow',
       command=partial(draw_shape, 'Трапеция', entry_trapeze)) \
    .grid(row=2, column=4, padx=5, pady=5, sticky='nsew')
Label(window, text="Два основания и высота", font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=3, column=4, padx=5, sticky=W)

entry_rhombus = Entry(window, bg='grey30', fg='green yellow')
entry_rhombus.grid(row=4, column=5, padx=5, sticky='nsew')
Button(window, text="Ромб", width=14, height=2, bg='grey30', fg='green yellow',
       command=partial(draw_shape, 'Ромб', entry_rhombus)) \
    .grid(row=2, column=5, padx=5, pady=5, sticky='nsew')
Label(window, text="Две диагонали", font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=3, column=5, padx=5, sticky=W)

# Объемные фигуры
Label(window, text="Объемные фигуры", font=('Arial Bold', 14), bg='grey20', fg='green yellow') \
    .grid(row=5, column=0, columnspan=6, pady=10, sticky='nsew')
Label(window, text="Введите требуемые данные через запятую и нажмите на кнопку с именем фигуры",
      font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=6, column=0, columnspan=6, sticky='nsew')

entry_sphere = Entry(window, bg='grey30', fg='green yellow')
entry_sphere.grid(row=9, column=0, padx=5, sticky='nsew')
Button(window, text="Сфера", width=14, height=2, bg='grey30', fg='green yellow',
       command=partial(draw_shape, 'Сфера', entry_sphere)) \
    .grid(row=7, column=0, padx=5, pady=5, sticky='nsew')
Label(window, text="Радиус", font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=8, column=0, padx=5, sticky=W)

entry_cube = Entry(window, bg='grey30', fg='green yellow')
entry_cube.grid(row=9, column=1, padx=5, sticky='nsew')
Button(window, text="Куб", width=14, height=2, bg='grey30', fg='green yellow',
       command=partial(draw_shape, 'Куб', entry_cube)) \
    .grid(row=7, column=1, padx=5, pady=5, sticky='nsew')
Label(window, text="Одна сторона", font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=8, column=1, padx=5, sticky=W)

entry_parallelepiped = Entry(window, bg='grey30', fg='green yellow')
entry_parallelepiped.grid(row=9, column=2, padx=5, sticky='nsew')
Button(window, text="Параллелепипед", width=14, height=2, bg='grey30', fg='green yellow',
       command=partial(draw_shape, 'Параллелепипед', entry_parallelepiped)) \
    .grid(row=7, column=2, padx=5, pady=5, sticky='nsew')
Label(window, text="Три стороны", font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=8, column=2, padx=5, sticky=W)

entry_pyramid = Entry(window, bg='grey30', fg='green yellow')
entry_pyramid.grid(row=9, column=3, padx=5, sticky='nsew')
Button(window, text="Пирамида", width=14, height=2, bg='grey30', fg='green yellow',
       command=partial(draw_shape, 'Пирамида', entry_pyramid)) \
    .grid(row=7, column=3, padx=5, pady=5, sticky='nsew')
Label(window, text="Два основания и высота", font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=8, column=3, padx=5, sticky=W)

entry_cylinder = Entry(window, bg='grey30', fg='green yellow')
entry_cylinder.grid(row=9, column=4, padx=5, sticky='nsew')
Button(window, text="Цилиндр", width=14, height=2, bg='grey30', fg='green yellow',
       command=partial(draw_shape, 'Цилиндр', entry_cylinder)) \
    .grid(row=7, column=4, padx=5, pady=5, sticky='nsew')
Label(window, text="Радиус и высота", font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=8, column=4, padx=5, sticky=W)

entry_cone = Entry(window, bg='grey30', fg='green yellow')
entry_cone.grid(row=9, column=5, padx=5, sticky='nsew')
Button(window, text="Конус", width=14, height=2, bg='grey30', fg='green yellow',
       command=partial(draw_shape, 'Конус', entry_cone)) \
    .grid(row=7, column=5, padx=5, pady=5, sticky='nsew')
Label(window, text="Радиус и высота", font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=8, column=5, padx=5, sticky=W)
#
Button(window, text="Exit", bg='grey20', fg='green yellow', command=exit) \
    .grid(row=10, column=0, columnspan=6, padx=5, pady=5, sticky='nsew')

if __name__ == '__main__':
    window.mainloop()
