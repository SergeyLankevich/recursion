import turtle as t
import math
import tkinter
from tkinter import ttk
import functools


def square(n, side):
    if n == 0:
        return
    t.down()
    t.speed(0)
    for _ in range(4):
        t.fd(side)
        t.rt(90)
    t.up()
    t.rt(10)
    t.fd(side * 0.05)
    square(n - 1, side * 0.9)


def koch(n, side):
    t.down()
    if n == 0:
        t.fd(side)
        return
    else:
        koch(n - 1, side/3)
        t.lt(60)
        koch(n - 1, side/3)
        t.rt(120)
        koch(n - 1, side/3)
        t.lt(60)
        koch(n - 1, side/3)


def ice(n, side):
    t.down()
    if n == 0:
        t.fd(side)
    else:
        ice(n - 1, side/2)
        t.lt(120)
        ice(n - 1, side/4)
        t.rt(180)
        ice(n - 1, side/4)
        t.lt(120)
        ice(n - 1, side/4)
        t.rt(180)
        ice(n - 1, side/4)
        t.lt(120)
        ice(n - 1, side/2)


def ice2(n, side):
    t.down()
    if n == 0:
        t.fd(side)
    else:
        ice2(n - 1, side/2)
        t.lt(90)
        ice2(n - 1, side/4)
        t.rt(180)
        ice2(n - 1, side/4)
        t.lt(90)
        ice2(n - 1, side/2)


def minkowski(n, side):
    t.down()
    if n == 0:
        t.fd(side)
    else:
        minkowski(n - 1, side / 4)
        t.lt(90)
        minkowski(n - 1, side / 4)
        t.rt(90)
        minkowski(n - 1, side / 4)
        t.rt(90)
        minkowski(n - 1, side / 4)
        minkowski(n - 1, side / 4)
        t.lt(90)
        minkowski(n - 1, side / 4)
        t.lt(90)
        minkowski(n - 1, side / 4)
        t.rt(90)
        minkowski(n - 1, side / 4)


def levi(n, side):
    t.down()
    if n == 0:
        t.fd(side)
    else:
        t.lt(45)
        levi(n - 1, 1 / math.sqrt(2) * side)
        t.rt(90)
        levi(n - 1, 1 / math.sqrt(2) * side)
        t.lt(45)


def tree(n, side):
    t.down()
    if n == 0:
        t.fd(side * 0.75)
        t.bk(side * 0.75)
    else:
        t.fd(side)
        t.rt(30)
        tree(n - 1, side * 0.75)
        t.lt(60)
        tree(n - 1, side * 0.75)
        t.rt(30)
        t.bk(side)


def dragon(n, side):
    t.speed(0)
    if n == 0:
        return t.forward(side)
    t.right(45)
    dragon(n - 1, side * 1 / 2 ** (1 / 2))
    t.left(90)
    t.up()
    t.forward(side * 1 / 2 ** (1 / 2))
    t.down()
    t.left(180)
    dragon(n - 1, side * 1 / 2 ** (1 / 2))
    t.left(180)
    t.up()
    t.forward(side * 1 / 2 ** (1 / 2))
    t.down()
    t.right(45)


def main_koch(n, side):
    t.speed(0)
    t.up()
    t.setposition(-side/2, side*math.sqrt(3)/6)
    koch(n, side)
    t.rt(120)
    koch(n, side)
    t.rt(120)
    koch(n, side)
    t.rt(120)


def main_ice(n, side):
    t.speed(0)
    t.up()
    t.setposition(-side/2, side*math.sqrt(3)/6)

    ice(n, side)
    t.rt(180)
    ice(n, side)
    t.rt(180)
    t.fd(side)
    t.rt(120)

    ice(n, side)
    t.rt(180)
    ice(n, side)
    t.rt(180)
    t.fd(side)
    t.rt(120)

    ice(n, side)
    t.rt(180)
    ice(n, side)
    t.rt(180)
    t.fd(side)
    t.rt(120)


def main_ice2(n, side):
    t.speed(0)
    t.up()
    t.setposition(-side / 2, side * math.sqrt(3) / 6)

    ice2(n, side)
    t.rt(180)
    ice2(n, side)
    t.rt(180)
    t.fd(side)
    t.rt(120)

    ice2(n, side)
    t.rt(180)
    ice2(n, side)
    t.rt(180)
    t.fd(side)
    t.rt(120)

    ice2(n, side)
    t.rt(180)
    ice2(n, side)
    t.rt(180)
    t.fd(side)
    t.rt(120)


def main_minkowski(n, side):
    t.speed(0)
    t.up()
    t.setx(-side/2)
    minkowski(n, side)


def main_levi(n, side):
    t.speed(0)
    t.up()
    t.setx(-side/2)
    levi(n, side)


def main_tree(n, side):
    y = 0
    l = side
    for i in range(n + 1):
        if i % 2 == 0:
            y += l
        else:
            y += l * math.sqrt(3)/2
        l *= 0.75

    t.speed(0)
    t.up()
    t.sety(-y/2)
    t.setheading(90)
    tree(n, side)


def scales(figures, index, depth, length):
    recursion_depth = depth.get()
    side_length = length.get()
    figures.get(index)(recursion_depth, side_length)
    print(recursion_depth, side_length)


figuresDict = {'Koch Snowflake': main_koch, 'Ice Pattern 1': main_ice, 'Ice Pattern 2': main_ice2,
               'Minkowski Fractal': main_minkowski, 'Levi Fractal': main_levi, 'Binary Tree': main_tree,
               'Dragon': dragon}

root = tkinter.Tk()
mainFrame = ttk.Frame(root)
mainFrame.pack(side=tkinter.LEFT, fill='both', expand=True)

addFrame = ttk.Frame(root)
addFrame.pack(side=tkinter.RIGHT, fill='both', expand=True)

depthLabel = tkinter.Label(addFrame, text="Recursion depth: ")
depthLabel.pack()
depthScale = tkinter.Scale(addFrame, orient=tkinter.HORIZONTAL, length=1000, from_=0, to=80, tickinterval=5,
                           resolution=1)
depthScale.pack()

lengthLabel = tkinter.Label(addFrame, text="Side length: ")
lengthLabel.pack()
lengthScale = tkinter.Scale(addFrame, orient=tkinter.HORIZONTAL, length=1000, from_=0, to=1000, tickinterval=50,
                            resolution=5)
lengthScale.pack()

n = depthScale.get()
side = lengthScale.get()

resetButton = ttk.Button(mainFrame, text='Reset', width=18, command=t.bye)
resetButton.pack()

for key in figuresDict.keys():
    button = ttk.Button(mainFrame, text=key, width=18,
                        command=functools.partial(scales, figures=figuresDict, index=key,
                                                  depth=depthScale,
                                                  length=lengthScale))
    button.pack(side=tkinter.BOTTOM)

root.mainloop()




