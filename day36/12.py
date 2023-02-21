# #변수 할당
# a,b,c =1,2,3
# print(a)
# print(b)
# print(c)
# #변수값 교환 , 제 3의 변수를 사용하지 않고 교환
# x=5
# y=10
# x,y=y,x
# #3개의 값을 교환할 때
# x,y,z=5,6,7
# z,x,y=x,y,z
# print(x,y,z)

# a,b,c='4 5 6'.split()
# print(a)
# print(b)
# print(c)

# mylist=[10,20,30]
# a,b,c=mylist
# print(a)
# print(b)
# print(c)

#튜플
# t=(25,35,45)
# x,y,z=t
# print(x)
# print(y)
# print(z)

#인자를 전달
def pack_it(*args): #패킹
    print(args)
    print(type(args))

x="forest"
y="hill"
z='rose'
pack_it(x,y,z)

# def pack_itt(x,y):
#     print(x)
#     print(y)

# args=["forest","rose"]
# pack_itt(*args)