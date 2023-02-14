import turtle
import numpy as np

myImg=np.array([
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    [0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0],\
    [0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0],\
    [0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0],\
    [0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0],\
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    [0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0],\
    [0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0],\
    [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0],\
    [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],\
    [0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0],\
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ])

def make(x,y,psize,pcol):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x*psize,(-1)*y*psize)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(pcol)
    turtle.setheading(45)
    turtle.circle(psize/2,steps=4)
    turtle.end_fill()

psize=30
for j in range(0,16):
    for i in range(0,16):
        if (myImg[j][i]>0):
            pcol='orange'
            make(i,j,psize,pcol)
        else :
            pcol='white'
            make(i,j,psize,pcol)