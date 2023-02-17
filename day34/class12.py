from tkinter import *
import time
import random

class Ball:
    def __init__(self,canvas,color,size,x,y,xspeed,yspeed):
        self.canvas=canvas
        self.color=color
        self.size=size
        self.x=x
        self.y=y
        self.xspeed=xspeed
        self.yspeed=yspeed
        self.id=canvas.create_oval(x,y,x+size,y+size,fill=color)
    def move(self):
        self.canvas.move(self.id,self.xspeed,self.yspeed)
        (x1,y1,x2,y2)=self.canvas.coords(self.id)  #공의 현재위치를 가져온다
        # (self.x,self.y)=(x1,y1)
        print(x1)
        print(y1)
        if x1<=0 or x2>=WIDTH:
            self.xspeed=-self.xspeed #공의 좌표가 음수, 오른쪽 경계선 넘으면 속도의 부호를 바꾼다.
        if y1<=0 or y2>=HEIGHT:
            self.yspeed=-self.yspeed



WIDTH=800
HEIGHT=400

window=Tk()
canvas=Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()


color_list=['yellow','green','blue','red','orange','pink','grey','black']
ball_list=[]

for i in range(10):
    color=random.choice(color_list)
    size=random.randrange(10,100)
    x=random.randrange(1,50)
    y=random.randrange(1,50)
    xspeed=random.randrange(1,10)
    yspeed=random.randrange(1,10)
    ball_list.append(Ball(canvas,color,size,x,y,xspeed,yspeed))

# ballA=Ball(canvas,'red',30,0,0,0,0)
while True:
    for ball in ball_list:
        ball.move()
    window.update()
    time.sleep(0.03)


    # ballA.move()
    # window.update()
    # time.sleep(0.03)
