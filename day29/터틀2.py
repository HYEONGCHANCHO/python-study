import turtle
t=turtle.Turtle()
t.shape=('turtle')
t.speed(0)

def n_polygun(n,length):
    for x in range(n):
        t.forward(length)
        t.left(360/n)


for i in range(100):
    t.left(10)
    n_polygun(13,100)