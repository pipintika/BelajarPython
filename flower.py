from turtle import *
from colorsys import *

screen = Screen()
screen.setup(width=1.0, height=1.0)
speed(0)
hue = 0.9
bgcolor('black')
hideturtle()

for i in range(180):
    col = hsv_to_rgb(hue, 1, 1)
    hue += 0.005
    color(col, col)
    begin_fill()
    circle(190 - i, 100)
    lt(90)
    circle(190 - i, 100)
    end_fill()

done()