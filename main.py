import turtle as t
import math


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


def minkovski(n, side):
    t.down()
    if n == 0:
        t.fd(side)
    else:
        minkovski(n - 1, side / 4)
        t.lt(90)
        minkovski(n - 1, side / 4)
        t.rt(90)
        minkovski(n - 1, side / 4)
        t.rt(90)
        minkovski(n - 1, side / 4)
        minkovski(n - 1, side / 4)
        t.lt(90)
        minkovski(n - 1, side / 4)
        t.lt(90)
        minkovski(n - 1, side / 4)
        t.rt(90)
        minkovski(n - 1, side / 4)


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

def tree(n, side, det):
    t.down()
    if n == 0:
        t.fd(side * det)
        t.bk(side * det)
    else:
        t.fd(side)
        t.rt(30)
        tree(n - 1, side * det, det)
        t.lt(60)
        tree(n - 1, side * det, det)
        t.rt(30)
        t.bk(side)


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


def main_minkovski(n, side):
    t.speed(0)
    t.up()
    t.setx(-side/2)
    minkovski(n, side)


def main_levi(n, side):
    t.speed(0)
    t.up()
    t.setx(-side/2)
    levi(n, side)


def main_tree(n, side, det):
    y = 0
    l = side
    for i in range(n + 1):
        if i % 2 == 0:
            y += l
        else:
            y += l * math.sqrt(3)/2
        l *= det

    t.speed(0)
    t.up()
    t.sety(-y/2)
    t.setheading(90)
    tree(n, side, det)


print('What do you want to draw (choose the number)?')
print('1. Koch Snowflake')
print('2. Ice Pattern 1')
print('3. Ice Pattern 2')
print('4. Minkovski Fractal')
print('5. Levi Fractal')
print('6. Binary Tree')
print('7. Fractal Dragon')
choice = input()
while True:
    try:
        choice = int(choice)
    except ValueError:
        print('Please, enter the number')
    else:
        if 1 <= choice <= 7:
            break
        else:
            print('Please, enter the number from the proposal')
            choice = input()
n = input('n = ')
while True:
    try:
        n = int(n)
    except ValueError:
        print('Please, enter the natural number')
        n = input('n = ')
    else:
        break
side = input('side = ')
while True:
    try:
        side = int(side)
    except ValueError:
        print('Please, enter the natural number')
        side = input('side = ')
    else:
        break

if choice == 1:
    main_koch(n, side)
elif choice == 2:
    main_ice(n, side)
elif choice == 3:
    main_ice2(n, side)
elif choice == 4:
    main_minkovski(n, side)
elif choice == 5:
    main_levi(n, side)
elif choice == 6:
    main_tree(n, side, 1/2)
elif choice == 7:
    print('Sorry, the dragon got lost somewhere. Now we will find him...')

t.exitonclick()
