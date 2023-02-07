# 모듈 import
import turtle
# t= turtle.Turtle()
t= turtle.Pen()
t.reset()
# 대략 하트모양
t.reset()
t.color(1,0,0)
t.begin_fill()
t.left(45)
t.forward(120)
for x in range(1,40):
    t.left(5)
    t.forward(5)
t.right(120)
for x in range(1,40):
    t.left(5)
    t.forward(5)
t.left(5)
t.forward(120)
t.end_fill()