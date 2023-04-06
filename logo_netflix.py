from turtle import *

WIDTH=600
HEIGHT=500
setup(WIDTH, HEIGHT)
title("NETFLIX LOGO")
bgcolor("black")

colormode(255)
RED = (255, 0, 0)
DARK_RED = (180, 0, 0)
positions = [(-80, 120), (18, 120)]
def logo():
    rt(90)
    for x,y in positions:
        penup()
        setposition(x,y)
        pendown()

        fillcolor(DARK_RED)
        begin_fill()
        for _ in range(2):
            fd(240)
            lt(90)
            fd(48)
            lt(90)
        end_fill()

    penup()
    setposition(-80,120)
    pendown()
    lt(22)

    fillcolor(RED)
    begin_fill()
    for _ in range(2):
        fd(259)
        lt(68)
        fd(49)
        lt(112)
    end_fill()
    hideturtle()

logo()

mainloop()