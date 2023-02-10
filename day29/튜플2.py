# num=[13,22,37,41,58]
# pos = [1,2,3,[11,12,13],5,6]

# print(list(num))
# print(list(pos))
# print(tuple(num))
# print(tuple(pos))

# print(tuple("hello"))
# print(list("hello"))

# t1=('apple','banana','cherry')
# t2=(1,2,3,4)
# t3=(True,False,False)
# print(t1)
# print(t2)
# print(t3)
# t4=('abc',33,True,"male")
# print(t4)

# a,b,c =(1,2,3)
# print(a) 
# print(b)
# print(c)



#함수에서 튜플과 함께

# def add_two(x,y):
#     return x+y, x*y

# result1,result2=add_two(10,20)
# print(result1)
# print(result2)

# pass문과 함께

# def myF():
#     pass #다음줄로 넘어가시오

w=tuple("Hello")
print(w.count('l'))
print(w.index('e'))