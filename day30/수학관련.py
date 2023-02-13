#사칙연산
#덧셈(+) 뺄셈(-) 곱셈(*) 나눗셈(/)
#몫(//) 나머지(%) 제곱(**)

# a=10
# b=3
# print("a +b", a+b)
# print("a -b", a-b)
# print("a *b", a*b)
# print("a/ b", a/b)
# print("a //b", a//b)
# print("a %b", a%b)
# print("a** b", a**b)

x=100
x+=100
print(x)

y=100
y//=y  #y=y/y
print("y//=y",y)

z=3
z*=z
print(z)

m=999
m-=m
print(m)

i=15
j=10
k=i%j
print("k",k)
i%=5
print("i",i)

import math
print(math.ceil(5.1)) #올림해서 6
print(math.floor(3.874)) #내림해서 3
print(abs(-10)) #절대값
x=4
y=5
print(math.pow(x,y))
print(math.pow(7,2))
print(math.sqrt(9)) #제곱근

import random
num = random.random()
print("random import 후",num)
num1=random.randint(1,500)
print("1~500 사이",num1)
