import turtle
t=turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
colors=['red','yellow','blue','green','orange','purple','white','gray']
sides= int(turtle.numinput("원의 갯수","(1-8)를 선택하세요"))

for x in range(180):
    t.pencolor(colors[x%sides])
    t.circle(x)
    t.left(360/sides+1)
    t.width(x*sides/200)