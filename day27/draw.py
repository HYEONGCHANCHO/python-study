import turtle
t= turtle.Pen()
turtle.bgcolor("black")
t.color("green")
for a in range(5,100,3):
    for b in range(20,1,-1):
        for x in range(1,20):
            t.left(a)
            t.forward(b)