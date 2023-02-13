# t1=()
# t2=(1,)
# t3=(1,2,3)
# t4=1,2,3
# t5=("a","b",("ab","cd",("xyz")))
# print(t1)
# print(t2)
# print(t3)
# print(t4)
# # print(t5)
# t5=("a","b",("ab","cd",("xyz",)))
# # print(t5[2])
# # print(t5[1:])
# # t3=(1,2,3)
# # t4=1,2,3
# # print(t3+t4)
# # print(t3*3)
# # print('t5의 len은',len(t5))
# print(t5[0])
# print(t5[1])
# print(t5[2][0])
# print(t5[2][1])
# print(t5[2][2])

# #튜플은 변수의 값교환 x,y=y,x로 가능하다
# x=10
# y=20
# x,y=y,x
# print(x)
# print(y)
# a,b=100,200
# print(a)
# print(b)

def sort_num(x):
    return x
numbers=(10,3,11,9,8)
sorted_num=tuple(sorted(numbers,key=sort_num))
print(sorted_num)

numbers=(10,3,11,9,8)
sorted_num2=tuple(sorted(numbers,key=lambda x:x))
print(sorted_num2)

numbers=(10,'3',11,9,'8')
sorted_num3=sorted(numbers,key=lambda x:int(x))
print(sorted_num3)
