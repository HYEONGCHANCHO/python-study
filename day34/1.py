# class Car:  #클래스 선언
#     x=5
# p1=Car() 
# print(p1.x) #5
# print(Car) #<class '__main__.Car'>
# class Mycar:
#     a=10

# n=Mycar()
# print(n.a)

# class Mybase:
#     a=1
# kia=Mybase()
# print(kia.a)

# class Car:
#     #속성,메소드   , 아래는 속성
#     def __init__(self):
#         self.name='hyundai'
#         self.color='red'
#     #움직이는 기능 함수 , 아래는 메소드
#     def driving(self):
#         print('드라이브가자')

# mycar=Car()
# print(mycar.name)
# print(mycar.color)
# mycar.driving()

# class Kcar:
#     #속성
#     def __init__(self):
#         self.name='kia'
#         self.color='red'
#         self.size='big'

#     #메소드
#     def driving(self):
#         print("go driving")

# yourcar=Kcar()
# print(yourcar.name)
# print(yourcar.color)
# print(yourcar.size)
# yourcar.driving()

class Hi:
    def __init__(self):
        self.name='happy'
        self.color='blue'
        self.car='kia'
    def cook(self):
        print("cooking")

hello=Hi()
print(hello.color)
print(hello.car)
print(hello.name)
hello.cook()







