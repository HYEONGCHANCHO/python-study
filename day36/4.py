#map () 반복적인 코드를 각 요소에 적용하다
def f(x):
    return x+10

numlist=[1,2,3,4,5]
print(list(map(f,numlist)))

# def f(x):
#     return x+10
# numlist=[1,2,3,4,5]
# templist=[]
# for i in numlist:
#     templist.append(f(i))
# print(templist)