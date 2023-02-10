# 리스트를 매개변수로

# def myF(food):
#     for x in food:
#         print(x) 

# fruits = ['apple','banana','cherry']
# myF(fruits)

# def myF(name,age,*hobby):
#     print("이름은",name,"나이는",age,"취미는",hobby)

# myF("emily",20)
# myF("emily",20,'ski',"낚시")

# def myName(*kids):
#     print("호명된 사람은"+kids[1])

# myName("Smith","John","Jane")

def greet(name,msg="금요일입니다."):
    print("Hello"+name+","+ msg)

greet("홍길동")
greet("김철수")
greet("김철수","Today")