import turtle
t= turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
color=["red","pink","magenta","green"]


for x in range(180):
    t.pencolor(color[x%4])
    t.circle(x)
    t.left(360/4)
    t.width(1)



# 반지름 입력 받아서 원 그리는거 만들기
# t=turtle.Pen()
# len=int(turtle.numinput("반지름 입력","숫자로 입력"))

# t.circle(len*len)