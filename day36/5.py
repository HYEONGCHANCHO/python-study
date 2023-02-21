#lambda() 한줄짜리 함수
def add(n1,n2):
    return n1+n2

print(add(10,20))

add=lambda n1,n2 : n1+n2
print(add(10,20))

#lambda는 식이 하나만 존재하는 것으로 한줄짜리 함수를 만들 때 사용할 수 있다
#map()사용
numbers=[1,2,3,4,5,6,7,8,9]
square=lambda n : n**2
square_num=[]
# for i in numbers:
#     square_num.append(square(i))
# print(square_num)

print(list(map(square,numbers)))
square_num=list(map(lambda n:n**2,numbers))
print(square_num)

print('---------------filter---------')
#filter는 이름 그대로 조건에 만족하는 것들만 추출
n=[4,3,2,1]
print(list(filter(lambda x : x>2, n)))

numbers=[234,56,234,568,974]
even_num=list(filter(lambda n : n%2==0,numbers))
for i in even_num:
    print(i)