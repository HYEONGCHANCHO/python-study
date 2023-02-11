import turtle
t=turtle.Turtle()
t.shape('turtle')
t.speed(0)


# def makestar(n):
#     for i in range(100):
#         t.left(20)
#         for x in range(n):
#             t.forward(50)
#             t.left(360/n)

# makestar(16)
def spin():
    for y in range(10):
        for x in range(10):
            t.left(5)
            t.forward(10)

spin()