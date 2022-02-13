from tkinter import *

window = Tk()
window.title("Холст")
canvas = Canvas(window, width=640, height=480, bg='grey20')  # 320 x 240
canvas.pack()


def draw_circle():
    canvas.create_oval(220, 140, 420, 340, width=2, fill='grey20', outline='green yellow')


def draw_square():
    canvas.create_polygon(220, 140, 420, 140, 420, 340, 220, 340, width=2, fill='grey20', outline='green yellow')


def draw_rectangle():
    canvas.create_polygon(220, 200, 420, 200, 420, 280, 220, 280, width=2, fill='grey20', outline='green yellow')


def draw_triangle():
    canvas.create_polygon(320, 140, 220, 340, 420, 340, width=2, fill='grey20', outline='green yellow')


def draw_trapeze():
    canvas.create_polygon(270, 200, 370, 200, 420, 280, 220, 280, width=2, fill='grey20', outline='green yellow')


def draw_rhombus():
    canvas.create_polygon(320, 140, 370, 240, 320, 340, 270, 240, width=2, fill='grey20', outline='green yellow')


def draw_sphere():
    pass


def draw_cube():
    pass


def draw_parallelepiped():
    pass


def draw_pyramid():
    pass


def draw_cylinder():
    pass


def draw_cone():
    pass
