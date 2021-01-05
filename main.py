from tkinter import *
from random import *
import time

window = Tk()
window.geometry('800x500+300+300')
window.title('flappy bird')
go = True
dy = 1
g = 9.8
t = 5


# x = x0 + g*t ^ 2 / 2


def fall():
    global go
    global dy
    n1 = randint(100, 300)
    c.move(bird, 0, dy)
    c.move('first', -1, 0)
    c.move('second', -1, 0)
    c.move('third', -1, 0)
    if c.coords(tube5)[2] == 500:
        c.coords(tube1, 800, 0, 900, n1)
        c.coords(tube2, 800, n1 + 100, 900, 500)
    if c.coords(tube3)[2] == 500:
        c.coords(tube5, 800, 0, 900, n1)
        c.coords(tube6, 800, n1 + 100, 900, 500)
    if c.coords(tube1)[2] == 500:
        c.coords(tube3, 800, 0, 900, n1)
        c.coords(tube4, 800, n1 + 100, 900, 500)
    if c.coords(bird)[3] < 0:
        c.coords(bird, 40, 480, 60, 500)
    if c.coords(bird)[1] > 500:
        c.coords(bird, 40, 0, 60, 20)

    if ((c.coords(bird)[2] >= c.coords(tube1)[0]) and (c.coords(bird)[0] <= c.coords(tube1)[2])) and (
            (c.coords(bird)[1] <= c.coords(tube1)[3]) or (c.coords(bird)[3] >= c.coords(tube2)[1])):
        go = False
    if ((c.coords(bird)[2] >= c.coords(tube3)[0]) and (c.coords(bird)[0] <= c.coords(tube3)[2])) and (
            (c.coords(bird)[1] <= c.coords(tube3)[3]) or (c.coords(bird)[3] >= c.coords(tube4)[1])):
        go = False
    if ((c.coords(bird)[2] >= c.coords(tube5)[0]) and (c.coords(bird)[0] <= c.coords(tube5)[2])) and (
            (c.coords(bird)[1] <= c.coords(tube5)[3]) or (c.coords(bird)[3] >= c.coords(tube6)[1])):
        go = False

    if go:
        dy += 0.0125
        window.after(t, fall)


def jump(event):
    global dy
    dy = -0.9


n1 = randint(100, 300)
n2 = randint(100, 300)
n3 = randint(100, 300)
c = Canvas(window, width=800, height=500, bg='#40E0D0')
bird = c.create_rectangle(40, 240, 60, 260, fill='yellow')
tube1 = c.create_rectangle(700, 0, 800, n1, fill='green', tag='first')
tube2 = c.create_rectangle(700, n1 + 100, 800, 500, fill='green', tag='first')
tube3 = c.create_rectangle(1100, 0, 1200, n2, fill='green', tag='second')
tube4 = c.create_rectangle(1100, n2 + 100, 1200, 500, fill='green', tag='second')
tube5 = c.create_rectangle(1500, 0, 1600, n3, fill='green', tag='third')
tube6 = c.create_rectangle(1500, n3 + 100, 1600, 500, fill='green', tag='third')
c.bind('<space>', jump)
c.focus_set()
fall()
c.pack()
window.mainloop()
