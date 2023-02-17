#Michael Sherrer
#CS 175L
#Stop Sign

import math
import turtle

window_width=400
window_height=400
animation_speed=0
num_sides=8
length=100
angle=45
text_x=-5
text_y=-10

turtle.setup(window_width, window_height)

s=length
x=s/math.sqrt(2)
diameter=s+(2*x)

t=turtle.Turtle()
t.penup()
t.goto(-45,-120)
t.pendown()

for i in range(8):
    t.forward(100)
    t.left(45)
t.penup()
t.goto(0,0)
t.pendown
t.write('STOP')
t.hideturtle()
t.done()
