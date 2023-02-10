import turtle
t = turtle.Turtle()
t.shape('turtle')

# square(x,y) 변의 길이가 x인 사각형 y개 출력하는 함수
def square(x,y):
    t.up()
    t.goto(-300,0)
    t.down()
    for l in range(1,y+1):
        for i in range(1,5):
            t.forward(x)
            t.left(90)
        if l==y:
            break
        t.up()
        t.goto(-300+(x*2)*l,0)
        t.down()

# 변의 길이가 100인 사각형 4개 출력
square(100,4)

# t.forward(200)
# t.left(90)
# t.up()
# t.goto(200,50)
# t.down()
# t.forward(200)
# t.left(90)
# t.forward(200)
# t.left(90)
# t.forward(200)

# 사각형 만드는 함수
# def square(x):
#     for i in range(1,5):
#         t.forward(x)
#         t.left(90)

# # 이동하는 함수
# def move(a):
#     t.up()
#     t.goto(a*2,0)
#     t.down()
    
# # 사각형 만들고 이동하는 함수
# def squmove(i):
#     square(100)
#     move(100*i)
    
# # 결과 출력
# for x in range(1,4):
#     squmove(x)









