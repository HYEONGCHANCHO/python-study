import turtle #그래픽처리
import numpy as np #행렬데이터를 처리하기 위한 모듈

myImg=np.array(
    [
        [0,0,0,0,0,0,0,0],\
        [0,1,1,1,0,0,0,0],\
        [1,1,1,1,1,0,0,0],\
        [1,1,1,1,1,0,0,0],\
        [0,1,1,1,0,0,0,0],\
        [0,0,0,0,0,0,0,0],\
        [0,0,0,0,0,0,0,0],
    ]
)

#사각형을 그리고 생상을 흰색 또는 오렌지 색으로 칠하기
def putPixel(x,y,psize,pcol):
    turtle.penup()
    turtle.goto(x*psize,(-1)*y*psize)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(pcol)
    turtle.setheading(45)
    turtle.circle(psize/2,steps=4)
    turtle.end_fill()

pixelsize=20
for j in range(0,8):
    for i in range(0,8):
        if (myImg[j][i]>0):
            putPixel(i,j,pixelsize,'orange')
        else :
            putPixel(i,j,pixelsize,'white')


