import turtle


t = turtle.Turtle()


def reset():
    turtle.resetscreen()

def polygon(t, d, n, is_reset):

    if is_reset:
        reset()

    angle = 360 / n

    for i in range(n):
        t.forward(d)
        t.left(angle)

polygon(t, 20, 8, False)

import math 


def circle(t, r, is_reset):

    perimeter = 2 * math.pi * r
    steps = int(360 / 10)

    distance = perimeter / steps

    polygon(t=t, d=distance, n=steps, is_reset=is_reset)



circle(t, 200, False)
turtle.mainloop()





