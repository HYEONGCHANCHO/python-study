#클래스를 이용한 turtle
import turtle
import os

class tt(turtle.Turtle):  #turtle.Turtle을 상속받음
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.goto(0,0)
        self.showturtle()
        self.speed(1)

turtles=[]

for a in range(5):
    turtles.append(tt())  #5번 반복하면서 turtles에 객체를 넣는다
    print(turtles)

for a in turtles:
    a.fd(100)   #100 앞으로 가기

turtle.mainloop()