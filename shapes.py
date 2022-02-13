from tkinter import *

window = Tk()
window.title("Холст")
canvas = Canvas(window, width=640, height=480, bg='grey20')
canvas.pack()


def draw_circle():
    canvas.delete("all")
    canvas.create_oval(220, 140, 420, 340, width=2, fill='grey20', outline='green yellow')


def draw_square():
    canvas.delete("all")
    canvas.create_polygon(220, 140, 420, 140, 420, 340, 220, 340, width=2, fill='grey20', outline='green yellow')


def draw_rectangle():
    canvas.delete("all")
    canvas.create_polygon(220, 200, 420, 200, 420, 280, 220, 280, width=2, fill='grey20', outline='green yellow')


def draw_triangle():
    canvas.delete("all")
    canvas.create_polygon(320, 140, 220, 340, 420, 340, width=2, fill='grey20', outline='green yellow')


def draw_trapeze():
    canvas.delete("all")
    canvas.create_polygon(270, 200, 370, 200, 420, 280, 220, 280, width=2, fill='grey20', outline='green yellow')


def draw_rhombus():
    canvas.delete("all")
    canvas.create_polygon(320, 140, 370, 240, 320, 340, 270, 240, width=2, fill='grey20', outline='green yellow')


def draw_sphere():
    canvas.delete("all")
    pass


def draw_cube():
    canvas.delete("all")
    pass


def draw_parallelepiped():
    canvas.delete("all")
    pass


def draw_pyramid():
    canvas.delete("all")
    pass


def draw_cylinder():
    canvas.delete("all")
    pass


def draw_cone():
    canvas.delete("all")
    pass
